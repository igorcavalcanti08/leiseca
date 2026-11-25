# Ampliação v2.10 — Raciocínio Lógico (importado por rl.py)
import itertools
def add(q, me, L1, L2, L3, LG, CAT, NEG, EQ, CA, J, R):
    def n(id,enun,gab,alt=None,orig=None,regra=NEG,top='Negação',com=None,tags=None):
        q(id,L1,LG,top,enun,gab,regra,alt=alt,orig=orig,tags=tags or R,com=com)
    n('RL-N-13','A negação de "Se chove, então a rua fica molhada" é "Chove e a rua não fica molhada".','C')
    n('RL-N-14','A negação de "Se chove, então a rua fica molhada" é "Não chove e a rua não fica molhada".','E',alt='"Não chove e a rua não fica molhada"',orig='mantém o antecedente')
    n('RL-N-15','A negação de "Nenhum candidato faltou" é "Todos os candidatos faltaram".','E',alt='"Todos os candidatos faltaram"',orig='~(algum A é B) ≡ nenhum A é B',com='Negação: "Algum candidato faltou" (pelo menos um).')
    n('RL-N-16','A negação de "Pedro estuda ou trabalha" é "Pedro não estuda e não trabalha".','C')
    n('RL-N-17','A negação de "João é alto e Maria é baixa" é "João não é alto ou Maria não é baixa".','C')
    n('RL-N-18','A negação de "Algum juiz é rigoroso" é "Algum juiz não é rigoroso".','E',alt='"Algum juiz não é rigoroso"',orig='~(algum A é B) ≡ nenhum A é B')
    n('RL-N-19','A negação de "Ou Ana viaja ou Bia viaja" é "Ana viaja se, e somente se, Bia viaja".','C')
    n('RL-E-10','"Se é feriado, então o fórum fecha" equivale a "Se o fórum não fecha, então não é feriado".','C',regra=EQ,top='Equivalência')
    n('RL-E-11','"Se é feriado, então o fórum fecha" equivale a "Se não é feriado, então o fórum não fecha".','E',regra=EQ,top='Equivalência',alt='"Se não é feriado, então o fórum não fecha"',orig='a inversa (~p → ~q) NÃO são equivalentes')
    n('RL-E-12','"Se é feriado, então o fórum fecha" equivale a "Não é feriado ou o fórum fecha".','C',regra=EQ,top='Equivalência')
    n('RL-E-13','"Se é feriado, então o fórum fecha" equivale a "É feriado e o fórum fecha".','E',regra=EQ,top='Equivalência',alt='"É feriado e o fórum fecha"',orig='~p ou q')
    n('RL-E-14','"p se, e somente se, q" equivale a "(se p, então q) e (se q, então p)".','C',regra='Bicondicional: p ↔ q ≡ (p → q) e (q → p). É verdadeira quando p e q têm o MESMO valor lógico.',top='Equivalência')
    VL='Tabela-verdade: "p e q" só é V se ambas forem V. "p ou q" só é F se ambas forem F. "p → q" só é F em V → F (antecedente falso ou consequente verdadeiro tornam o condicional V). "p ↔ q" é V quando ambas têm o mesmo valor. "Ou p ou q" é V quando exatamente uma é V. Tautologia: sempre V (p ou ~p). Contradição: sempre F (p e ~p).'
    n('RL-V-01','A conjunção "p e q" só é verdadeira quando p e q são ambas verdadeiras.','C',regra=VL,top='Valor lógico')
    n('RL-V-02','A disjunção "p ou q" é falsa quando apenas uma das proposições é falsa.','E',regra=VL,top='Valor lógico',alt='quando apenas uma das proposições é falsa',orig='"p ou q" só é F se ambas forem F')
    n('RL-V-03','Se p é falsa, a proposição "se p, então q" é verdadeira, qualquer que seja o valor de q.','C',regra=VL,top='Valor lógico')
    n('RL-V-04','Se q é verdadeira, a proposição "se p, então q" é verdadeira, qualquer que seja o valor de p.','C',regra=VL,top='Valor lógico')
    n('RL-V-05','Sendo p verdadeira e q falsa, a bicondicional p ↔ q tem valor lógico verdadeiro.','E',regra=VL,top='Valor lógico',alt='tem valor lógico verdadeiro',orig='"p ↔ q" é V quando ambas têm o mesmo valor')
    n('RL-V-06','A proposição "p ou ~p" é uma tautologia.','C',regra=VL,top='Valor lógico')
    n('RL-V-07','A proposição "p e ~p" é uma tautologia.','E',regra=VL,top='Valor lógico',alt='é uma tautologia',orig='Contradição: sempre F (p e ~p)')
    PRO='Proposição é sentença declarativa que pode ser julgada V ou F. Não são proposições: perguntas, ordens, exclamações e sentenças abertas (com variável, como "x + 3 = 7").'
    n('RL-V-08','"Que horas são?" não é proposição lógica, enquanto "Paulo é escrevente" é.','C',regra=PRO,top='Proposição')
    n('RL-V-09','A sentença "x + 3 = 7" é uma proposição, pois pode ser julgada verdadeira para x = 4.','E',regra=PRO,top='Proposição',alt='é uma proposição',orig='sentenças abertas (com variável')
    def c(id,enun,gab,alt=None,orig=None,regra=CA,top='Categóricas'):
        q(id,L2,CAT,top,enun,gab,regra,alt=alt,orig=orig,tags=R)
    c('RL-C-07','Sendo verdadeiras "Todo A é B" e "Nenhum B é C", conclui-se que nenhum A é C.','C')
    c('RL-C-08','Sendo verdadeiras "Algum A é B" e "Todo B é C", conclui-se que algum A é C.','C')
    c('RL-C-09','De "Todo servidor é concursado" conclui-se que todo concursado é servidor.','E',alt='todo concursado é servidor',orig='não se conclui nada sobre "todo B"')
    ARG='Argumentos válidos: modus ponens (p → q; p; logo q) e modus tollens (p → q; ~q; logo ~p). Falácias: afirmar o consequente (p → q; q; logo p) e negar o antecedente (p → q; ~p; logo ~q).'
    c('RL-C-10','É válido o argumento: "Se estudo, passo. Não passei. Logo, não estudei."','C',regra=ARG,top='Validade')
    c('RL-C-11','É válido o argumento: "Se estudo, passo. Passei. Logo, estudei."','E',alt='É válido',orig='afirmar o consequente',regra=ARG,top='Validade')
    c('RL-C-12','É válido o argumento: "Se estudo, passo. Não estudei. Logo, não passei."','E',alt='É válido',orig='negar o antecedente',regra=ARG,top='Validade')
    # ---- problemas (múltipla escolha) ----
    s=[3];
    while len(s)<6: s.append(2*s[-1]+1)
    me('RL-P-10','Sequências','Na sequência 3, 7, 15, 31, 63, ..., o próximo termo é:',s[5],[126,95,96,129],'Cada termo é o dobro do anterior mais 1: 63 × 2 + 1 = 127.')
    f=[1,1]
    while len(f)<12: f.append(f[-1]+f[-2])
    me('RL-P-11','Sequências','Na sequência 1, 1, 2, 3, 5, 8, 13, ..., cada termo, a partir do terceiro, é a soma dos dois anteriores. O 12º termo é:',f[11],[89,233,121,155],'Continuando: 21, 34, 55, 89, 144 → o 12º termo é 144.')
    ab='ABCDEFGHIJKLMNOPQRSTUVWXYZ'; seq=[0]; st=2
    while len(seq)<6: seq.append(seq[-1]+st); st+=1
    nxt=ab[seq[5]]; assert [ab[i] for i in seq[:5]]==list('ACFJO') and nxt=='U'
    me('RL-P-12','Sequências','No alfabeto de 26 letras, a sequência A, C, F, J, O, ... segue um padrão. A próxima letra é:',nxt,['T','V','S','X'],'Os saltos crescem: +2, +3, +4, +5, e agora +6. O (15ª letra) + 6 = 21ª letra: U.')
    dias=['domingo','segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','sábado']; d=dias[(3+100)%7]; assert d=='sexta-feira'
    me('RL-P-13','Calendário','Se hoje é quarta-feira, daqui a 100 dias será:',d,['quarta-feira','quinta-feira','sábado','domingo'],'A semana se repete a cada 7 dias: 100 = 14 × 7 + 2. Avança 2 dias a partir de quarta: sexta-feira.')
    # verdade/mentira: cada um é sempre-verdadeiro ou sempre-mentiroso
    sols=[]
    for a,b,c_ in itertools.product([True,False],repeat=3):
        A=(not b); B=(not c_); C=((not a) and (not b))
        if A==a and B==b and C==c_: sols.append((a,b,c_))
    assert sols==[(False,True,False)]
    me('RL-P-14','Verdades e mentiras','Cada um de três irmãos ou sempre diz a verdade ou sempre mente. Davi: "Elias mente." Elias: "Fábio mente." Fábio: "Davi e Elias mentem." Quem diz a verdade?','Apenas Elias',['Apenas Davi','Apenas Fábio','Davi e Fábio','Os três'],'Teste Fábio: se ele dissesse a verdade, Davi e Elias mentiriam; mas, com Elias mentindo, a frase de Davi ("Elias mente") seria verdadeira — contradição. Logo, Fábio mente. Então "Fábio mente" é verdade: Elias diz a verdade. E "Elias mente" é falso: Davi mente. Confere: Fábio disse que os dois mentem, o que é falso.')
    # fila
    pess=['Ana','Bia','Caio','Davi','Eva']; ok=[]
    for p in itertools.permutations(pess):
        pos={x:i+1 for i,x in enumerate(p)}
        if pos['Davi']!=1: continue
        if pos['Ana'] in (1,5): continue
        if pos['Bia']!=pos['Caio']+1: continue
        if pos['Eva']!=pos['Ana']-1: continue
        if pos['Caio']<pos['Ana']: continue
        ok.append(p)
    assert len(ok)==1; fila=ok[0]
    me('RL-P-15','Posições','Cinco pessoas estão em fila, nas posições 1 a 5. Davi está na posição 1; Ana não está em nenhuma ponta; Eva está imediatamente antes de Ana; Bia está imediatamente depois de Caio; e Caio está depois de Ana. Quem ocupa a posição 3?',fila[2],[x for x in pess if x!=fila[2]],f'Davi é o 1º. Eva vem logo antes de Ana, e Caio–Bia vêm juntos depois de Ana: Davi, Eva, Ana, Caio, Bia. Posição 3: {fila[2]}.')
    nen=100-(50+40+30-15-10-8+5); assert nen==8
    me('RL-P-16','Conjuntos','Numa pesquisa com 100 pessoas, 50 leem o jornal A, 40 o B e 30 o C; 15 leem A e B, 10 leem A e C, 8 leem B e C, e 5 leem os três. Quantas não leem nenhum dos três?',nen,[5,13,0,23],'Leem algum: 50 + 40 + 30 − 15 − 10 − 8 + 5 = 92. Nenhum: 100 − 92 = 8.',tags=['calculo','ja-caiu'])
    amb=25+20-(40-8); assert amb==13
    me('RL-P-17','Conjuntos','Numa turma de 40 alunos, 25 gostam de futebol, 20 de vôlei e 8 de nenhum dos dois. Quantos gostam dos dois?',amb,[5,12,17,8],'Gostam de pelo menos um: 40 − 8 = 32. Ambos: 25 + 20 − 32 = 13.')
    me('RL-P-18','Princípio da casa dos pombos','Quantas pessoas, no mínimo, devem estar numa sala para garantir que duas façam aniversário no mesmo mês?',13,[12,2,24,7],'Pior caso: 12 pessoas, uma em cada mês. A 13ª repete um mês.')
    me('RL-P-19','Contagem','Oito pessoas se cumprimentam, cada uma apertando a mão de cada outra uma única vez. O total de apertos de mão é:',28,[56,64,16,36],'Cada par se cumprimenta uma vez: 8 × 7 ÷ 2 = 28. (56 conta cada aperto duas vezes.)')
    me('RL-P-20','Contagem','Quantas senhas de 3 algarismos distintos podem ser formadas com os algarismos de 0 a 9?',720,[1000,30,504,120],'10 opções para o 1º, 9 para o 2º e 8 para o 3º: 10 × 9 × 8 = 720.')
    # encadeamento 2
    sol=[]
    for a,b,c_,d_ in itertools.product([True,False],repeat=4):
        if (not a or b) and (not b or not c_) and (c_ or d_) and (not d_):
            sol.append((a,b,c_,d_))
    assert sol==[(False,False,True,False)]
    me('RL-P-21','Encadeamento de condicionais','São verdadeiras: I. Se Gil é analista, Hugo é técnico. II. Se Hugo é técnico, Íris não é juíza. III. Íris é juíza ou Júlia é perita. IV. Júlia não é perita. Logo:','Gil não é analista e Hugo não é técnico.',['Gil é analista e Íris é juíza.','Hugo é técnico ou Júlia é perita.','Íris não é juíza e Gil não é analista.','Hugo é técnico e Íris é juíza.'],'IV: Júlia não é perita. III: então Íris é juíza. II (contrapositiva): Hugo não é técnico. I (contrapositiva): Gil não é analista.',tags=['calculo','ja-caiu'])
