import re, json, sys
raw = open('/tmp/ns/ns_raw.txt', encoding='utf-8').read().replace('\f', '\n')
lines = [l.rstrip() for l in raw.split('\n')]
FOOT = re.compile(r'^(Provs?\.|Prov |CJE|D\. ?\d|L\. ?\d|L\.C\.|LC |RITJ|Res\.|Resol|Lei |Comunicado|Com\.|Decreto|Dec\.|CPC|CF,|CF |CPP|Port\.|Portaria|Provimento|Parecer|Proc\.|Ato |Assento|Cód\.|Código|Instr|Inst\.|Of\.|Ofício|Recomend|Res\. CNJ|Resolução|Lei Federal|Lei Estadual|Lei Complementar|CLT|ECA|LEP|Súmula|DOJ|DJE|Normas)')
START = re.compile(r'^(Art\. \d|§ ?\d|Parágrafo único|[IVXL]+ ?[-–]|[a-z]\) |\d+(\.\d+)* ?[-–] |Seção |Subseção |SEÇÃO|CAPÍTULO|Seção [IVXL])')
out = []; cur = None
for l in lines:
    s = l.strip()
    if not s: continue
    if re.fullmatch(r'\d{1,3}', s): continue
    if FOOT.match(s) and (cur is None or len(s) < 160): continue
    if START.match(s):
        if cur: out.append(cur)
        cur = s
    else:
        if cur is None: continue
        cur = (cur[:-1] + s) if cur.endswith('-') and not cur.endswith(' -') else (cur + ' ' + s)
if cur: out.append(cur)
def clean(p):
    p = re.sub(r'([.;:)])\d{1,2}(?=\s|$)', r'\1', p)   # footnote refs
    p = re.sub(r'\s+', ' ', p).strip()
    return p
out = [clean(p) for p in out]
json.dump(out, open('/home/claude/interna/ns_paras.json', 'w'), ensure_ascii=False)
print(len(out))
