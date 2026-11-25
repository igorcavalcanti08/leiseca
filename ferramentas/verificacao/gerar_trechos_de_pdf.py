import json,re
RI='Regimento Interno do TJSP'; NS='Normas da Corregedoria Geral da Justiça (NSCGJ), Tomo I'
ri=json.load(open('/home/claude/interna/ri_paras.json')); ns=json.load(open('/home/claude/interna/ns_paras.json'))
NOTE=re.compile(r'\s*\((?:“Caput” com r|R)edação [^)]*\)|\s*\(Incluíd[oa] [^)]*\)|\s*\(§ [^)]*renumerado[^)]*\)|\s*\(Seção X incluída[^)]*\)')
FIX={ # footnote digits glued to words
 796:[('horas2,','horas,')], 1000:[('NSCGJ. 4','NSCGJ.')], 1045:[('cópia simples1,','cópia simples,')],
 5197:[('Padrão A3)4.','Padrão A3).')], 5204:[('indevido2.','indevido.')], 5223:[('Paulo4.','Paulo.')],
 5224:[('Brasília 5.','Brasília.')], 5225:[('forense6.','forense.')], 5229:[('eletrônicos9.','eletrônicos.')],
 5331:[('eletrônico4.','eletrônico.')], 5333:[('processo6.','processo.')], 950:[('precisa7,','precisa,')], 5207:[('arquivado4.','arquivado.')],
 38:[('Seção III Do Órgão Especial ','')], 1060:[], 838:[],
}
def P(src,i):
    s=(ri if src=='ri' else ns)[i]
    for a,b in FIX.get(i,[]) if src=='ns' or i==38 else []: s=s.replace(a,b)
    s=NOTE.sub('',s).strip()
    s=re.sub(r'\s+\d+$','',s)  # trailing footnote number
    return s
SPEC={
 'ri2':('ri',[4,5,6,7,8,9,10,11],'Composição do Tribunal'),
 'ri4':('ri',[27,28,29,38,39,51],'Tribunal Pleno e Órgão Especial'),
 'ri15':('ri',[97,99,100,103,104,116,118],'Conselho Superior da Magistratura'),
 'ri17':('ri',[123,125,128,135,136],'Eleições dos cargos de direção'),
 'ri24':('ri',[138,139,145],'Substituições'),
 'ri29a':('ri',[239,241,243],'Ouvidoria'),
 'ri33':('ri',[266,267,268,271,275],'Câmara Especial'),
 'ri62':('ri',[401,404],'Antiguidade e incompatibilidades'),
 'ri105':('ri',[540,542,545],'Prevenção'),
 'ri108':('ri',[548,549,555],'Juiz certo'),
 'ri113':('ri',[567],'Suspeição'),
 'ri144':('ri',[696,697,698,699,700],'Preferências'),
 'ri146':('ri',[704,705,706,708,712,713,714,715],'Sustentação oral: pedido e vedações'),
 'ri147':('ri',[716,720,721,723],'Sustentação oral: ordem'),
 'ri152':('ri',[725,727,728,729,730,731],'Ordem da votação'),
 'ri155':('ri',[733,734,735,739,749,755],'Acórdão'),
 'ri253':('ri',[986,990,993],'Agravo regimental'),
 'n30':('ns',[479,485,506,508,509,510,511,512],'Deveres do escrivão e ponto'),
 'n87':('ns',[796,799,804,805],'Autuação e numeração'),
 'n92':('ns',[807,808,809,810,811,812,818],'Juntada e cotas'),
 'n97':('ns',[820,825,829,830,831],'Movimentação dos autos'),
 'n100':('ns',[833,834,839,844],'Controle de prazos'),
 'n132':('ns',[946,947,948,950,951,952,953,958,960],'Intimações pela imprensa'),
 'n141':('ns',[965,966,968,969],'Intimações por edital'),
 'n143':('ns',[974,975,977,978,979,980,981,984],'Audiências'),
 'n152':('ns',[993,994,995,1000],'Gravação e estações passivas'),
 'n170':('ns',[1045,1046,1047,1048,1049,1052,1055,1060],'Desentranhamento'),
 'n1192':('ns',[5197,5204,5207],'Certificação digital'),
 'n1198':('ns',[5223,5224,5225,5226,5229],'Tempestividade no processo eletrônico'),
 'n1205':('ns',[5244,5245,5246,5247,5248,5249],'Indisponibilidade do sistema'),
 'n1205b':('ns',[5259,5260,5262],'Indisponibilidade severa'),
 'n1209':('ns',[5279,5290,5301,5305],'Distribuição eletrônica'),
 'n1224':('ns',[5330,5331,5333,5351],'Consulta aos autos eletrônicos'),
 'n1207':('ns',[5270,5271],'Alimentos de balcão'),
}
L2={k:{'lei':RI if s=='ri' else NS,'p':[P(s,i) for i in ix],'rub':r} for k,(s,ix,r) in SPEC.items()}
L2['ri134']={'lei':RI,'p':[P('ri',671),P('ri',672),P('ri',673),P('ri',684),P('ri',685),P('ri',687),P('ri',691),P('ri',693)],'rub':'Ordem dos trabalhos e votação'}
with open('/home/claude/penal/interna_L2.py','w') as f:
    f.write('# gerado por gen_L2.py a partir dos PDFs oficiais (RITJSP 12/11/2026; NSCGJ 22/10/2026)\nL2 = '+json.dumps(L2,ensure_ascii=False,indent=1)+'\n')
for k,v in L2.items():
    for s in v['p']:
        if re.search(r'[a-zà-ú\)\.]\d+[\s,.]|\d+$',s) and not re.search(r'\d{2,}',s[-6:]): pass
print(len(L2))
