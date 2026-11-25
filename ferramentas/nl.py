# Helper para matérias sem lei (Português, Informática, Raciocínio Lógico, Matemática)
FONTE = 'Questão original no padrão de cobrança VUNESP (Escrevente TJ-SP 2021–2025, analisadas no QConcursos em 24/11/2026)'
def banco(materia):
    Q = []
    def q(id, grupo, tema, topico, enun, gab, regra, alt=None, orig=None, tags=None, com=None, alts=None, tabela=None, origem=None):
        o = {'id': id, 'tipo': 'ME' if alts else 'CE', 'materia': materia, 'lei': tema, 'grupo': grupo, 'artigo': topico,
             'enunciado': enun, 'gabarito': gab, 'textoLei': regra, 'tags': tags or [], 'verificado': True, 'fonte': FONTE}
        if alts: o['alternativas'] = alts
        if alt: o['trechoAlterado'] = alt
        if orig: o['trechoOriginal'] = orig
        if com: o['comentario'] = com
        if tabela: o['tabela'] = tabela
        if origem: o['origem'] = origem
        Q.append(o)
    return Q, q
def validar(Q):
    err = []; ids = set()
    for o in Q:
        i = o['id']
        if i in ids: err.append(i + ' duplicado')
        ids.add(i)
        if o['tipo'] == 'CE':
            if o['gabarito'] not in 'CE': err.append(i + ' gab')
            if o['gabarito'] == 'E':
                if not o.get('trechoAlterado'): err.append(i + ' sem alt')
                elif o['trechoAlterado'].lower() not in o['enunciado'].lower(): err.append(i + ' alt fora do enunciado')
        else:
            if o['gabarito'] not in o['alternativas']: err.append(i + ' gab ME')
            if len(set(o['alternativas'].values())) != len(o['alternativas']): err.append(i + ' alternativas repetidas')
        if o.get('trechoOriginal') and o['trechoOriginal'].lower() not in o['textoLei'].lower(): err.append(i + ' orig fora da regra')
    return err
def VU(ano, cargo='Escrevente Técnico Judiciário — TJ-SP'):
    return {'banca': 'VUNESP', 'ano': ano, 'cargo': cargo, 'adaptada': True}
