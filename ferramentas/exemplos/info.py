from nl import banco, validar, VU
Q, q = banco('Informática')
EX = 'Microsoft Excel (365)'; WD = 'Microsoft Word (365)'; WIN = 'Windows 10/11'; EM = 'Correio eletrônico'; NET = 'Internet e navegadores'; TM = 'Microsoft Teams'; OD = 'OneDrive'
G1 = 'Excel: fórmulas e funções'; G2 = 'Word: formatação e recursos'; G3 = 'Windows: atalhos, arquivos e área de transferência'; G4 = 'E-mail e Internet'; G5 = 'Teams e OneDrive'
R = ['regra']; JC = ['ja-caiu']

# ---------------- EXCEL (C/E) ----------------
X_SEP = 'No Excel em português, os argumentos de uma função são separados por ponto e vírgula (;) e o intervalo é indicado por dois-pontos (:). SOMA(B1;C3) soma só as duas células; SOMA(B1:C3) soma todo o retângulo de B1 a C3.'
q('INF-X-01', G1, EX, 'Separadores', 'No Excel em português, =SOMA(B1;C3) soma todas as células do intervalo de B1 até C3.', 'E', X_SEP, alt='soma todas as células do intervalo de B1 até C3', orig='SOMA(B1;C3) soma só as duas células', tags=JC, origem=VU(2024))
q('INF-X-02', G1, EX, 'Separadores', 'No Excel em português, a fórmula =SOMA(B1:C3) soma as seis células do retângulo formado pelas colunas B e C e pelas linhas 1 a 3.', 'C', X_SEP, tags=R)
X_CONC = 'CONCATENAR (ou CONCAT) junta os textos exatamente como estão, sem inserir espaço ou separador. Para separar, o separador deve ser um argumento entre aspas: =CONCATENAR(B2;"-";C2). O operador & faz o mesmo: =B2&"-"&C2.'
q('INF-X-03', G1, EX, 'CONCATENAR', 'Se A1 contém "casa", A2 contém "de" e A3 contém "barro", a fórmula =CONCATENAR(A1;A2;A3) resulta em "casa de barro".', 'E', X_CONC, alt='resulta em "casa de barro"', orig='sem inserir espaço ou separador', com='Resultado: "casadebarro".', tags=JC, origem=VU(2024))
q('INF-X-04', G1, EX, 'CONCATENAR', 'Para juntar B2 e C2 separados por hífen, pode-se usar =CONCATENAR(B2;"-";C2).', 'C', X_CONC, tags=JC, origem=VU(2021))
q('INF-X-05', G1, EX, 'CONCATENAR', 'A fórmula =B2&" "&C2 junta o conteúdo de B2 e C2 com um espaço entre eles.', 'C', X_CONC, tags=R)
X_MAI = 'MAIÚSCULA(texto) converte tudo para maiúsculas; MINÚSCULA(texto) converte tudo para minúsculas; PRI.MAIÚSCULA(texto) põe só a primeira letra de cada palavra em maiúscula.'
q('INF-X-06', G1, EX, 'Funções de texto', 'Se B2 contém "abC", a fórmula =MAIÚSCULA(B2) resulta em "ABC".', 'C', X_MAI, tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
q('INF-X-07', G1, EX, 'Funções de texto', 'A função PRI.MAIÚSCULA converte todo o texto para letras maiúsculas.', 'E', X_MAI, alt='converte todo o texto para letras maiúsculas', orig='põe só a primeira letra de cada palavra em maiúscula', tags=R)
X_SE = 'SE(teste; valor_se_verdadeiro; valor_se_falso). E(...) só é VERDADEIRO se TODOS os testes forem verdadeiros; OU(...) é VERDADEIRO se PELO MENOS UM for verdadeiro.'
q('INF-X-08', G1, EX, 'SE, E, OU', 'A função E(teste1;teste2) retorna VERDADEIRO quando pelo menos um dos testes é verdadeiro.', 'E', X_SE, alt='quando pelo menos um dos testes é verdadeiro', orig='só é VERDADEIRO se TODOS os testes forem verdadeiros', tags=R)
q('INF-X-09', G1, EX, 'SE, E, OU', 'Na função SE, o segundo argumento é o valor retornado quando o teste lógico é verdadeiro.', 'C', X_SE, tags=R)
X_MM = 'MAIOR(intervalo; k) retorna o k-ésimo MAIOR valor; MENOR(intervalo; k) retorna o k-ésimo MENOR. MÁXIMO e MÍNIMO retornam o maior e o menor de todos.'
q('INF-X-10', G1, EX, 'MAIOR e MENOR', 'A fórmula =MAIOR(A1:C3;2) retorna o segundo maior valor do intervalo A1:C3.', 'C', X_MM, tags=JC, origem=VU(2025))
q('INF-X-11', G1, EX, 'MAIOR e MENOR', 'A fórmula =MENOR(A1:A10;3) retorna a soma dos três menores valores de A1:A10.', 'E', X_MM, alt='a soma dos três menores valores', orig='retorna o k-ésimo MENOR', tags=R)
X_PROCV = 'PROCV(valor_procurado; matriz_tabela; núm_índice_coluna; [procurar_intervalo]). O valor procurado vem PRIMEIRO; a busca é feita na 1ª coluna da matriz. Omitido o 4º argumento, o Excel faz correspondência aproximada (VERDADEIRO); para correspondência exata, usa-se FALSO (ou 0). Para arrastar a fórmula para baixo sem deslocar a tabela, fixam-se as linhas da matriz com $ (ex.: A$2:B$4 ou $A$2:$B$4).'
q('INF-X-12', G1, EX, 'PROCV', 'Na função PROCV, o primeiro argumento é a matriz onde será feita a busca e o segundo é o valor procurado.', 'E', X_PROCV, alt='o primeiro argumento é a matriz onde será feita a busca e o segundo é o valor procurado', orig='O valor procurado vem PRIMEIRO', tags=JC, origem=VU(2025))
q('INF-X-13', G1, EX, 'PROCV', 'Para arrastar para baixo uma fórmula com PROCV sem que a matriz de busca se desloque, as linhas da matriz devem ser fixadas com o símbolo $, como em A$2:B$4.', 'C', X_PROCV, tags=JC, origem=VU(2025))
q('INF-X-14', G1, EX, 'PROCV', 'Omitido o quarto argumento da PROCV, o Excel faz, por padrão, correspondência exata.', 'E', X_PROCV, alt='correspondência exata', orig='Omitido o 4º argumento, o Excel faz correspondência aproximada', tags=R)
X_REF = 'Ao copiar ou arrastar uma fórmula, as referências RELATIVAS se ajustam ao deslocamento; o $ fixa a coluna ($A1), a linha (A$1) ou ambas ($A$1).'
q('INF-X-15', G1, EX, 'Referências', 'Se C1 contém =A1*$B$1 e essa fórmula é copiada para C2, o resultado em C2 será =A2*$B$1.', 'C', X_REF, tags=R)
q('INF-X-16', G1, EX, 'Referências', 'Na referência A$1, o símbolo $ fixa a coluna A, que não muda quando a fórmula é copiada para outras colunas.', 'E', X_REF, alt='fixa a coluna A, que não muda quando a fórmula é copiada para outras colunas', orig='a linha (A$1)', tags=R)
X_AREA = 'Guia Layout da Página > botão Área de Impressão: Definir Área de Impressão e Limpar Área de Impressão.'
q('INF-X-17', G1, EX, 'Layout da Página', 'No Excel, o botão Área de Impressão, da guia Layout da Página, oferece as opções Definir Área de Impressão e Limpar Área de Impressão.', 'C', X_AREA, tags=JC, origem=VU(2023))
X_GUIA = 'Clique com o botão direito na guia (aba) da planilha: Inserir, Excluir, Renomear, Mover ou Copiar, Exibir Código, Proteger Planilha, Cor da Guia, Ocultar/Reexibir, Selecionar Todas as Planilhas.'
q('INF-X-18', G1, EX, 'Planilhas', 'Clicando com o botão direito sobre o nome (guia) de uma planilha, é possível alterar a cor da guia.', 'C', X_GUIA, tags=JC, origem=VU(2021))
q('INF-X-19', G1, EX, 'Planilhas', 'Clicando com o botão direito sobre a guia de uma planilha, há a opção de enviá-la por e-mail diretamente a outro usuário.', 'E', X_GUIA, alt='enviá-la por e-mail diretamente a outro usuário', orig='Mover ou Copiar', tags=R)
X_INS = 'Página Inicial > Células > Inserir > Inserir Colunas na Planilha: a nova coluna entra À ESQUERDA da coluna selecionada, e as colunas à direita se deslocam (C vira D, D vira E...).'
q('INF-X-20', G1, EX, 'Inserir colunas', 'Com uma célula da coluna C selecionada, o comando Inserir Colunas na Planilha cria uma coluna nova à direita de C.', 'E', X_INS, alt='à direita de C', orig='À ESQUERDA da coluna selecionada', tags=JC, origem=VU(2021))
X_ERR = '#DIV/0! = divisão por zero; #NOME? = nome de função ou intervalo não reconhecido; #REF! = referência inválida (célula excluída); #VALOR! = tipo de argumento errado; #N/D = valor não disponível (ex.: PROCV não achou).'
q('INF-X-21', G1, EX, 'Erros', 'O erro #NOME? aparece quando a fórmula contém um nome de função que o Excel não reconhece, como =SOMAA(A1:A3).', 'C', X_ERR, tags=R)
q('INF-X-22', G1, EX, 'Erros', 'Quando a PROCV não encontra o valor procurado em correspondência exata, retorna o erro #DIV/0!.', 'E', X_ERR, alt='#DIV/0!', orig='#N/D = valor não disponível (ex.: PROCV não achou)', tags=R)
X_SS = 'SOMASE(intervalo; critério; [intervalo_soma]) soma o intervalo_soma onde o intervalo atende ao critério. CONT.SE(intervalo; critério) conta as células que atendem ao critério. Critérios com operador vão entre aspas: ">5".'
q('INF-X-23', G1, EX, 'SOMASE e CONT.SE', 'A função CONT.SE(A1:A10;">5") soma os valores de A1:A10 maiores que 5.', 'E', X_SS, alt='soma os valores', orig='conta as células que atendem ao critério', tags=R)
q('INF-X-24', G1, EX, 'SOMASE e CONT.SE', 'Em =SOMASE(A1:A5;"X";B1:B5), são somados os valores de B1:B5 cujas células correspondentes em A1:A5 contêm "X".', 'C', X_SS, tags=R)
X_ALCA = 'Alça de preenchimento: arrastar uma célula com um único número COPIA o número (com Ctrl, cria série); arrastar "Janeiro", "seg" ou datas cria a sequência; arrastar uma fórmula ajusta as referências relativas.'
q('INF-X-25', G1, EX, 'Alça de preenchimento', 'Arrastando pela alça de preenchimento uma célula que contém a palavra Janeiro, o Excel preenche as células seguintes com Fevereiro, Março etc.', 'C', X_ALCA, tags=R)

# ---------------- EXCEL (múltipla escolha com tabela) ----------------
T = {'colunas': ['', 'A', 'B', 'C'], 'linhas': [[1, 4, 7, 2], [2, 9, 1, 6], [3, 3, 8, 5]]}
v = {(r, c): T['linhas'][r - 1][' ABC'.index(c)] for r in (1, 2, 3) for c in 'ABC'}
tudo = sorted(v.values())
r1 = v[3,'C'] + v[2,'C'] if not (v[1,'A'] > v[2,'A'] and v[1,'B'] > v[2,'B']) else v[1,'C'] + v[2,'C']
assert r1 == 11
q('INF-XT-01', G1, EX, 'SE com E', 'Considere a planilha. Qual é o resultado de =SE(E(A1>A2;B1>B2);C1+C2;C3+C2)?', 'B',
  'A1>A2 é falso (4>9) — basta um falso para E(...) ser FALSO. Logo, a SE devolve o 3º argumento: C3+C2 = 5+6 = 11.', alts={'A': '8', 'B': '11', 'C': '13', 'D': '7', 'E': '15'}, tabela=T, tags=JC, origem=VU(2023))
r2 = (v[1,'A'] + v[3,'C']) if (v[1,'A'] > v[2,'A'] or v[1,'B'] > v[2,'B']) else sum(tudo)
assert r2 == 9
q('INF-XT-02', G1, EX, 'SE com OU', 'Considere a planilha. Qual é o resultado de =SE(OU(A1>A2;B1>B2);SOMA(A1;C3);SOMA(A1:C3))?', 'A',
  'OU(...) é VERDADEIRO porque B1>B2 (7>1). Então vale SOMA(A1;C3) — com ponto e vírgula, só as duas células: 4+5 = 9. (SOMA(A1:C3) seria 45.)', alts={'A': '9', 'B': '45', 'C': '17', 'D': '20', 'E': '11'}, tabela=T, tags=JC, origem=VU(2024))
r3 = tudo[-2] + tudo[2]
assert r3 == 11
q('INF-XT-03', G1, EX, 'MAIOR e MENOR', 'Considere a planilha. Qual é o resultado de =MAIOR(A1:C3;2)+MENOR(A1:C3;3)?', 'D',
  'Valores em ordem: 1, 2, 3, 4, 5, 6, 7, 8, 9. Segundo maior = 8; terceiro menor = 3. 8 + 3 = 11.', alts={'A': '12', 'B': '10', 'C': '17', 'D': '11', 'E': '9'}, tabela=T, tags=JC, origem=VU(2025))
r4 = sum(1 for x in tudo if x > 5)
assert r4 == 4
q('INF-XT-04', G1, EX, 'CONT.SE', 'Considere a planilha. Qual é o resultado de =CONT.SE(A1:C3;">5")?', 'C',
  'CONT.SE conta as células: 9, 7, 8 e 6 são maiores que 5 → 4 células. (A soma delas, 30, seria o resultado de SOMASE.)', alts={'A': '30', 'B': '5', 'C': '4', 'D': '3', 'E': '6'}, tabela=T, tags=R)
r5 = v[2,'A'] + max(v[1,'B'], v[2,'B'], v[3,'B'])
q('INF-XT-05', G1, EX, 'SE com MAIOR', 'Considere a planilha. Qual é o resultado de =SE(MAIOR(A1:C3;1)>8;MÍNIMO(A1:C1);MÁXIMO(A1:C1))?', 'E',
  'MAIOR(A1:C3;1) = 9, e 9>8 é verdadeiro → MÍNIMO(A1:C1) = menor entre 4, 7 e 2 = 2.', alts={'A': '7', 'B': '9', 'C': '4', 'D': '1', 'E': '2'}, tabela=T, tags=R)
T2 = {'colunas': ['', 'A', 'B'], 'linhas': [[1, 'Cível', 120], [2, 'Criminal', 80], [3, 'Cível', 60], [4, 'Família', 40], [5, 'Criminal', 30]]}
r6 = sum(l[2] for l in T2['linhas'] if l[1] == 'Criminal'); assert r6 == 110
q('INF-XT-06', G1, EX, 'SOMASE', 'A planilha registra processos por área (coluna A) e quantidade (coluna B). Qual é o resultado de =SOMASE(A1:A5;"Criminal";B1:B5)?', 'B',
  'Soma B onde A = "Criminal": 80 (linha 2) + 30 (linha 5) = 110. CONT.SE(A1:A5;"Criminal") daria 2.', alts={'A': '2', 'B': '110', 'C': '180', 'D': '80', 'E': '330'}, tabela=T2, tags=R)
T3 = {'colunas': ['', 'A', 'B'], 'linhas': [[1, 'tj', 'sp'], [2, 'Fórum', 'Santos']]}
q('INF-XT-07', G1, EX, 'Funções de texto', 'Considere a planilha. Qual é o resultado de =CONCATENAR(MAIÚSCULA(A1);"-";B1)?', 'A',
  'MAIÚSCULA(A1) = "TJ"; B1 continua "sp" (nada o altera). CONCATENAR junta tudo: "TJ-sp".', alts={'A': 'TJ-sp', 'B': 'TJ-SP', 'C': 'TJ sp', 'D': 'tj-sp', 'E': 'TJsp'}, tabela=T3, tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
q('INF-XT-08', G1, EX, 'Referências', 'A célula C1 contém =A1*$B$1. Se essa célula for copiada e colada em D2, a fórmula em D2 será:', 'D',
  'Deslocou 1 coluna e 1 linha: A1 (relativa) vira B2; $B$1 (absoluta) não muda. Resultado: =B2*$B$1.', alts={'A': '=A2*$B$1', 'B': '=B2*$C$2', 'C': '=A1*$B$1', 'D': '=B2*$B$1', 'E': '=B1*$B$2'}, tags=R)

# ---------------- WORD ----------------
W_TOG = 'Negrito, itálico e sublinhado funcionam como liga/desliga: acionados sem texto selecionado, valem para o que for digitado em seguida até serem desligados. Com o cursor dentro de uma palavra (sem seleção), a formatação de caractere é aplicada à PALAVRA INTEIRA.'
q('INF-W-01', G2, WD, 'Formatação', 'No Word, com o cursor posicionado no meio de uma palavra, sem nada selecionado, ao acionar o itálico a formatação é aplicada à palavra inteira.', 'C', W_TOG, tags=JC, origem=VU(2023))
q('INF-W-02', G2, WD, 'Formatação', 'No Word, acionar o negrito sem texto selecionado não tem efeito sobre o que for digitado em seguida.', 'E', W_TOG, alt='não tem efeito sobre o que for digitado em seguida', orig='valem para o que for digitado em seguida até serem desligados', tags=JC, origem=VU(2025))
W_UNDO = 'Ctrl+Z desfaz apenas a ÚLTIMA ação; repetindo, desfaz as anteriores, uma a uma. Ctrl+Y refaz.'
q('INF-W-03', G2, WD, 'Desfazer', 'Uma palavra recebeu sublinhado e, em seguida, o efeito tachado. Pressionando Ctrl+Z uma vez, a palavra fica sem o tachado, mas continua sublinhada.', 'C', W_UNDO, tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
W_EF = 'Sobrescrito: letras pequenas ACIMA da linha (ex.: m²) — Ctrl+Shift+=. Subscrito: letras pequenas ABAIXO da linha (ex.: H₂O) — Ctrl+=. Versalete: minúsculas viram maiúsculas pequenas. Tachado: linha no meio do texto.'
q('INF-W-04', G2, WD, 'Efeitos de fonte', 'No Word, o efeito que deixa o texto com letras pequenas acima da linha, como em m², é o subscrito.', 'E', W_EF, alt='é o subscrito', orig='Sobrescrito: letras pequenas ACIMA da linha', tags=JC, origem=VU(2021))
q('INF-W-05', G2, WD, 'Efeitos de fonte', 'O efeito Versalete exibe as letras minúsculas como maiúsculas de tamanho reduzido.', 'C', W_EF, tags=R)
W_AT = 'Atalhos do Word em português: Ctrl+N negrito; Ctrl+I itálico; Ctrl+S sublinhado; Ctrl+B salvar; Ctrl+E centralizar; Ctrl+J justificar; Ctrl+G alinhar à direita; Ctrl+Q alinhar à esquerda; Ctrl+Enter quebra de página; Ctrl+P imprimir.'
q('INF-W-06', G2, WD, 'Atalhos', 'No Word em português, Ctrl+S aplica sublinhado ao texto selecionado.', 'C', W_AT, tags=R)
q('INF-W-07', G2, WD, 'Atalhos', 'No Word em português, o atalho Ctrl+B aplica negrito ao texto selecionado.', 'E', W_AT, alt='aplica negrito ao texto selecionado', orig='Ctrl+B salvar', com='Negrito é Ctrl+N.', tags=R)
q('INF-W-08', G2, WD, 'Atalhos', 'No Word, Ctrl+Enter insere uma quebra de página.', 'C', W_AT, tags=R)
W_NUM = 'Para mudar o número inicial de uma lista numerada: clicar com o botão DIREITO (secundário) sobre um número da lista > Definir valor de numeração... e digitar o valor (ex.: 20). No mesmo menu: Reiniciar em 1 e Continuar numeração.'
q('INF-W-09', G2, WD, 'Lista numerada', 'Para que uma lista numerada de 1 a 5 passe a começar em 20, pode-se clicar com o botão direito sobre um número da lista e escolher Definir valor de numeração.', 'C', W_NUM, tags=JC, origem=VU(2025))
q('INF-W-10', G2, WD, 'Lista numerada', 'O menu que permite definir o valor inicial de uma lista numerada é aberto com o clique do botão primário (esquerdo) do mouse sobre o número da lista.', 'E', W_NUM, alt='botão primário (esquerdo)', orig='botão DIREITO (secundário)', tags=JC, origem=VU(2025))
W_SEN = 'Senha para abrir: Arquivo > Informações > Proteger Documento > Criptografar com Senha. (Também em Salvar Como > Ferramentas > Opções Gerais.)'
q('INF-W-11', G2, WD, 'Proteção', 'Para exigir senha na abertura de um documento, usa-se Arquivo > Informações > Proteger Documento > Criptografar com Senha.', 'C', W_SEN, tags=JC, origem=VU(2024))
W_FOR = 'Formas sobrepostas: Avançar move a forma UMA camada para a frente; Trazer para a Frente a coloca à frente de TODAS. Recuar / Enviar para Trás funcionam ao contrário.'
q('INF-W-12', G2, WD, 'Formas', 'No Word, o comando Avançar coloca a forma selecionada à frente de todas as demais formas.', 'E', W_FOR, alt='à frente de todas as demais formas', orig='Avançar move a forma UMA camada para a frente', tags=JC, origem=VU(2024))
W_SA = 'Categorias de SmartArt: Lista, Processo, Ciclo, Hierarquia, Relação, Matriz, Pirâmide e Imagem.'
q('INF-W-13', G2, WD, 'SmartArt', 'Processo e Hierarquia são categorias de elementos gráficos SmartArt do Word.', 'C', W_SA, tags=JC, origem=VU(2023))
q('INF-W-14', G2, WD, 'SmartArt', 'Tabela e Vetor estão entre as categorias de SmartArt do Word.', 'E', W_SA, alt='Tabela e Vetor', orig='Lista, Processo, Ciclo, Hierarquia, Relação, Matriz, Pirâmide e Imagem', tags=R)
W_IMP = 'Arquivo > Imprimir > Impressão Personalizada: imprime só as páginas digitadas (ex.: 1,3,5-8).'
q('INF-W-15', G2, WD, 'Impressão', 'A opção Impressão Personalizada, em Arquivo > Imprimir, permite imprimir apenas páginas específicas, como 2,5-7.', 'C', W_IMP, tags=JC, origem=VU(2021))
W_CX = 'Caixa de Texto (Inserir > Texto > Caixa de Texto): selecionada, pode ser movida, redimensionada e girada pela alça de rotação; recebe preenchimento, contorno e efeitos.'
q('INF-W-16', G2, WD, 'Caixa de texto', 'Uma caixa de texto inserida no Word pode ser girada no sentido horário ou anti-horário.', 'C', W_CX, tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))

# ---------------- WINDOWS ----------------
WT = 'Atalhos com a tecla Windows: Win+Tab Visão de Tarefas (janelas e áreas de trabalho virtuais); Win+D mostra/oculta a área de trabalho; Win+E Explorador de Arquivos; Win+L bloqueia; Win+I Configurações; Win+V histórico da área de transferência; Win+Shift+S captura de tela; Win+. emojis; Win+Z layouts de ajuste (Windows 11).'
q('INF-S-01', G3, WIN, 'Atalhos', 'No Windows 11, o atalho Windows + Tab abre a Visão de Tarefas.', 'C', WT, tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
q('INF-S-02', G3, WIN, 'Atalhos', 'No Windows, o atalho Windows + E bloqueia o computador.', 'E', WT, alt='bloqueia o computador', orig='Win+E Explorador de Arquivos', tags=R)
q('INF-S-03', G3, WIN, 'Atalhos', 'No Windows 10 e 11, Windows + V abre o histórico da área de transferência, quando ativado.', 'C', WT, tags=R)
q('INF-S-04', G3, WIN, 'Atalhos', 'No Windows, Windows + D abre as Configurações do sistema.', 'E', WT, alt='abre as Configurações do sistema', orig='Win+D mostra/oculta a área de trabalho', tags=R)
WAT = 'Histórico da área de transferência do Windows (Configurações > Sistema > Área de Transferência): ativável; guarda até 25 itens; o histórico é apagado a cada reinicialização e ao clicar em Limpar tudo, EXCETO os itens FIXADOS; há opção de sincronizar entre dispositivos. A Área de Transferência do Office guarda até 24 itens.'
q('INF-S-05', G3, WIN, 'Área de transferência', 'Fixar um item no histórico da área de transferência do Windows impede que ele seja apagado ao limpar o histórico.', 'C', WAT, tags=JC, origem=VU(2024))
q('INF-S-06', G3, WIN, 'Área de transferência', 'No Windows 11, existem duas áreas de transferência separadas: uma para textos e outra para imagens.', 'E', WAT, alt='duas áreas de transferência separadas: uma para textos e outra para imagens', orig='guarda até 25 itens', tags=JC, origem=VU(2024))
q('INF-S-07', G3, WIN, 'Área de transferência', 'A Área de Transferência do Microsoft Office armazena até 24 itens copiados.', 'C', WAT, tags=JC, origem=VU(2021))
q('INF-S-08', G3, WIN, 'Área de transferência', 'Em Configurações > Sistema > Área de Transferência, é possível ativar a sincronização do histórico entre dispositivos.', 'C', WAT, tags=JC, origem=VU(2023))
WTV = 'Áreas de trabalho virtuais: Visão de Tarefas (Win+Tab ou botão na barra de tarefas) > Nova área de trabalho. Atalho direto: Win+Ctrl+D cria; Win+Ctrl+setas alternam.'
q('INF-S-09', G3, WIN, 'Áreas de trabalho', 'Para criar uma nova área de trabalho virtual no Windows 10, pode-se abrir a Visão de Tarefas e clicar em Nova área de trabalho.', 'C', WTV, tags=JC, origem=VU(2023))
WLX = 'Excluir (Delete) envia o arquivo para a Lixeira; Shift+Delete exclui definitivamente, após confirmação. Um atalho aponta para o caminho do arquivo: se o arquivo for para a Lixeira, o atalho deixa de funcionar até o arquivo ser restaurado ao mesmo local. Excluir o arquivo não exclui seus atalhos.'
q('INF-S-10', G3, WIN, 'Lixeira e atalhos', 'Excluído um arquivo que tinha um atalho na área de trabalho, o atalho deixa de funcionar até que o arquivo seja restaurado da Lixeira para o mesmo local.', 'C', WLX, tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
q('INF-S-11', G3, WIN, 'Lixeira e atalhos', 'No Windows, Shift+Delete envia o arquivo selecionado para a Lixeira.', 'E', WLX, alt='envia o arquivo selecionado para a Lixeira', orig='Shift+Delete exclui definitivamente', tags=R)
WPA = 'Propriedades de uma pasta (botão direito > Propriedades, guia Geral): atributos Somente leitura (aplica-se aos arquivos da pasta) e Oculto; o botão Avançados traz compactar e criptografar.'
q('INF-S-12', G3, WIN, 'Pastas', 'Na guia Geral das Propriedades de uma pasta, os atributos disponíveis são Somente leitura e Oculto.', 'C', WPA, tags=JC, origem=VU(2021))
WMC = 'Menu do botão direito sobre uma pasta no Windows 11: Abrir em nova guia, Abrir em nova janela, Fixar no Acesso rápido, Fixar em Iniciar, Compactar para arquivo ZIP, Copiar como caminho, Propriedades (e Mostrar mais opções).'
q('INF-S-13', G3, WIN, 'Pastas', 'No Windows 11, o menu de contexto de uma pasta oferece as opções Fixar no Acesso rápido e Fixar em Iniciar.', 'C', WMC, tags=JC, origem=VU(2024))
q('INF-S-14', G3, WIN, 'Pastas', 'No Windows 11, uma das opções do menu de contexto de uma pasta é Copiar como atalho.', 'E', WMC, alt='Copiar como atalho', orig='Copiar como caminho', tags=JC, origem=VU(2024))
WNV = 'Criar pasta: botão direito em área vazia > Novo > Pasta, ou Ctrl+Shift+N no Explorador. Criar atalho na área de trabalho: arrastar com o botão DIREITO e escolher Criar atalhos aqui, ou botão direito > Enviar para > Área de trabalho (criar atalho).'
q('INF-S-15', G3, WIN, 'Pastas', 'No Explorador de Arquivos, Ctrl+Shift+N cria uma nova pasta.', 'C', WNV, tags=R)
q('INF-S-16', G3, WIN, 'Atalhos de arquivo', 'Arrastando um programa com o botão direito do mouse até a área de trabalho, pode-se escolher a opção Criar atalhos aqui.', 'C', WNV, tags=JC, origem=VU(2021))

# ---------------- E-MAIL E INTERNET ----------------
EC = 'Para: e Cc: ficam visíveis a todos os destinatários. Cco (cópia oculta): o destinatário recebe, mas ninguém vê seu endereço — nem os outros Cco. Responder a todos vai para o remetente + Para + Cc (nunca para os Cco, que ninguém vê).'
q('INF-E-01', G4, EM, 'Cc e Cco', 'Um e-mail foi enviado com A no campo Para, B em Cc e C em Cco. A sabe que B recebeu a mensagem, mas não sabe que C a recebeu.', 'C', EC, tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
q('INF-E-02', G4, EM, 'Cc e Cco', 'Quem está em Cco consegue ver os endereços dos demais destinatários em Cco.', 'E', EC, alt='consegue ver os endereços dos demais destinatários em Cco', orig='nem os outros Cco', tags=R)
q('INF-E-03', G4, EM, 'Cc e Cco', 'Se o destinatário em Cc clicar em Responder a todos, a resposta também será enviada aos destinatários que estavam em Cco.', 'E', EC, alt='também será enviada aos destinatários que estavam em Cco', orig='nunca para os Cco', tags=JC, origem=VU(2025))
ER = 'Responder e Responder a todos NÃO incluem os anexos da mensagem original; Encaminhar inclui os anexos por padrão. É possível anexar vários arquivos a uma única mensagem.'
q('INF-E-04', G4, EM, 'Responder e encaminhar', 'Ao encaminhar uma mensagem, os anexos da mensagem original são incluídos, por padrão, na nova mensagem.', 'C', ER, tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
q('INF-E-05', G4, EM, 'Responder e encaminhar', 'Ao usar Responder a todos, os anexos da mensagem original são reenviados automaticamente.', 'E', ER, alt='são reenviados automaticamente', orig='NÃO incluem os anexos', tags=R)
q('INF-E-06', G4, EM, 'Responder e encaminhar', 'Para retransmitir dois anexos recebidos em mensagens diferentes, é necessário enviar duas mensagens separadas.', 'E', ER, alt='é necessário enviar duas mensagens separadas', orig='É possível anexar vários arquivos a uma única mensagem', tags=JC, origem=VU(2021))
EP = 'Prefixos no assunto: Re: (ou RES:) = resposta; Fwd: (ou Enc:/ENC:) = encaminhamento. Cada ação acrescenta o prefixo À ESQUERDA. "Fwd: Enc: Re: X" = encaminhamento de um encaminhamento de uma resposta à mensagem X. Os prefixos não indicam anexo nem número de destinatários.'
q('INF-E-07', G4, EM, 'Prefixos', 'Uma mensagem com o assunto "Fwd: Enc: Re: Contrato" resultou de dois encaminhamentos de uma resposta à mensagem original.', 'C', EP, tags=JC, origem=VU(2024))
q('INF-E-08', G4, EM, 'Prefixos', 'O prefixo "Re:" no assunto indica que a mensagem contém arquivo anexo.', 'E', EP, alt='indica que a mensagem contém arquivo anexo', orig='Re: (ou RES:) = resposta', tags=R)
EU = 'URL: protocolo://domínio[:porta]/caminho?consulta#fragmento. Ex.: https://www.site.com:8080/pasta/arq.html?id=123#sec1 → protocolo (esquema) https; domínio www.site.com; porta 8080; caminho /pasta/arq.html; consulta (query string, opcional) id=123; fragmento sec1. Portas padrão: HTTP 80, HTTPS 443.'
q('INF-I-01', G4, NET, 'URL', 'A estrutura básica de uma URL é protocolo://domínio/caminho.', 'C', EU, tags=JC, origem=VU(2021))
q('INF-I-02', G4, NET, 'URL', 'Em https://www.site.com:8080/pasta/arq.html?id=123#sec1, o trecho sec1 é o fragmento e 8080 é a porta.', 'C', EU, tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
q('INF-I-03', G4, NET, 'URL', 'A porta padrão do protocolo HTTP é a 800.', 'E', EU, alt='800', orig='HTTP 80', tags=JC, origem=VU(2024))
q('INF-I-04', G4, NET, 'URL', 'A query string (ex.: ?id=123) é parte obrigatória de toda URL.', 'E', EU, alt='é parte obrigatória de toda URL', orig='consulta (query string, opcional)', tags=JC, origem=VU(2023))
EG = 'Operadores do Google: "frase exata" (aspas); -palavra exclui; * curinga dentro de uma frase; site:dominio restringe ao site; intitle: palavra no título; intext: uma palavra no corpo; allintext: TODAS as palavras seguintes no corpo; filetype:pdf tipo de arquivo; OR alternativa.'
q('INF-I-05', G4, NET, 'Google', 'Para buscar páginas que contenham no corpo, ao mesmo tempo, as palavras segurança, dados e privacidade, pode-se usar allintext:segurança dados privacidade.', 'C', EG, tags=JC, origem=VU(2025))
q('INF-I-06', G4, NET, 'Google', 'No Google, o sinal de menos antes de uma palavra (ex.: -clube) inclui obrigatoriamente essa palavra nos resultados.', 'E', EG, alt='inclui obrigatoriamente essa palavra nos resultados', orig='-palavra exclui', tags=JC, origem=VU(2024))
q('INF-I-07', G4, NET, 'Google', 'A busca site:tjsp.jus.br escrevente restringe os resultados a páginas do domínio tjsp.jus.br.', 'C', EG, tags=R)
q('INF-I-08', G4, NET, 'Google', 'No Google, o termo entre aspas, como "tribunal de justiça", busca páginas com essas palavras em qualquer ordem.', 'E', EG, alt='em qualquer ordem', orig='"frase exata" (aspas)', tags=R)
EA = 'Navegação anônima (InPrivate/anônima): ao fechar a janela, não ficam salvos histórico, cookies e dados de formulários; downloads e favoritos criados continuam. Não torna o usuário invisível para o provedor, o empregador ou os sites visitados.'
q('INF-I-09', G4, NET, 'Navegadores', 'Na navegação anônima, as informações inseridas em formulários não são salvas pelo navegador após o encerramento da sessão.', 'C', EA, tags=JC, origem=VU(2021))
q('INF-I-10', G4, NET, 'Navegadores', 'A navegação anônima impede que o provedor de internet saiba quais sites o usuário visitou.', 'E', EA, alt='impede que o provedor de internet saiba quais sites o usuário visitou', orig='Não torna o usuário invisível para o provedor', tags=R)

# ---------------- TEAMS E ONEDRIVE ----------------
TC = 'Canais do Teams: PADRÃO (todos os membros da equipe), PRIVADO (só um subconjunto da equipe) e COMPARTILHADO (pode incluir pessoas de fora da equipe e da organização). A Moderação de canal existe apenas no canal padrão — não nos canais privados nem nos compartilhados.'
q('INF-T-01', G5, TM, 'Canais', 'No Teams, um canal privado permite limitar o acesso a um subconjunto dos membros da equipe.', 'C', TC, tags=JC, origem=VU(2024))
q('INF-T-02', G5, TM, 'Canais', 'No Teams, o recurso de Moderação aplica-se aos canais privados e compartilhados.', 'E', TC, alt='aos canais privados e compartilhados', orig='A Moderação de canal existe apenas no canal padrão', tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
q('INF-T-03', G5, TM, 'Canais', 'No Teams, todo canal de uma equipe deve incluir obrigatoriamente todos os membros dessa equipe.', 'E', TC, alt='deve incluir obrigatoriamente todos os membros dessa equipe', orig='PRIVADO (só um subconjunto da equipe)', tags=JC, origem=VU(2021))
TMN = 'Para mencionar alguém num chat ou canal do Teams e notificá-lo: digitar @ seguido do nome (@fulano).'
q('INF-T-04', G5, TM, 'Menções', 'No chat do Teams, para mencionar um usuário e notificá-lo automaticamente, digita-se #fulano.', 'E', TMN, alt='#fulano', orig='@ seguido do nome', tags=JC, origem=VU(2025))
TR = 'Barra da reunião do Teams: Chat, Pessoas, Reagir, Exibição (Galeria, Modo Juntos, Destaque/Foco no conteúdo...), Câmera, Microfone, Compartilhar (conteúdo/tela). Recorrência ao agendar: Não se repete, Todos os dias da semana (seg. a sex.), Diariamente, Semanalmente, Mensalmente e Personalizado.'
q('INF-T-05', G5, TM, 'Reuniões', 'Para apresentar a tela durante uma reunião do Teams, usa-se o botão Compartilhar.', 'C', TR, tags=JC, origem=VU(2023))
q('INF-T-06', G5, TM, 'Reuniões', 'O botão Exibição, na reunião do Teams, oferece o modo Galeria para ver os participantes.', 'C', TR, tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
q('INF-T-07', G5, TM, 'Reuniões', 'Entre as opções de recorrência predefinidas do Teams estão Diariamente e Semanalmente.', 'C', TR, tags=JC, origem=VU(2023))
q('INF-T-08', G5, TM, 'Reuniões', 'Entre as opções de recorrência predefinidas do Teams está De hora em hora.', 'E', TR, alt='De hora em hora', orig='Diariamente, Semanalmente, Mensalmente e Personalizado', tags=JC, origem=VU(2023))
OC = 'Cofre Pessoal (OneDrive): pasta protegida por uma etapa EXTRA de verificação de identidade; bloqueia-se sozinho após inatividade (20 minutos, por padrão); arquivos do Cofre não podem ser compartilhados; na conta GRATUITA cabem até 3 arquivos (desde 2024, assinantes do Microsoft 365 — inclusive o Basic — não têm mais limite de quantidade, só o de armazenamento).'
q('INF-O-01', G5, OD, 'Cofre Pessoal', 'O Cofre Pessoal do OneDrive tem uma camada extra de proteção para o seu acesso.', 'C', OC, tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
q('INF-O-02', G5, OD, 'Cofre Pessoal', 'Os arquivos guardados no Cofre Pessoal podem ser compartilhados diretamente com outros usuários.', 'E', OC, alt='podem ser compartilhados diretamente com outros usuários', orig='arquivos do Cofre não podem ser compartilhados', tags=JC, origem=VU(2024))
q('INF-O-03', G5, OD, 'Cofre Pessoal', 'No plano gratuito do OneDrive, o Cofre Pessoal comporta até 5 arquivos.', 'E', OC, alt='até 5 arquivos', orig='até 3 arquivos', tags=JC, origem=VU(2024))
OS = 'Arquivos sob demanda: nuvem = somente online; círculo com ✓ verde vazado = disponível localmente; círculo verde cheio = Sempre manter neste dispositivo. Arquivo apenas "disponível localmente" pode voltar a ser só online para liberar espaço (Sensor de Armazenamento), sem ação do usuário; o "Sempre manter" não. Configurações do OneDrive: Sincronizar e fazer backup, Conta, Notificações e Sobre; em Configurações avançadas, é possível limitar as taxas de upload (carregamento) e download.'
q('INF-O-04', G5, OD, 'Sincronização', 'Um arquivo do OneDrive marcado como disponível localmente pode deixar de estar no dispositivo por falta de espaço, mesmo sem ação direta do usuário.', 'C', OS, tags=JC, origem=VU(2025))
q('INF-O-05', G5, OD, 'Sincronização', 'Nas configurações avançadas do OneDrive, é possível limitar as taxas de download e de carregamento (upload).', 'C', OS, tags=JC, origem=VU(2024, 'Escrevente Técnico Judiciário — TJ-SP (reaplicação)'))
q('INF-O-06', G5, OD, 'Sincronização', 'As configurações do OneDrive trazem as seções Sincronizar e fazer backup, Conta, Notificações e Sobre.', 'C', OS, tags=JC, origem=VU(2024))
q('INF-O-07', G5, OD, 'Sincronização', 'No OneDrive, o ícone de nuvem ao lado de um arquivo indica que ele está sempre disponível no dispositivo, mesmo sem internet.', 'E', OS, alt='está sempre disponível no dispositivo, mesmo sem internet', orig='nuvem = somente online', tags=R)

VER = {'INF-O-01','INF-O-02','INF-O-03','INF-O-04','INF-S-05','INF-S-06','INF-S-07','INF-S-08','INF-T-01','INF-T-02','INF-T-07','INF-T-08','INF-X-12','INF-X-13','INF-X-14','INF-W-09','INF-W-10','INF-S-13'}
for o in Q:
    if o['id'] in VER: o['fonte'] += '. Regra conferida no suporte oficial da Microsoft em 24/11/2026'
if __name__ == '__main__':
    import json, collections
    e = validar(Q); print(len(Q), e, collections.Counter(x['grupo'] for x in Q), collections.Counter(x['gabarito'] for x in Q))
    json.dump(Q, open('info.json', 'w'), ensure_ascii=False, indent=1)
