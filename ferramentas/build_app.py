# Injeta bancos e quadros extras no app (base: leiseca3/index.html)
import json, sys, re, shutil, os
import os as _os
BASE=_os.environ.get('LEISECA_BASE','/home/claude/leiseca3'); OUT=sys.argv[1]; VER=sys.argv[2]; bancos=sys.argv[3].split(','); quadros=sys.argv[4].split(',') if len(sys.argv)>4 and sys.argv[4] else []
remover=sys.argv[5].split(',') if len(sys.argv)>5 and sys.argv[5] else []
os.makedirs(OUT, exist_ok=True)
for f in ['manifest.json','icon-192.png','icon-512.png']: shutil.copy(f'{BASE}/{f}', OUT)
s=open(f'{BASE}/index.html').read()
extra=[]
for b in bancos:
    for x in json.load(open(b)):
        x={k:v for k,v in x.items() if v not in ('',None)}; extra.append(x)
blob=json.dumps(extra,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
qd={}
for f in quadros: qd.update(json.load(open(f)))
s=s.replace("const SEED = [...PENAL, ...SEED_CPC];", "// Bancos adicionais (texto legal conferido no Planalto)\nconst EXTRA = "+blob+";\nconst SEED = [...PENAL, ...EXTRA, ...SEED_CPC];")
s=s.replace("const quadro = g =>", "Object.assign(QUADROS, "+json.dumps(qd,ensure_ascii=False)+");\nconst quadro = g =>")
s=re.sub(r"const APP_VERSION = '[^']+';", f"const APP_VERSION = '{VER}';", s)
# migração genérica por versão de banco
s=s.replace("const SEED_V1_REMOVER = [", "const SEED_VERSION = "+str(int(VER.replace('.',''))) +";\nconst SEED_V1_REMOVER = ["+''.join(f"'{r}', " for r in remover))
s=s.replace("S.meta.seedVersion = 2; await setMeta('seedVersion', 2); }\n    if ((S.meta.seedVersion || 1) < 2) await atualizarExemplos();",
            "S.meta.seedVersion = SEED_VERSION; await setMeta('seedVersion', SEED_VERSION); }\n    if ((S.meta.seedVersion || 1) < SEED_VERSION) await atualizarExemplos();")
s=s.replace("const n = await importarQuestoes(parseLote(JSON.stringify(PENAL)).validas);\n  S.meta.seedVersion = 2; await setMeta('seedVersion', 2);",
            "const n = await importarQuestoes(parseLote(JSON.stringify(SEED.filter(q => !SEED_V1_REMOVER.includes(q.id)))).validas);\n  S.meta.seedVersion = SEED_VERSION; await setMeta('seedVersion', SEED_VERSION);")
s=s.replace("toast(`Direito Penal atualizado: ${n} questões novas","toast(`Banco atualizado: ${n} questões novas")
s=s.replace("if (!S.meta.seeded && S.q.size === 0) await importarQuestoes(parseLote(JSON.stringify(SEED)).validas);", "if (!S.meta.seeded && S.q.size === 0) await importarQuestoes(parseLote(JSON.stringify(SEED.filter(q => !SEED_V1_REMOVER.includes(q.id)))).validas);")
s=s.replace('/^(Art\\.|', '/^(Art\\.|Artigo |\\d+\\s*[-–.]\\s|', 1)

# ---- v2.9: matérias sem lei (Português, Informática, RL, Matemática): tabela e rótulos ----
s=s.replace('<p class="enunciado" id="qText"></p>', '<p class="enunciado" id="qText"></p>\n    <div id="qTab" class="qtabw"></div>', 1)
s=s.replace(".alts{list-style:none;", ".qtabw{overflow-x:auto}.qtab{border-collapse:collapse;margin:.6rem 0 0;font-size:calc(var(--fs) * .9);font-variant-numeric:tabular-nums}.qtab th,.qtab td{border:1px solid var(--line);padding:.25rem .55rem;text-align:center}.qtab th{background:var(--line);font-weight:600}\n.alts{list-style:none;", 1)
s=s.replace("  $('#qText').textContent = q.enunciado;\n", "  $('#qText').textContent = q.enunciado;\n  $('#qTab').innerHTML = q.tabela ? tabelaHtml(q.tabela) : '';\n", 1)
s=s.replace("function atualizarTopoQuiz() {", "function tabelaHtml(t) {\n  const cab = t.colunas || [];\n  return `<table class=\"qtab\">${cab.length ? `<tr>${cab.map(c => `<th>${esc(String(c))}</th>`).join('')}</tr>` : ''}`\n    + (t.linhas || []).map(l => `<tr>${l.map((c, i) => i === 0 && t.rotulos !== false ? `<th>${esc(String(c))}</th>` : `<td>${esc(String(c))}</td>`).join('')}</tr>`).join('') + '</table>';\n}\nconst ehMateriaDeLei = m => { const x = EDITAL.blocos.flatMap(b => b.materias).find(y => y.nome === m); return !x || x.leis.length > 0; };\nfunction atualizarTopoQuiz() {", 1)
old = """  h += `<div class="label">Texto da lei · ${esc(q.lei)} · ${esc(q.artigo)}</div>`
    + `<p class="lei">${destacarRubricas(highlight(q.textoLei, q.gabarito === 'E' || q.tipo === 'ME' ? q.trechoOriginal : '', 'ok'))}</p>`;"""
new = """  if (ehMateriaDeLei(q.materia)) h += `<div class="label">Texto da lei · ${esc(q.lei)} · ${esc(q.artigo)}</div>`
    + `<p class="lei">${destacarRubricas(highlight(q.textoLei, q.gabarito === 'E' || q.tipo === 'ME' ? q.trechoOriginal : '', 'ok'))}</p>`;
  else h += `<div class="label">${q.tipo === 'ME' ? 'Resolução' : 'Regra'} · ${esc(q.lei)}</div>`
    + `<p class="lei" style="font-family:inherit">${highlight(q.textoLei, q.gabarito === 'E' || q.tipo === 'ME' ? q.trechoOriginal : '', 'ok')}</p>`;"""
assert old in s; s=s.replace(old,new,1)
s=s.replace("${q.origem.adaptada ? ' · adaptada para Certo/Errado' : ''}", "${q.origem.adaptada ? (q.tipo === 'ME' ? ' · adaptada' : ' · adaptada para Certo/Errado') : ''}", 1)
s=s.replace("  if (q.verificado != null && typeof q.verificado !== 'boolean')", "  if (q.tabela != null && (typeof q.tabela !== 'object' || !Array.isArray(q.tabela.linhas))) erros.push(`${pre}: \\\"tabela\\\" deve ter \\\"linhas\\\" (lista)`);\n  if (q.verificado != null && typeof q.verificado !== 'boolean')", 1)
assert 'tabelaHtml(q.tabela)' in s and 'id="qTab"' in s and '.qtab{' in s and 'ehMateriaDeLei(q.materia)' in s and 'q.tabela != null' in s

# ---- v2.11: atualização também corrige o conteúdo das questões já existentes (o progresso fica em outro store) ----
old_up = "  S.meta.seedVersion = SEED_VERSION; await setMeta('seedVersion', SEED_VERSION);\n  if (rem.length || n)"
new_up = """  const alt = [];
  SEED.forEach((o, i) => { if (!S.q.has(o.id) || SEED_V1_REMOVER.includes(o.id)) return; const r = validarQuestao(o, i); if (!r.q) return; const old = S.q.get(o.id); if (old.importadoEm != null) r.q.importadoEm = old.importadoEm; const k = x => JSON.stringify(Object.keys(x).sort().map(c => [c, x[c]])); if (k(r.q) !== k(old)) alt.push(r.q); });
  if (alt.length) { await putMany('questions', alt); alt.forEach(q => S.q.set(q.id, q)); }
  S.meta.seedVersion = SEED_VERSION; await setMeta('seedVersion', SEED_VERSION);
  if (rem.length || n || alt.length)"""
assert old_up in s
s = s.replace(old_up, new_up, 1)
s = s.replace("toast(`Banco atualizado: ${n} questões novas${rem.length ? `, ${rem.length} antigas removidas` : ''}.`, 4500)", "toast(`Banco atualizado: ${n} questões novas${alt.length ? `, ${alt.length} revisadas` : ''}${rem.length ? `, ${rem.length} antigas removidas` : ''}.`, 4500)", 1)
assert 'alt.length ? `, ${alt.length} revisadas`' in s

assert '/^(Art\\.|Artigo |' in s
assert 'const EXTRA' in s and 'SEED_VERSION' in s and 'Object.assign(QUADROS' in s and "SEED.filter(q => !SEED_V1_REMOVER" in s

# ---- Outro edital (opcional, por variáveis de ambiente) ----
# LEISECA_EDITAL=arquivo.js  -> objeto JS que substitui "const EDITAL = {...};" (mesmo formato: prova, blocos[], materias[] com nome, leis, recorte, questoes)
# LEISECA_TITULO="Lei Seca C/E — ÓRGÃO"  -> título da página e nome do app instalado
# LEISECA_SEM_TJSP=1  -> remove os bancos embutidos do TJSP (PENAL e SEED_CPC) da base
_ed = _os.environ.get('LEISECA_EDITAL')
if _ed:
    i = s.index('const EDITAL = {'); j = s.index('\nconst MATERIAS_EDITAL')
    s = s[:i] + 'const EDITAL = ' + open(_ed).read().strip().rstrip(';') + ';' + s[j:]
if _os.environ.get('LEISECA_SEM_TJSP') == '1':
    s = re.sub(r'const PENAL = \[.*?\];\n', 'const PENAL = [];\n', s, count=1, flags=re.S)
    i = s.index('const SEED_CPC = ['); j = s.index('\n];', i)
    s = s[:i] + 'const SEED_CPC = [' + s[j:]
_tt = _os.environ.get('LEISECA_TITULO')
if _tt:
    s = re.sub(r'<title>[^<]*</title>', f'<title>{_tt}</title>', s, count=1)
open(f'{OUT}/index.html','w').write(s)
sw=open(f'{BASE}/sw.js').read()
if _tt:
    mf=json.load(open(f'{BASE}/manifest.json')); mf['name']=_tt; json.dump(mf,open(f'{OUT}/manifest.json','w'),ensure_ascii=False,indent=2)
sw=re.sub(r"leiseca-v[\d.]+", f"leiseca-v{VER}", sw); open(f'{OUT}/sw.js','w').write(sw)
print('ok', len(extra), 'questões extras;', len(qd), 'quadros')
