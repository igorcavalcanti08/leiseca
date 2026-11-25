# Ampliação v2.10 — Matemática (importado por mat.py)
from fractions import Fraction as F
def add(me, R, P, br, M1, M2, M3, M4):
    M5='Divisibilidade, frações e tempo'; M6='Tabelas e gráficos'
    U=lambda s: (lambda v: f'{br(v)} {s}')
    # ---- PORCENTAGEM ----
    v=F(3200)*F(115,100); assert v==3680
    me('MAT-P-08',M1,'Aumento percentual','Um salário de R$ 3.200,00 teve reajuste de 15%. O novo salário é:',v,[F(3215),F(3520),F(3480),F(4800)],'3.200 × 1,15 = R$ 3.680,00. (15% de 3.200 = 480.)',fmt=R)
    me('MAT-P-09',M1,'Variação percentual','O preço de um serviço caiu de R$ 250,00 para R$ 200,00. A redução foi de:',F(20),[F(25),F(50),F(15),F(30)],'Redução sobre o valor INICIAL: 50 ÷ 250 = 0,20 = 20%.',fmt=P)
    me('MAT-P-10',M1,'Variação percentual','O preço de um serviço subiu de R$ 200,00 para R$ 250,00. O aumento foi de:',F(25),[F(20),F(50),F(15),F(30)],'Aumento sobre o valor INICIAL: 50 ÷ 200 = 0,25 = 25%. (Compare: a queda de 250 para 200 é de 20%.)',fmt=P)
    d=(1-F(80,100)*F(90,100))*100; assert d==28
    me('MAT-P-11',M1,'Descontos sucessivos','Dois descontos sucessivos, de 20% e de 10%, equivalem a um desconto único de:',d,[F(30),F(25),F(32),F(18)],'Sobra 0,80 × 0,90 = 0,72 do preço → desconto de 28%, não de 30%.',fmt=P)
    me('MAT-P-12',M1,'Porcentagem de porcentagem','Numa vara, 40% dos processos são cíveis e, desses, 30% estão conclusos ao juiz. Os processos cíveis conclusos representam, do total:',F(12),[F(70),F(10),F(30),F(34)],'30% de 40% = 0,30 × 0,40 = 0,12 = 12%.',fmt=P)
    me('MAT-P-13',M1,'Porcentagem','Dos 24 servidores de um cartório, 18 foram aprovados num curso. O percentual de aprovados é:',F(75),[F(18),F(60),F(80),F(72)],'18 ÷ 24 = 0,75 = 75%.',fmt=P)
    o=F(150)/F(125,100); assert o==120
    me('MAT-P-14',M1,'Valor anterior','Após um aumento de 25%, um produto passou a custar R$ 150,00. O preço antes do aumento era:',o,[F(1125,10),F(125),F(130),F(100)],'150 corresponde a 125%: 150 ÷ 1,25 = R$ 120,00. (Tirar 25% de 150 dá 112,50 — erro clássico.)',fmt=R)
    me('MAT-P-15',M1,'Lucro','Um comerciante comprou um produto por R$ 80,00 e o vendeu por R$ 100,00. O lucro, em relação ao preço de custo, foi de:',F(25),[F(20),F(80),F(15),F(30)],'Lucro 20; sobre o custo: 20 ÷ 80 = 25%. (Sobre o preço de venda seria 20 ÷ 100 = 20%.)',fmt=P)
    # ---- RAZÃO, PROPORÇÃO, REGRA DE TRÊS ----
    k=F(1800,9); assert 4*k==800
    me('MAT-R-05',M2,'Divisão proporcional','R$ 1.800,00 serão divididos em partes diretamente proporcionais a 2, 3 e 4. A maior parte é:',4*k,[F(600),F(900),F(400),F(720)],'Soma das partes: 2 + 3 + 4 = 9. Cada parte vale 1.800 ÷ 9 = 200. A maior: 4 × 200 = R$ 800,00.',fmt=R)
    k2=F(2100)/(F(1,2)+F(1,5)); assert (k2/5)==600
    me('MAT-R-06',M2,'Divisão inversamente proporcional','R$ 2.100,00 serão divididos em partes inversamente proporcionais a 2 e 5. A menor parte é:',k2/5,[F(1500),F(840),F(700),F(1050)],'Inversamente a 2 e 5 = diretamente a 1/2 e 1/5 (ou a 5 e 2). Soma 7 → 2.100 ÷ 7 = 300. Partes: 5×300 = 1.500 e 2×300 = 600. Menor: R$ 600,00.',fmt=R)
    me('MAT-R-07',M2,'Escala','Numa planta na escala 1:500, uma parede mede 4 cm. Na realidade, ela mede:',F(20),[F(2),F(200),F(125),F(50)],'1 cm no desenho = 500 cm reais. 4 × 500 = 2.000 cm = 20 m.',fmt=U('m'))
    me('MAT-R-08',M2,'Razão','Num setor com 64 servidores, a razão entre homens e mulheres é 3/5. O número de mulheres é:',F(40),[F(24),F(38),F(32),F(45)],'3 + 5 = 8 partes; 64 ÷ 8 = 8 por parte. Mulheres: 5 × 8 = 40.')
    v=F(480)*F(10,8)*F(9,6); assert v==900
    me('MAT-R-09',M2,'Regra de três composta','Oito escreventes digitalizam 480 processos em 6 dias. No mesmo ritmo, dez escreventes, em 9 dias, digitalizarão:',v,[F(576),F(720),F(1080),F(600)],'Processos são diretamente proporcionais a escreventes e a dias: 480 × (10/8) × (9/6) = 480 × 1,25 × 1,5 = 900.',tags=['calculo','ja-caiu'])
    me('MAT-R-10',M2,'Regra de três inversa','A 80 km/h, uma viagem dura 3 horas. A 120 km/h, a mesma viagem dura:',F(2),[F(4),F(45,10),F(25,10),F(18,10)],'Velocidade e tempo são inversamente proporcionais: 3 × 80 ÷ 120 = 2 horas.',fmt=lambda v:br(v).replace(',50',',5').replace(',80',',8')+' h')
    me('MAT-R-11',M2,'Regra de três simples','Uma receita usa 3 xícaras de farinha para 12 pessoas. Para 20 pessoas, serão necessárias:',F(5),[F(4),F(6),F(8),F(36,10)],'3 ÷ 12 = 0,25 xícara por pessoa; 20 × 0,25 = 5 xícaras.',fmt=lambda v:br(v).replace(',60',',6')+' xícaras')
    t=1/(F(1,6)+F(1,3)); assert t==2
    me('MAT-R-12',M2,'Torneiras','Uma torneira enche um tanque em 6 horas; outra, em 3 horas. Abertas juntas, enchem o tanque em:',t,[F(45,10),F(9),F(3),F(15,10)],'Por hora: 1/6 + 1/3 = 1/6 + 2/6 = 1/2 do tanque. Tanque cheio em 2 horas.',fmt=lambda v:br(v).replace(',50',',5')+' h')
    # ---- MÉDIAS E EQUAÇÕES ----
    me('MAT-M-05',M3,'Média','A média de cinco números é 12. Retirando-se um deles, a média dos quatro restantes passa a ser 11. O número retirado é:',F(16),[F(12),F(1),F(11),F(14)],'Soma dos cinco: 5 × 12 = 60. Soma dos quatro: 4 × 11 = 44. Retirado: 60 − 44 = 16.')
    x=5*F(74,10)-4*7; assert x==9
    me('MAT-M-06',M3,'Média','Um candidato tem média 7 em quatro provas. Para ficar com média 7,4 nas cinco provas, precisa tirar na quinta:',x,[F(74,10),F(8),F(10),F(85,10)],'Total necessário: 5 × 7,4 = 37. Já tem 4 × 7 = 28. Precisa de 37 − 28 = 9.',fmt=lambda v:br(v).replace(',40',',4').replace(',50',',5'))
    f_=12; assert 3*f_+12==2*(f_+12)
    me('MAT-M-07',M3,'Equação do 1º grau','Hoje, um pai tem o triplo da idade do filho. Daqui a 12 anos, terá o dobro. A soma das idades atuais é:',F(48),[F(36),F(60),F(24),F(52)],'Filho x, pai 3x. Em 12 anos: 3x + 12 = 2(x + 12) → x = 12. Pai 36. Soma: 48.')
    xi=F(4800-20*150,20); assert xi==90
    me('MAT-M-08',M3,'Sistema de equações','Um evento vendeu 150 ingressos, inteiras a R$ 40,00 e meias a R$ 20,00, e arrecadou R$ 4.800,00. Foram vendidas quantas meias?',150-xi,[F(90),F(75),F(50),F(80)],'Se todos fossem meia: 150 × 20 = 3.000. A diferença (1.800) vem das inteiras, que custam 20 a mais: 1.800 ÷ 20 = 90 inteiras. Meias: 60.',tags=['calculo','ja-caiu'])
    assert 2*22+15==3*22-7
    me('MAT-M-09',M3,'Equação do 1º grau','O dobro de um número, mais 15, é igual ao triplo desse número, menos 7. O número é:',F(22),[F(8),F(15),F(7),F(30)],'2x + 15 = 3x − 7 → x = 22.')
    mp=F(6*1+8*1+9*2,4); assert mp==8
    me('MAT-M-10',M3,'Média ponderada','Notas 6 e 8 têm peso 1 cada; a nota 9 tem peso 2. A média ponderada é:',mp,[F(77,10),F(23,3)+F(1,3)+F(1,2),F(75,10),F(7)],'(6×1 + 8×1 + 9×2) ÷ (1+1+2) = 32 ÷ 4 = 8.',fmt=lambda v:br(v).replace(',70',',7').replace(',50',',5'))
    assert 5*8==40
    me('MAT-M-11',M3,'Equação do 2º grau','Um retângulo tem comprimento 3 cm maior que a largura e área de 40 cm². Seu perímetro é:',F(26),[F(40),F(13),F(20),F(30)],'x(x + 3) = 40 → x² + 3x − 40 = 0 → x = 5 (a raiz −8 não serve). Lados 5 e 8; perímetro 2 × (5 + 8) = 26 cm.',fmt=U('cm'))
    co=F(80-2*30,2); assert co==10
    me('MAT-M-12',M3,'Sistema de equações','Num sítio há galinhas e coelhos: 30 cabeças e 80 pés. O número de coelhos é:',co,[F(20),F(15),F(8),F(25)],'Se todos fossem galinhas: 60 pés. Faltam 20 pés, e cada coelho tem 2 a mais: 20 ÷ 2 = 10 coelhos.')
    # ---- GEOMETRIA E MEDIDAS ----
    me('MAT-G-04',M4,'Áreas','Um retângulo tem perímetro de 36 m, e o comprimento é o dobro da largura. Sua área é:',F(72),[F(36),F(81),F(64),F(54)],'Largura x, comprimento 2x: 2(x + 2x) = 36 → x = 6. Área: 6 × 12 = 72 m².',fmt=U('m²'))
    me('MAT-G-05',M4,'Teorema de Pitágoras','Os catetos de um triângulo retângulo medem 6 cm e 8 cm. A hipotenusa mede:',F(10),[F(14),F(12),F(7),F(48)],'h² = 6² + 8² = 36 + 64 = 100 → h = 10 cm.',fmt=U('cm'))
    me('MAT-G-06',M4,'Áreas','Um trapézio tem bases de 10 m e 6 m e altura de 4 m. Sua área é:',F(32),[F(64),F(40),F(24),F(60)],'Área = (B + b) × h ÷ 2 = (10 + 6) × 4 ÷ 2 = 32 m².',fmt=U('m²'))
    me('MAT-G-07',M4,'Volume e capacidade','Uma caixa-d\'água tem 2 m × 1,5 m × 0,8 m. Sua capacidade é de:',F(2400),[F(240),F(24000),F(4300),F(2000)],'Volume: 2 × 1,5 × 0,8 = 2,4 m³. Como 1 m³ = 1.000 L, são 2.400 litros.',fmt=U('L'))
    me('MAT-G-08',M4,'Unidades de medida','Uma área de 3 m² equivale a:',F(30000),[F(300),F(3000),F(300000),F(30)],'1 m² = 100 cm × 100 cm = 10.000 cm². Logo, 3 m² = 30.000 cm².',fmt=U('cm²'))
    me('MAT-G-09',M4,'Áreas','Usando π = 3, a área de um círculo de raio 5 m é:',F(75),[F(30),F(15),F(150),F(225)],'A = π r² = 3 × 25 = 75 m². (30 seria o comprimento da circunferência, 2πr.)',fmt=U('m²'))
    # ---- DIVISIBILIDADE, FRAÇÕES E TEMPO ----
    from math import lcm, gcd
    assert lcm(12,18)==36
    me('MAT-D-01',M5,'MMC','Dois ônibus partem juntos às 7h; um sai a cada 12 minutos e o outro a cada 18 minutos. Voltarão a partir juntos às:','7h36',['7h30','7h18','7h54','8h12'],'MMC(12, 18) = 36 minutos → 7h + 36 min = 7h36.')
    g=gcd(48,72); assert g==24 and 48//g+72//g==5
    me('MAT-D-02',M5,'MDC','Duas fitas de 48 cm e 72 cm serão cortadas em pedaços iguais, do maior tamanho possível, sem sobras. O total de pedaços será:',F(5),[F(24),F(10),F(12),F(6)],'MDC(48, 72) = 24 cm por pedaço. 48 ÷ 24 + 72 ÷ 24 = 2 + 3 = 5 pedaços.')
    assert lcm(4,6,10)==60
    me('MAT-D-03',M5,'MMC','Três luzes piscam juntas e, depois, a cada 4, 6 e 10 segundos, respectivamente. Voltarão a piscar juntas após:',F(60),[F(20),F(120),F(30),F(240)],'MMC(4, 6, 10) = 60 segundos.',fmt=U('s'))
    me('MAT-D-04',M5,'Operações com tempo','Uma audiência durou 2 h 45 min e a seguinte, 1 h 50 min. Juntas, duraram:','4 h 35 min',['3 h 85 min','4 h 15 min','3 h 35 min','4 h 45 min'],'2 h 45 + 1 h 50 = 3 h 95 min = 3 h + 1 h 35 min = 4 h 35 min.')
    S=F(1500)/(F(2,3)*F(3,4)); assert S==3000
    me('MAT-D-05',M5,'Frações','Uma pessoa gastou 1/3 do salário com aluguel e 1/4 do restante com alimentação, sobrando R$ 1.500,00. O salário é:',S,[F(2000),F(2500),F(3600),F(4500)],'Sobra 2/3 após o aluguel, e 3/4 disso após a alimentação: 2/3 × 3/4 = 1/2 do salário = 1.500 → salário R$ 3.000,00.',fmt=R)
    # ---- TABELAS ----
    T={'colunas':['Mês','Processos distribuídos'],'linhas':[['Janeiro',120],['Fevereiro',150],['Março',90],['Abril',140]]}
    assert sum(l[1] for l in T['linhas'])/4==125
    me('MAT-T-01',M6,'Tabela','A tabela mostra os processos distribuídos a uma vara. A média mensal no período foi de:',F(125),[F(120),F(130),F(150),F(500)],'(120 + 150 + 90 + 140) ÷ 4 = 500 ÷ 4 = 125.',tabela={**T,'rotulos':True},tags=['calculo','ja-caiu'])
    me('MAT-T-02',M6,'Tabela','Pela tabela, de fevereiro para março o número de processos distribuídos caiu:',F(40),[F(60),F(375,10),F(25),F(50)],'Queda de 60 sobre o valor de FEVEREIRO (150): 60 ÷ 150 = 40%.',fmt=lambda v:br(v).replace(',50',',5')+'%',tabela={**T,'rotulos':True})
