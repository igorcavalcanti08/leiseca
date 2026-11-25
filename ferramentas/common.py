import re, hashlib, unicodedata

def norm(s):
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'\s*\((Reda[çc][ãa]o dada|Inclu[íi]d[oa]|Vide|Vig[êe]ncia|Renumerad|Revogad|Regulamento|Acrescid)[^)]*\)+', '', s, flags=re.I)
    s = re.sub(r'\s*\(NR\)', '', s)
    s = re.sub(r'\s+Vig[êe]ncia\s*$', '', s, flags=re.I)
    s = re.sub(r'[–—‑]', '-', s).replace('“', '"').replace('”', '"')
    s = re.sub(r'\s+', ' ', s); s = re.sub(r'\s+([:;.,])', r'\1', s); s = re.sub(r'([.:;])\.+', r'\1', s)
    return s.strip()

def h(s): return hashlib.sha256(norm(s).encode()).hexdigest()[:12]

def factory(Q, L, materia, QC, fonte_base, prefixo_origem='Escrevente Técnico Judiciário — '):
    def q(id, grupo, artigo, arts, enun, gab, com, alt='', orig='', tags=(), qc=None, letra=None, lei=None):
        leis = {a: v for a, v in L.items()}
        textos = [p for a in arts for p in leis[a]['p']]
        d = dict(id=id, tipo='CE', materia=materia, lei=lei or leis[arts[0]]['lei'], grupo=grupo, artigo=artigo,
                 enunciado=enun, gabarito=gab, textoLei='\n'.join(textos), comentario=com, tags=list(tags), verificado=True)
        if alt: d['trechoAlterado'] = alt
        if orig: d['trechoOriginal'] = orig
        r = leis[arts[0]].get('rub')
        if r: d['rubrica'] = r
        fonte = fonte_base
        if qc:
            ano, org = QC[qc]
            d['origem'] = {'banca': 'VUNESP', 'ano': ano, 'cargo': prefixo_origem + org, 'adaptada': True}
            d['tags'] = ['ja-caiu'] + d['tags']
            fonte = (f'Adaptada de VUNESP {ano}, {org}, Escrevente — QConcursos {qc}{", alternativa " + letra if letra else ""}. '
                     'Gabarito deduzido da lei, não conferido com o gabarito oficial. ' + fonte_base)
        d['fonte'] = fonte
        Q.append(d)
    return q

def validar(Q):
    import collections
    err = []
    ids = collections.Counter(x['id'] for x in Q)
    err += [(k, 'id duplicado') for k, v in ids.items() if v > 1]
    for x in Q:
        if x['gabarito'] == 'E' and not x.get('trechoAlterado'): err.append((x['id'], 'E sem trechoAlterado'))
        if x.get('trechoAlterado') and x['trechoAlterado'].lower() not in x['enunciado'].lower(): err.append((x['id'], 'trechoAlterado fora do enunciado'))
        if x.get('trechoOriginal') and x['trechoOriginal'].lower() not in x['textoLei'].lower(): err.append((x['id'], 'trechoOriginal fora do textoLei'))
    return err
