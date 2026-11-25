from nl import banco, validar, VU
from fractions import Fraction as F
import random
Q, q = banco('Matemática')
M1='Porcentagem'; M2='Razão, proporção e regra de três'; M3='Médias e equações'; M4='Geometria plana'
def br(x):
    x=F(x)
    if x.denominator==1: s=f'{int(x):,}'.replace(',','.')
    else: s=f'{float(x):,.2f}'.replace(',','X').replace('.',',').replace('X','.')
    return s
def _fmtdef(v):
    from fractions import Fraction as F
    return br(v) if isinstance(v,F) else str(v)
def me(id,g,top,enun,correta,erradas,resol,fmt=_fmtdef,tags=None,origem=None,tabela=None):
    vals=[correta]+erradas; assert len(set(map(fmt,vals)))==5, (id,vals)
    rnd=random.Random(id); rnd.shuffle(vals); ks='ABCDE'
    alts={ks[i]:fmt(v) for i,v in enumerate(vals)}; gab=[k for k,v in alts.items() if v==fmt(correta)][0]
    q(id,g,'Matemática',top,enun,gab,resol,alts=alts,tags=tags or ['calculo'],origem=origem,tabela=tabela)
R=lambda v:'R$ '+f'{float(v):,.2f}'.replace(',','X').replace('.',',').replace('X','.'); P=lambda v:br(v)+'%'
# ---- PORCENTAGEM ----
v=F(200)*F(110,100)*F(90,100); assert v==198
me('MAT-P-01',M1,'Aumentos e descontos sucessivos','Um produto de R$ 200,00 teve aumento de 10% e, em seguida, desconto de 10%. O preço final é:',v,[200,F(202),F(180),F(220)],'Aumentos e descontos sucessivos se multiplicam: 200 × 1,10 × 0,90 = 200 × 0,99 = R$ 198,00. Não se anulam.',fmt=R)
r=F(100)*F(80,100)*F(75,100)*F(2,3); assert r==40
me('MAT-P-02',M1,'Porcentagem sucessiva','Numa votação, 20% dos funcionários votaram no 1º horário; no 2º, votaram 25% dos que ainda não haviam votado; no 3º, 1/3 dos restantes. Os demais não votaram. A porcentagem que não votou foi:',r,[F(35),F(25),F(45),F(60)],'Trabalhe com o que SOBRA: 100% × 0,80 × 0,75 × 2/3 = 40%.',fmt=P,tags=['calculo','ja-caiu'],origem=VU(2024,'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
A=F(30)/F(15,100); B=F(40)/F(25,100); au=(A-B)/B*100; assert (A,B,au)==(200,160,25)
me('MAT-P-03',M1,'Porcentagem','O desconto de 15% no produto A equivale a R$ 30,00; o desconto de 25% no produto B equivale a R$ 40,00. Para o mais barato custar o mesmo que o mais caro (preços sem desconto), ele deve ter aumento de:',au,[F(20),F(40),F(10),F(15)],'A = 30 ÷ 0,15 = R$ 200; B = 40 ÷ 0,25 = R$ 160. Aumento sobre o menor: 40 ÷ 160 = 25%. (Sobre o maior, 40 ÷ 200 = 20% — é a pegadinha.)',fmt=P,tags=['calculo','ja-caiu'],origem=VU(2024))
tot=F(10*20)/F(25,100); nd=(tot-200)/20; assert (tot,nd)==(800,30)
me('MAT-P-04',M1,'Porcentagem','Uma servidora digitalizou os processos de um arquivo em 30 dias. Nos 10 primeiros dias, digitalizou 25% do total, 20 processos por dia. Nos demais dias, digitalizou a mesma quantidade diária N. N vale:',nd,[F(20),F(25),F(40),F(35)],'10 dias × 20 = 200 processos = 25% → total 800. Restam 600 em 20 dias: N = 30.',tags=['calculo','ja-caiu'],origem=VU(2025))
me('MAT-P-05',M1,'Porcentagem','Um mercado movimentou R$ 2,4 trilhões em um ano. Uma variação de 0,5% sobre esse valor corresponde a:','R$ 12 bilhões',['R$ 120 bilhões','R$ 1,2 bilhão','R$ 1,2 trilhão','R$ 0,12 bilhão'],'0,5% = 0,005. 2,4 trilhões × 0,005 = 0,012 trilhão = 12 bilhões.',tags=['calculo','ja-caiu'],origem=VU(2021))
a=F(270)/F(90,100); assert a==300
me('MAT-P-06',M1,'Porcentagem','Em 2023, uma receita foi de 270 bilhões de dólares, 10% menor que a de 2022. A receita de 2022 foi de:',a,[F(297),F(280),F(243),F(310)],'270 corresponde a 90% de 2022: 270 ÷ 0,9 = 300. (Somar 10% de 270 dá 297 — erro clássico.)',fmt=lambda v:f'US$ {br(v)} bilhões',tags=['calculo','ja-caiu'],origem=VU(2023))
j=F(2000)*F(2,100)*5; assert j==200
me('MAT-P-07',M1,'Juros simples','Um capital de R$ 2.000,00 aplicado a juros simples de 2% ao mês, por 5 meses, rende juros de:',j,[F(100),F(2200),F(400),F(208)],'Juros simples: J = C × i × t = 2.000 × 0,02 × 5 = R$ 200,00.',fmt=R)
# ---- RAZÃO, PROPORÇÃO, REGRA DE TRÊS ----
m=F(20)/(3-2); s2=3*m; s3=2*m; s1=s2*F(5,3); assert (s1,s2,s3)==(100,60,40)
me('MAT-R-01',M2,'Razão e proporção','Numa escola, a razão entre os alunos do 2º e do 1º ano é 3/5, e entre os do 3º e do 2º ano é 2/3. O 2º ano tem 20 alunos a mais que o 3º. O total de alunos dos três anos é:',s1+s2+s3,[F(180),F(120),F(240),F(160)],'3º/2º = 2/3 → 2º = 3k e 3º = 2k; diferença k = 20 → 2º = 60, 3º = 40. 2º/1º = 3/5 → 1º = 100. Total: 200.',tags=['calculo','ja-caiu'],origem=VU(2024))
d=F(10*6*8,4*6); assert d==20
me('MAT-R-02',M2,'Regra de três composta','Seis máquinas, trabalhando 8 horas por dia, fazem um serviço em 10 dias. Quatro máquinas iguais, trabalhando 6 horas por dia, farão o mesmo serviço em:',d,[F(15),F(18),F(12),F(25)],'Dias são inversamente proporcionais a máquinas e a horas: 10 × (6/4) × (8/6) = 20 dias.',fmt=lambda v:f'{br(v)} dias',tags=['calculo','ja-caiu'],origem=VU(2024,'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
x=F(12*45,15); assert x==36
me('MAT-R-03',M2,'Regra de três inversa','Quinze escreventes cumprem uma tarefa em 12 dias. Se fossem 45 escreventes, no mesmo ritmo, cumpririam a tarefa em:',F(4),[F(36),F(6),F(3),F(8)],'Mais pessoas, menos dias (inversa): 12 × 15 ÷ 45 = 4 dias.',fmt=lambda v:f'{br(v)} dias')
c3=len([k for k in range(1,101) if k%3==0 and k%4!=0]); assert c3==25
me('MAT-R-04',M2,'Múltiplos','Quantos números de 1 a 100 são múltiplos de 3, mas não de 4?',c3,[F(33),F(8),F(27),F(24)],'Múltiplos de 3: 33. Múltiplos de 3 e de 4 ao mesmo tempo = múltiplos de 12: 8. 33 − 8 = 25.',tags=['calculo','ja-caiu'],origem=VU(2024,'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
# ---- MÉDIAS E EQUAÇÕES ----
nm=(20*25-3*30+18+20+22)/F(20); assert nm==F(235,10)
me('MAT-M-01',M3,'Média','A média de idade dos 20 jogadores de um time é 25 anos. Saem os três mais velhos, de 30 anos cada, e entram três de 18, 20 e 22 anos. A nova média é:',nm,[F(25),F(24),F(22),F(26)],'Soma inicial: 20 × 25 = 500. Nova soma: 500 − 90 + 60 = 470. Média: 470 ÷ 20 = 23,5 anos.',fmt=lambda v:br(v).replace(',50',',5')+' anos',tags=['calculo','ja-caiu'],origem=VU(2024))
mp=F(6*2+8*3,5); assert mp==F(72,10)
me('MAT-M-02',M3,'Média ponderada','Um candidato tirou 6 na prova de peso 2 e 8 na prova de peso 3. A média ponderada é:',mp,[F(7),F(7,1)+F(4,10),F(68,10),F(75,10)],'(6×2 + 8×3) ÷ (2+3) = 36 ÷ 5 = 7,2.',fmt=lambda v:br(v).replace(',20',',2').replace(',40',',4').replace(',80',',8').replace(',50',',5'))
me('MAT-M-03',M3,'Sistema de equações','Três cadernos e duas canetas custam R$ 23,00; dois cadernos e cinco canetas custam R$ 30,00. Um caderno e uma caneta, juntos, custam:',F(9),[F(10),F(8),F(11),F(7)],'3x + 2y = 23 e 2x + 5y = 30 → x = 5 (caderno) e y = 4 (caneta). x + y = R$ 9,00.',fmt=R,tags=['calculo','ja-caiu'],origem=VU(2023))
assert 3*5+2*4==23 and 2*5+5*4==30
I=F(200-25)/F(5,2); Pd=I/2+5; Mc=2*Pd+10; assert (I,Pd,Mc)==(70,40,90)
me('MAT-M-04',M3,'Equação do 1º grau','Três vendedores venderam 200 carros no mês. Pedro vendeu 5 a mais que a metade de Igor, e Marcelo vendeu 10 a mais que o dobro de Pedro. Marcelo vendeu:',Mc,[F(70),F(40),F(80),F(100)],'I + (I/2 + 5) + (I + 20) = 200 → 2,5I + 25 = 200 → I = 70; Pedro = 40; Marcelo = 2×40 + 10 = 90.',tags=['calculo','ja-caiu'],origem=VU(2024))
# ---- GEOMETRIA ----
xq=50; resto=xq*xq-(xq-30)*(xq-10); assert resto==1700
me('MAT-G-01',M4,'Áreas','Um terreno quadrado de lado 50 m teve separado um setor retangular de (50 − 30) m por (50 − 10) m. A área restante do terreno é:',resto,[F(800),F(2500),F(1500),F(1900)],'Quadrado: 50² = 2.500 m². Retângulo: 20 × 40 = 800 m². Resta 1.700 m².',fmt=lambda v:f'{br(v)} m²',tags=['calculo','ja-caiu'],origem=VU(2024))
me('MAT-G-02',M4,'Triângulo retângulo','Um logotipo tem a forma de um triângulo retângulo de lados proporcionais a 5, 12 e 13. Impresso com o menor lado medindo 10 cm, sua área é:',F(120),[F(240),F(60),F(130),F(150)],'Escala 2: lados 10, 24 e 26 (o maior é a hipotenusa). Catetos 10 e 24 → área = 10 × 24 ÷ 2 = 120 cm².',fmt=lambda v:f'{br(v)} cm²',tags=['calculo','ja-caiu'],origem=VU(2023))
me('MAT-G-03',M4,'Perímetro','Um quadrado tem área de 2.601 m². Seu perímetro é:',F(204),[F(51),F(102),F(208),F(2601,4)],'Lado = √2.601 = 51 m. Perímetro = 4 × 51 = 204 m.',fmt=lambda v:f'{br(v)} m',tags=['calculo','ja-caiu'],origem=VU(2024,'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
assert 51*51==2601
from mat2 import add
add(me, R, P, br, M1, M2, M3, M4)
if __name__=='__main__':
    import json,collections
    e=validar(Q); print(len(Q),e,collections.Counter(x['grupo'] for x in Q))
    for o in Q: print(o['id'],o['gabarito'],o['alternativas'])
    json.dump(Q,open('mat.json','w'),ensure_ascii=False,indent=1)
