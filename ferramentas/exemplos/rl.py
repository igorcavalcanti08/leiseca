from nl import banco, validar, VU
import itertools
Q, q = banco('Raciocínio Lógico')
L1='Negação e equivalência'; L2='Proposições categóricas e conjuntos'; L3='Problemas lógicos e sequências'
LG='Lógica proposicional'; CAT='Lógica de argumentação'; PB='Problemas lógicos'
J=['ja-caiu']; R=['regra']
NEG='Negações: ~(p → q) ≡ p e ~q (mantém o antecedente, nega o consequente, troca "se...então" por "e"). ~(p e q) ≡ ~p ou ~q. ~(p ou q) ≡ ~p e ~q. ~(todo A é B) ≡ algum A não é B. ~(algum A é B) ≡ nenhum A é B. ~(p ↔ q) ≡ ou p ou q (disjunção exclusiva).'
EQ='Equivalências do condicional: p → q ≡ ~q → ~p (contrapositiva) ≡ ~p ou q. A recíproca (q → p) e a inversa (~p → ~q) NÃO são equivalentes. p ou q ≡ ~p → q. (p → q) e (p → r) ≡ p → (q e r).'
def n(id,enun,gab,alt=None,orig=None,tags=None,origem=None,com=None,regra=NEG,top='Negação'): q(id,L1,LG,top,enun,gab,regra,alt=alt,orig=orig,tags=tags or R,origem=origem,com=com)
n('RL-N-01','A negação de "Se estou correndo ou jogando futebol, então amanhã estarei de férias" é "Estou correndo ou jogando futebol, e amanhã não estarei de férias".','C',tags=J,origem=VU(2025))
n('RL-N-02','A negação de "Se estou correndo ou jogando futebol, então amanhã estarei de férias" é "Se não estou correndo nem jogando futebol, então amanhã não estarei de férias".','E',alt='"Se não estou correndo nem jogando futebol, então amanhã não estarei de férias"',orig='troca "se...então" por "e"',tags=J,origem=VU(2025))
n('RL-N-03','A negação de "Se a questão é fácil, então todos os candidatos acertam" é "A questão é fácil e pelo menos um candidato não acerta".','C',tags=J,origem=VU(2021))
n('RL-N-04','A negação de "Se a questão é fácil, então todos os candidatos acertam" é "A questão é fácil e nenhum candidato acerta".','E',alt='nenhum candidato acerta',orig='~(todo A é B) ≡ algum A não é B',tags=J,origem=VU(2021))
n('RL-N-05','A negação de "Corro todos os dias e, se jogo bola, então não tenho disposição" é "Não corro todos os dias ou jogo bola e tenho disposição".','C',tags=J,origem=VU(2024),com='~[c e (j → ~d)] ≡ ~c ou ~(j → ~d) ≡ ~c ou (j e d).')
n('RL-N-06','A negação de "A isca é boa ou, se a pesca não aconteceu, então não tinha peixe" é "A isca não é boa e a pesca não aconteceu e tinha peixe".','C',tags=J,origem=VU(2024,'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'),com='~[i ou (~p → ~t)] ≡ ~i e ~(~p → ~t) ≡ ~i e (~p e t).')
n('RL-N-07','A negação de "Qualquer processo deve ser considerado ou não há trabalho eficiente neste escritório" é "Algum processo não deve ser considerado e há trabalho eficiente neste escritório".','C',tags=J,origem=VU(2023))
n('RL-N-08','A negação de "Todo servidor é pontual" é "Nenhum servidor é pontual".','E',alt='"Nenhum servidor é pontual"',orig='~(todo A é B) ≡ algum A não é B')
n('RL-N-09','A negação de "Algum processo está atrasado" é "Nenhum processo está atrasado".','C')
n('RL-N-10','A negação de "Choveu e a audiência foi adiada" é "Não choveu e a audiência não foi adiada".','E',alt='"Não choveu e a audiência não foi adiada"',orig='~(p e q) ≡ ~p ou ~q')
n('RL-N-11','A negação de "Ana é escrevente ou Bruno é oficial" é "Ana não é escrevente e Bruno não é oficial".','C')
n('RL-N-12','A negação de "Marcos viaja se, e somente se, recebe as férias" é "Ou Marcos viaja ou recebe as férias".','C')
n('RL-E-01','"Se o esforço é recompensado, então desistir não é a escolha" equivale a "Se desistir é a escolha, então o esforço não é recompensado".','C',regra=EQ,top='Equivalência',tags=J,origem=VU(2024))
n('RL-E-02','"Se o esforço é recompensado, então desistir não é a escolha" equivale a "Se desistir não é a escolha, então o esforço é recompensado".','E',regra=EQ,top='Equivalência',alt='"Se desistir não é a escolha, então o esforço é recompensado"',orig='A recíproca (q → p) e a inversa (~p → ~q) NÃO são equivalentes',tags=J,origem=VU(2024))
n('RL-E-03','"Se o esforço é recompensado, então desistir não é a escolha" equivale a "O esforço não é recompensado ou desistir é a escolha".','E',regra=EQ,top='Equivalência',alt='ou desistir é a escolha',orig='~p ou q',com='~p ou q: "O esforço não é recompensado OU desistir NÃO é a escolha".',tags=J,origem=VU(2024))
n('RL-E-04','"Os garfos têm quatro pontas ou as facas não são afiadas" equivale a "Se as facas são afiadas, então os garfos têm quatro pontas".','C',regra=EQ,top='Equivalência',tags=J,origem=VU(2024,'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'),com='p ou ~f ≡ ~(~f) → p ≡ f → p.')
n('RL-E-05','"Se Alice estuda, então faz uma boa prova, e se Alice estuda, então não fica triste" equivale a "Se Alice estuda, então faz uma boa prova e não fica triste".','C',regra=EQ,top='Equivalência',tags=J,origem=VU(2021))
n('RL-E-06','"Se Alice estuda, então faz uma boa prova e não fica triste" equivale a "Se Alice fica triste e não faz uma boa prova, então ela não estuda".','E',regra=EQ,top='Equivalência',alt='fica triste e não faz uma boa prova',orig='~q → ~p (contrapositiva)',com='A contrapositiva nega "faz boa prova E não fica triste": "Se Alice NÃO faz boa prova OU fica triste, então não estuda".',tags=J,origem=VU(2021))
n('RL-E-07','"Maria está na sala ou Nelson está na sala" equivale a "Se Maria não está na sala, então Nelson está na sala".','C',regra=EQ,top='Equivalência')
n('RL-E-08','Se a proposição p → ~q é falsa, então p e q são ambas verdadeiras.','C',regra='Um condicional só é FALSO quando o antecedente é verdadeiro e o consequente é falso (V → F). p → ~q falso ⇒ p = V e ~q = F, logo q = V.',top='Valor lógico',tags=J,origem=VU(2025))
n('RL-E-09','A proposição "Ou Carla está interessada ou Bianca está interessada" é verdadeira quando ambas estão interessadas.','E',regra='Disjunção exclusiva ("ou... ou...") é verdadeira quando EXATAMENTE UMA das proposições é verdadeira; com as duas verdadeiras (ou as duas falsas), é falsa.',top='Valor lógico',alt='quando ambas estão interessadas',orig='EXATAMENTE UMA')
CA='Categóricas: "Todo A é B" — o conjunto A está dentro de B. "Algum A é B" — há ao menos um elemento comum. "Nenhum A é B" — conjuntos disjuntos. "Não existe A que não seja B" ≡ "Todo A é B". De "Todo A é B" e "Algum A é C" conclui-se "Algum C é B"; mas não se conclui nada sobre "todo B" nem sobre quem está fora de A.'
def c(id,enun,gab,alt=None,orig=None,tags=None,origem=None,com=None): q(id,L2,CAT,'Categóricas',enun,gab,CA,alt=alt,orig=orig,tags=tags or R,origem=origem,com=com)
c('RL-C-01','Sendo verdadeiras "Todo jogador é esportista" e "Algum jogador é jogador de futebol", conclui-se que algum jogador de futebol é esportista.','C',tags=J,origem=VU(2024))
c('RL-C-02','Sendo verdadeiras "Todo jogador é esportista" e "Algum jogador é jogador de futebol", conclui-se que todo esportista é jogador de futebol.','E',alt='todo esportista é jogador de futebol',orig='não se conclui nada sobre "todo B"',tags=J,origem=VU(2024))
c('RL-C-03','"Não existe mecânico que não goste de carro" equivale a "Todo mecânico gosta de carro".','C',tags=J,origem=VU(2021))
c('RL-C-04','Sendo verdadeiras "Todo mecânico gosta de carro" e "Alguns funileiros gostam de carro", conclui-se que alguns funileiros são mecânicos.','E',alt='conclui-se que alguns funileiros são mecânicos',orig='não se conclui nada sobre "todo B" nem sobre quem está fora de A',tags=J,origem=VU(2021))
c('RL-C-05','Sendo verdadeira "Todo mecânico gosta de carro", conclui-se que, se Carlos não gosta de carro, então Carlos não é mecânico.','C',tags=J,origem=VU(2021))
c('RL-C-06','Sendo verdadeiras "Todo praticante de B pratica A" e "Alguns praticantes de C praticam B", conclui-se que alguns praticantes de C praticam A.','C',tags=J,origem=VU(2023))

# ---------------- PROBLEMAS (múltipla escolha) ----------------
def me(id,top,enun,correta,erradas,resol,tags=None,origem=None):
    ks='ABCDE'; vals=[correta]+erradas; import random; rnd=random.Random(id); rnd.shuffle(vals)
    alts={ks[i]:str(v) for i,v in enumerate(vals)}; gab=[k for k,v in alts.items() if v==str(correta)][0]
    q(id,L3,PB,top,enun,gab,resol,alts=alts,tags=tags or ['calculo'],origem=origem)
# sequência de dígitos
A=[2+3*i for i in range(200)]; dig=''.join(str(x) for x in A); t100=int(dig[99])
me('RL-P-01','Sequências','A sequência (2, 5, 8, 11, 14, ...) cresce de 3 em 3. Escrevendo seus termos lado a lado e separando os algarismos, forma-se a sequência (2, 5, 8, 1, 1, 1, 4, 1, 7, ...). O 100º termo dessa nova sequência é:',t100,[x for x in [0,1,4,7,9,3] if x!=t100][:4],
   f'Termos de 1 algarismo: 2, 5, 8 → 3 algarismos. Termos de 2 algarismos: de 11 a 98 (30 termos) → 60 algarismos; acumulado 63. Faltam 37 algarismos, nos termos de 3 algarismos (101, 104, ...): 37 = 12×3 + 1 → 12 termos completos (101 a 134) e o 1º algarismo do 13º (137). O 100º termo é {t100}.',tags=['calculo','ja-caiu'],origem=VU(2025))
seq=[];x=100
for i in range(40):
    seq.append(x); x+= [5,3,-9][i%3]
me('RL-P-02','Sequências','Na sequência 100, 105, 108, 99, 104, 107, 98, ..., o padrão se repete. O 30º termo é:',seq[29],[seq[29]+1,seq[29]-1,seq[28],seq[29]+9],
   f'Padrão +5, +3, −9: a cada 3 termos, o valor cai 1 (100, 99, 98...). O 30º termo é o 3º do 10º bloco; o 1º termo do 10º bloco é 100 − 9 = 91, e o 3º é 91 + 5 + 3 = {seq[29]}.',tags=['calculo','ja-caiu'],origem=VU(2025))
s2=[ (k*k if i%2==0 else k*k+2) for k in range(1,30) for i in range(2)]
me('RL-P-03','Sequências','A sequência 1, 3, 4, 6, 9, 11, 16, 18, 25, 27, ... segue um padrão lógico. O 20º termo é:',s2[19],[100,121,104,83],
   f'Termos ímpares: quadrados perfeitos (1, 4, 9, 16...). Termos pares: o quadrado anterior + 2. O 20º termo é par, ligado ao 10º quadrado: 10² + 2 = {s2[19]}.',tags=['calculo'])
bloco='ABCDCB'; l100=bloco[99%6]
me('RL-P-04','Sequências','A sequência de letras A B C D C B A B C D C B A ... repete sempre o mesmo bloco. A 100ª letra é:',l100,[x for x in 'ABCDE' if x!=l100][:4],
   f'O bloco "ABCDCB" tem 6 letras. 100 = 16×6 + 4 → a 100ª letra é a 4ª do bloco: {l100}.',tags=['calculo'])
# verdade e mentira: exatamente um fala a verdade
falas={'Ana':lambda c:c=='Bia','Bia':lambda c:c=='Davi','Caio':lambda c:c!='Caio','Davi':lambda c:c!='Davi'}
sol=[c for c in falas if sum(f(c) for f in falas.values())==1]; assert len(sol)==1; cul=sol[0]
me('RL-P-05','Verdades e mentiras','Um dos quatro amigos quebrou o vaso. Ana: "Foi a Bia." Bia: "Foi o Davi." Caio: "Não fui eu." Davi: "Não fui eu." Sabendo que apenas um deles diz a verdade, quem quebrou o vaso?',cul,[x for x in ['Ana','Bia','Caio','Davi','Ninguém'] if x!=cul],
   f'Teste cada culpado e conte as verdades. Se fosse Ana, Bia ou Davi, Caio diria a verdade junto com ao menos mais um. Só com {cul} como culpado há exatamente uma verdade (a de Davi: "Não fui eu").',tags=['calculo','ja-caiu'],origem=VU(2025))
# encadeamento
me('RL-P-06','Encadeamento de condicionais','São verdadeiras: I. Se Paulo não é juiz, Rita é promotora. II. Se Rita é promotora, Caio não é perito. III. Caio é perito ou Dora é escrevente. IV. Ou Dora é escrevente ou Elisa é oficial. V. Se Fábio é diretor, Elisa não é oficial. VI. Elisa é oficial. Logo, é verdade que:','Paulo é juiz e Fábio não é diretor.',['Dora é escrevente e Rita é promotora.','Caio não é perito e Paulo é juiz.','Rita é promotora ou Fábio é diretor.','Paulo não é juiz e Dora não é escrevente.'],
   'Comece pelo fato (VI): Elisa é oficial. V: logo Fábio não é diretor. IV ("ou... ou..."): Dora não é escrevente. III: então Caio é perito. II (contrapositiva): Rita não é promotora. I (contrapositiva): Paulo é juiz.',tags=['calculo','ja-caiu'],origem=VU(2024))
# casa dos pombos
me('RL-P-07','Princípio da casa dos pombos','Uma gaveta tem 8 camisetas pretas, 10 azuis e 6 brancas. Retirando no escuro, qual o menor número de camisetas que garante ao menos uma preta e uma azul?',17,[15,19,12,24],
   'Pior caso: tirar todas as azuis (10) e todas as brancas (6) sem nenhuma preta = 16. A próxima é obrigatoriamente preta: 17. (O outro pior caso, 8 pretas + 6 brancas + 1, dá 15, que é menor; vale o maior.)',tags=['calculo','ja-caiu'],origem=VU(2021))
# conjuntos
me('RL-P-08','Conjuntos','Em um grupo de 60 servidores, todos fazem o curso A ou o curso B. Dez fazem os dois cursos. Entre os que fazem apenas um curso, a razão entre os que fazem só A e os que fazem só B é 2/3. Quantos servidores fazem o curso A?',30,[20,40,10,36],
   'Só um curso: 60 − 10 = 50. Só A : só B = 2 : 3 → só A = 20 e só B = 30. Curso A = só A + ambos = 20 + 10 = 30.',tags=['calculo','ja-caiu'],origem=VU(2025))
# associação
nomes=['Ana','Bia','Carla']; disc=['espanhol','francês','inglês']; bairros=['Perdizes','Moema','Tatuapé']
sols=[]
for dp in itertools.permutations(disc):
    for bp in itertools.permutations(bairros):
        D=dict(zip(nomes,dp)); B=dict(zip(nomes,bp))
        if B['Ana']!='Perdizes': continue
        if B[[n_ for n_ in nomes if D[n_]=='francês'][0]]!='Tatuapé': continue
        if D['Bia']!='inglês': continue
        sols.append((D,B))
assert len(sols)==1; D,B=sols[0]
me('RL-P-09','Associação','Ana, Bia e Carla ensinam espanhol, francês e inglês e moram em Perdizes, Moema e Tatuapé, uma em cada. Ana mora em Perdizes, a professora de francês mora no Tatuapé e Bia ensina inglês. Logo:',f'Carla ensina francês e Bia mora em Moema.',['Ana ensina francês e Carla mora em Moema.','Bia mora no Tatuapé e Carla ensina espanhol.','Carla mora em Perdizes e Ana ensina inglês.','Ana ensina espanhol e Bia mora no Tatuapé.'],
   'Ana mora em Perdizes, então não ensina francês (que é de quem mora no Tatuapé) nem inglês (é da Bia): Ana ensina espanhol. Sobra francês para Carla, que mora no Tatuapé; Bia mora em Moema.',tags=['calculo','ja-caiu'],origem=VU(2024))
assert D['Carla']=='francês' and B['Bia']=='Moema'
from rl2 import add
add(q, me, L1, L2, L3, LG, CAT, NEG, EQ, CA, J, R)
if __name__=='__main__':
    import json,collections
    e=validar(Q); print(len(Q),e,collections.Counter(x['grupo'] for x in Q))
    json.dump(Q,open('rl.json','w'),ensure_ascii=False,indent=1)
    for o in Q:
        if o['tipo']=='ME': print(o['id'],o['gabarito'],o['alternativas'][o['gabarito']])
