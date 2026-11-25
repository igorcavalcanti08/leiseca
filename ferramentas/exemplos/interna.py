from common import factory, validar
R850 = 'Resolução TJSP 850/2021 (Teletrabalho)'
R963 = 'Resolução TJSP 963/2025 (eproc)'
LC = 'Lei Complementar Estadual 1.111/2010 (Plano de Cargos e Carreiras do TJSP)'
RI = 'Regimento Interno do TJSP'
NS = 'Normas da Corregedoria Geral da Justiça (NSCGJ), Tomo I'
def X(lei, p, rub=None): return {'lei': lei, 'p': p, 'rub': rub}
L = {
 't3': X(R850, ["Art. 3º. O regime de teletrabalho, contanto que exercido de acordo com as regras dispostas na presente Resolução, assegurará a quem o realize os mesmos direitos do regime de trabalho presencial, inclusive auxílio-alimentação, exceção feita ao auxílio-transporte.",
  "Art. 4º. O regime de teletrabalho não será permitido se implicar qualquer despesa ao Tribunal de Justiça de São Paulo.",
  "Art. 20. O Tribunal de Justiça não arcará com nenhum custo na aquisição de bens ou serviços para o(a) servidor(a) em teletrabalho."], 'Direitos e custos'),
 't9': X(R850, ["Art. 9º. O teletrabalho de servidores(as) sujeita-se às seguintes regras:",
  "I - exigência de que as atividades sejam, exclusivamente, relativas a processamentos digitais;",
  "III - nas unidades de primeiro grau, com exceção dos gabinetes, a quantidade de servidores (as) em teletrabalho, por unidade, será de até 50% (cinquenta por cento) do quadro, arredondadas as frações para o primeiro número inteiro imediatamente superior;",
  "IV - nos gabinetes, o número de servidores (as) em teletrabalho será definido pelo(a) Juiz(a) ou Desembargador(a);",
  "VIII - intervalo para almoço, de 30 minutos, admitida a tolerância de até 15 minutos, deverá ocorrer, obrigatoriamente, no período compreendido entre 12h e 14h, sendo vedado nesse período o agendamento de reuniões ou contato com o(a) servidor(a) para qualquer finalidade, salvo situação de urgência;",
  "X - o alcance da meta de produtividade estabelecida para o(a) servidor(a) em teletrabalho equivale ao cumprimento de sua jornada de trabalho e a superação dela não implica pagamento de gratificação de horas extras ou a formação de banco de horas."], 'Regras do teletrabalho'),
 't10': X(R850, ["Art. 10. O teletrabalho, de caráter facultativo e realizado no interesse e a critério da Administração, dependerá de apresentação de requerimento, em formulário próprio, do qual constará a autorização prévia do(a) Desembargador(a), Juiz(a) ou gestor(a) da unidade, além de compromisso do(a) interessado(a) de cumprir integralmente os parâmetros e deveres previstos neste ato e no Manual de Orientação de Teletrabalho e declaração expressa do(a) servidor(a) de que o local em que executará o teletrabalho atende às exigências do Tribunal de Justiça.",
  "§ 4º. O(A) servidor(a) em regime de teletrabalho poderá requerer, desde que atendido o interesse e a critério da Administração, autorização para residir em local diverso de sua lotação."], 'Requerimento'),
 't11': X(R850, ["Art. 11. É vedada a participação em teletrabalho aos(às) servidores(as) que:",
  "I - apresentem contraindicações por motivo de saúde, devidamente comprovadas por laudo médico;",
  "II - tenham sofrido penalidade disciplinar nos 2 (dois) anos anteriores à solicitação;",
  "III - tenham sido desligados(as) do teletrabalho nos últimos 6 (seis) meses, nos termos indicados no artigo 19, inciso IV, desta resolução;",
  "IV - tenham sido relotados(as) pelo processo de remoção, nos últimos 6 (seis) meses;",
  "V - não tenham alcançado conceito positivo na avaliação de desempenho mais recente;",
  "VI - estejam no primeiro ano do estágio probatório."], 'Vedações'),
 't12': X(R850, ["Art. 12. São deveres do(a) servidor(a) em teletrabalho:",
  "VII - cumprir diretamente as atividades atribuídas em regime de teletrabalho, sendo vedada a utilização de terceiros, servidores(as) ou não, para o cumprimento das metas estabelecidas;",
  "Art. 13. No caso de descumprimento dos deveres estabelecidos nesta Resolução, ou em caso de denúncia motivada e identificada, o(a) servidor(a) deverá prestar, em 2 (dois) dias úteis, esclarecimentos ao(à) gestor(a) da unidade, que poderá, se for o caso, suspender o teletrabalho, comunicando o fato à Secretaria de Gestão de Pessoas - SGP.",
  "Art. 16. Sempre que entender conveniente e necessário, e no interesse e a critério da Administração, o(a) servidor(a) em teletrabalho poderá prestar serviços nas dependências de sua unidade de lotação, mediante autorização do(a) gestor(a).",
  "Art. 18. A produtividade do(a) servidor(a) em teletrabalho deverá ser superior à produtividade aferida na atividade presencial da unidade de trabalho."], 'Deveres e produtividade'),
 't19': X(R850, ["Art. 19. O(A) servidor(a) será desligado(a) do teletrabalho:",
  "I - a qualquer tempo, por pedido pessoal;",
  "V - a critério do(a) gestor(a) da unidade ou por deliberação da Presidência, a qualquer tempo.",
  "§ 1º. Em caso de cessação do teletrabalho, o(a) servidor(a) terá o prazo de até 5 (cinco) dias úteis para retorno ao trabalho presencial, mantido, no período, o dever de cumprimento das atividades definidas no plano de trabalho."], 'Desligamento'),
 't24': X(R850, ["Art. 24. Os(as) magistrados(as) titulares de comarcas de entrância final e os titulares de Comarcas de entrância intermediária com mais de 3 (três) varas, que optarem pelo regime de teletrabalho, deverão comparecer ao fórum pelo menos 3 (três) dias úteis por semana.",
  "§ 1º. Os(as) magistrados(as) titulares de comarcas de entrância intermediária com 3 (três) ou menos varas, os(as) titulares de comarcas de entrância inicial e os(as) juízes(as) substitutos(as), que optarem pelo regime de teletrabalho, deverão comparecer ao fórum pelo menos 4 (quatro) dias úteis por semana."], 'Teletrabalho de magistrados'),
 't32': X(R850, ["Art. 32. Os(As) magistrados(as) e os(as) servidores(as) com deficiência, necessidades especiais ou doença grave, ou que tenham filhos(as) ou dependentes legais nessa condição, poderão requerer diretamente à Presidência do Tribunal de Justiça a concessão de condição especial de trabalho em uma ou mais das modalidades previstas neste Capítulo, independentemente de compensação laboral posterior e sem prejuízo da remuneração.",
  "§ 5º. Para fins da manutenção das condições especiais de trabalho deverá ser apresentado, anualmente, laudo médico que ateste a permanência da situação que deu ensejo à concessão."], 'Condição especial de trabalho'),
 'e10': X(R963, ["Art. 10 - Implantado o sistema eproc em determinada competência de uma unidade judiciária, o ajuizamento de novos processos nessa competência será admitido exclusivamente por meio do eproc.",
  "§2º - O cumprimento definitivo de sentença no sistema eproc será iniciado por petição inicial autônoma, observada a classe processual \"Cumprimento de Sentença\", que será vinculado ao principal, quando tramitar na mesma unidade.",
  "Art. 11 - Os processos ajuizados antes da implantação do sistema eproc, bem como os recursos, incidentes e processos dependentes ou conexos, continuarão tramitando no sistema legado até o seu encerramento, ressalvada a hipótese de migração.",
  "§2º - O cumprimento definitivo de sentença oriundo de processo que tramitou no sistema legado deverá ser iniciado nesse mesmo sistema, até que seja disponibilizada, no eproc, a funcionalidade específica para essa finalidade, conforme regulamentação própria.",
  "Art. 14 - A identificação do sistema processual correto e a prática do respectivo ato processual competem exclusivamente ao peticionante, sob pena de não produção dos respectivos efeitos jurídicos."], 'Implantação'),
 'e4': X(R963, ["Art. 4º - A governança será exercida pelos seguintes órgãos:", "I - Comitê Gestor do eproc - Cge;", "II - Núcleo de Gestão Negocial - NGN; e", "III - Núcleo de Gestão Técnica - NGT.",
  "Parágrafo único - Os usuários externos poderão apresentar demandas relacionadas ao sistema eproc exclusivamente por meio do Comitê Interinstitucional, que exercerá o primeiro filtro de pertinência e relevância."], 'Governança'),
 'e16': X(R963, ["§1º - É dever do usuário interno com perfil de gestor do sistema ou de seu substituto gerenciar o acesso dos magistrados e demais usuários internos que lhe estejam subordinados, bem como interrompê-lo após o encerramento do vínculo com a unidade em até 24 (vinte e quatro) horas, sob pena de responsabilidade."], 'Usuários'),
 'e21': X(R963, ["Art. 21 - Os prazos que se vencerem no dia de indisponibilidade do sistema serão prorrogados para o dia útil seguinte à retomada do funcionamento, quando:",
  "I - a indisponibilidade for superior a 60 (sessenta) minutos, ininterruptos ou não, e ocorrer entre 12h00min e 23h00min;",
  "II - a indisponibilidade ocorrer por qualquer período entre 23h01min e 00h00min.",
  "§1º - A indisponibilidade ocorrida entre 00h01min e 11h59min dos dias de expediente forense e a ocorrida em feriados e finais de semana, por qualquer período, não produzirão o efeito do caput deste artigo."], 'Indisponibilidade'),
 'e26': X(R963, ["Art. 26 - Considera-se realizado o ato processual no dia e hora do seu envio ao sistema eproc.",
  "§1º - Quando o ato for praticado para atender prazo processual, será considerado tempestivo aquele transmitido integralmente até as 24 (vinte e quatro) horas do seu último dia.",
  "§2º - O eproc considerará o horário oficial de Brasília - DF.",
  "Parágrafo único - Havendo necessidade das partes de documento comprobatório de qualquer evento do processo eletrônico, deverá fazer uso da funcionalidade \"certidão narratória\", que terá a mesma validade de certidão de objeto e pé para todos os fins de direito."], 'Atos processuais e certidão narratória'),
 'e34': X(R963, ["Art. 34 - Os agravos de instrumento tirados de processos que tramitam pelo sistema eproc serão interpostos no sistema de primeiro grau, por intermédio do link apropriado, que os enviará automaticamente ao sistema de segundo grau do tribunal competente, onde serão processados em autos apartados com nova numeração.",
  "§1º - A parte agravante juntará apenas a petição inicial do agravo de instrumento com as suas razões, devendo indicar precisamente a decisão agravada, preferentemente por referência ao evento que a gerou, dispensada a juntada de quaisquer peças existentes no processo de primeiro grau.",
  "Art. 41 - Em caso de indisponibilidade absoluta do sistema eproc, devidamente certificada, e para o fim de evitar perecimento de direito ou ofensa à liberdade de locomoção, a petição poderá ser protocolizada em meio físico para distribuição manual, com posterior digitalização e inserção no sistema pelo juízo a que for distribuída."], 'Recursos e indisponibilidade absoluta'),
 'lc11': X(LC, ["Artigo 11 - O servidor nomeado para cargo de provimento efetivo ficará sujeito, durante o período de 36 (trinta e seis) meses, a Estágio Probatório, ao longo do qual a assiduidade, pontualidade, aptidão, capacidade e eficiência que demonstrar serão objeto de avaliação, para a efetivação na carreira.",
  "Artigo 13 - A Progressão é a passagem do servidor de cargo de provimento efetivo de um grau para o imediatamente superior, dentro da mesma referência e nível.",
  "I - tenha cumprido, no mesmo cargo efetivo e grau, o interstício mínimo de 1 (um) ano de efetivo exercício;",
  "Artigo 18 - O servidor poderá interpor recurso ao Comitê de Recursos Humanos no prazo máximo de 30 (trinta) dias corridos, a contar da publicação do resultado do processo da Progressão.",
  "Artigo 21 - A Promoção é a passagem do servidor de cargo de provimento efetivo para o de nível e grau imediatamente superior, dentro da mesma referência."], 'Estágio, progressão e promoção'),
 'lc29': X(LC, ["Artigo 29 - O Acesso é a forma de provimento vertical de cargo em comissão de direção, coordenação, supervisão ou chefia do servidor ocupante de cargo efetivo.",
  "Artigo 30 - Os cargos em comissão de direção, coordenação, supervisão, ou chefia, ficam reservados para provimento exclusivo de servidores públicos titulares de cargos efetivos de mesma natureza e mesma profissão do Quadro do Tribunal de Justiça do Estado de São Paulo, na seguinte proporção:",
  "I - em sua totalidade, os de Chefe de Seção Judiciário e Chefe de Seção Técnica Judiciário;",
  "IV - 70% (setenta por cento), para os de Diretor.",
  "Artigo 31 - Os candidatos a cargos em comissão de direção, coordenação, supervisão, ou chefia, deverão ter exercido anteriormente cargos dessa natureza, ainda que em substituição, ou comprovar experiência adequada, de acordo com critérios estabelecidos pelo Comitê de Recursos Humanos.",
  "III - resultados finais positivos nos últimos 3 (três) processos anuais de Avaliação de Desempenho;"], 'Acesso'),
 'lc37': X(LC, ["Artigo 37-A - É instituído o Adicional de Qualificação - AQ destinado aos servidores do Tribunal de Justiça, em razão dos conhecimentos adicionais adquiridos, comprovados por meio de títulos, diplomas ou certificados de cursos de graduação ou pós-graduação, em sentido amplo ou estrito.",
  "§ 1° - O adicional de que trata este artigo não será concedido quando o curso constituir requisito ou estiver no mesmo nível de escolaridade para ingresso no cargo efetivo ou em comissão.",
  "Artigo 37-B - O Adicional de Qualificação - AQ incidirá sobre os vencimentos brutos equivalentes à base de contribuição previdenciária do cargo em que o servidor estiver em exercício, da seguinte forma:",
  "I - 20% (vinte por cento), em se tratando de título de Doutor;", "II - 15% (quinze por cento), em se tratando de título de Mestre;",
  "III -10% (dez por cento), em se tratando de certificado de Especialização; e",
  "IV - 7,5% (sete inteiros e cinco décimos por cento), em se tratando de diploma de graduação em curso superior.",
  "§ 1° - Em nenhuma hipótese o servidor perceberá cumulativamente qualquer percentual dentre os previstos nos incisos I a IV do ‘caput’ deste artigo.",
  "Artigo 51 - Fica criado o instituto de Remoção, destinado a propiciar a alteração de posto de trabalho, a pedido, dos servidores dentro do Quadro do Tribunal de Justiça."], 'Adicional de Qualificação e remoção'),
 'ri116': X(RI, ["Art. 116. As sessões realizar-se-ão no período compreendido entre nove e dezessete horas dos dias úteis, podendo haver prorrogação sempre que o serviço o exigir.",
  "Art. 118. Se, até trinta minutos após a hora marcada, o magistrado responsável pela audiência não houver comparecido, poderão os presentes retirar-se, registrado o fato em livro próprio.",
  "Art. 120. As atas serão submetidas à aprovação do órgão colegiado na sessão subsequente.",
  "Art. 122. O interessado, mediante petição dirigida ao presidente da sessão, poderá reclamar contra erro contido em ata, dentro de quarenta e oito horas, contadas da publicação ou, não havendo, de sua aprovação."], 'Sessões e atas'),
 'ri123': X(RI, ["§ 2º Para cada sessão, será organizada uma pauta de julgamento, com observância da ordem de apresentação dos feitos, em relação aos da mesma classe; os apresentados no mesmo dia serão inscritos segundo a ordem ascendente numérica.",
  "§ 3° Independe de pauta o julgamento de 'habeas corpus', de desaforamento, de conflito de jurisdição, de competência ou de atribuição e de embargos de declaração, estes em matéria criminal apenas.",
  "Art. 124. Salvo deliberação em contrário, recaindo a data da sessão em feriado ou dia em que não haja expediente forense, os feitos incluídos em pauta serão julgados na sessão ordinária seguinte, independentemente de nova publicação.",
  "Art. 127. A pauta de julgamento será publicada, pelo menos, cinco dias antes da data da sessão correlata, sua cópia será afixada à porta da sala da sessão, com antecedência mínima de quinze minutos, e entregue a cada desembargador."], 'Pauta'),
 'ri134': X(RI, ["Art. 134. Nenhum feito será julgado na ausência do relator, ainda que já tenha proferido voto, salvo se, iniciado o julgamento, vier ele a se afastar, computando-se os votos proferidos.",
  "§ 2º A ausência ocasional de vogal não acarretará adiamento, se for possível substituição por outro juiz.",
  "Art. 138. Quando, na votação de questão indecomponível ou de questões distintas, se formarem correntes divergentes, sem que se alcance a maioria exigida, prevalecerá a média dos votos ou o voto intermediário.",
  "§ 2º Em matéria criminal, firmando-se mais de duas correntes sobre a pena aplicável, sem que nenhuma delas alcance a maioria, os votos pela imposição da mais grave serão reunidos aos proferidos para a imediatamente inferior, e assim por diante, até constituir-se a maioria. Persistindo o empate, o presidente, se não tiver votado, proferirá seu voto; em caso contrário, prevalecerá a decisão mais favorável ao réu.",
  "III - havendo empate no julgamento de agravos, considerar-se-á mantida a decisão agravada.",
  "Art. 141. Os desembargadores poderão retificar ou modificar seus votos até a proclamação do resultado."], 'Ordem dos trabalhos e votação'),
 'n6': X(NS, ["§ 2º A correição extraordinária consiste em fiscalização excepcional, realizada a qualquer momento e sem prévio anúncio e poderá ser geral ou parcial, conforme as necessidades e conveniência do serviço correcional.",
  "§ 4º As atas das correições e visitas serão encaminhadas à Corregedoria Geral da Justiça nos prazos que seguem:",
  "I - correição ordinária – até 60 (sessenta) dias após realizada;",
  "II - correição extraordinária ou visita correcional – até 15 (quinze) dias após realizada.",
  "§ 5º A Corregedoria Geral da Justiça implementará, gradativamente, a correição virtual, com vistas ao controle permanente das atividades subordinadas à sua disciplina.",
  "§ 1º O Corregedor Geral da Justiça, com aprovação do Conselho Superior da Magistratura, poderá, por motivo de interesse público ou conveniência da administração, alterar a designação do Corregedor Permanente."], 'Correições'),
 'n8': X(NS, ["Art. 8º O Juiz Corregedor Permanente efetuará, uma vez por ano, de preferência no mês de dezembro, correição ordinária em todas as serventias, repartições e demais estabelecimentos sujeitos à sua fiscalização correcional, lavrandose o correspondente termo no livro próprio.",
  "§ 1º A correição ordinária será anunciada por edital, afixado no átrio do fórum e publicado no Diário da Justiça Eletrônico, com pelo menos quinze dias de antecedência, bem como comunicada à Ordem dos Advogados do Brasil da respectiva subseção.",
  "Art. 9º Em até 30 (trinta) dias depois de assumir a corregedoria permanente em caráter definitivo, o juiz fará visita correcional às unidades sob sua corregedoria, com o intuito de constatar a regularidade dos serviços, observado o modelo disponibilizado.",
  "§ 1º A visita correcional independe de edital ou qualquer outra providência e dela se lançará sucinto termo no livro de visitas e correições, no qual também constarão as determinações que o Juiz Corregedor Permanente eventualmente fizer no momento.",
  "Art. 10. O escrivão auxiliará o Juiz Corregedor Permanente nas diligências correcionais, facultada a nomeação de escrivão ‘ad hoc’ entre os demais servidores da unidade.",
  "Art. 11. Durante os serviços correcionais, todos os funcionários da unidade permanecerão à disposição do Corregedor Geral da Justiça, dos Juízes Assessores da Corregedoria Geral ou do Juiz Corregedor Permanente, sem prejuízo de requisição de auxílio externo ou de requisição de força policial.",
  "Art. 13. Os estabelecimentos prisionais e outros destinados ao recolhimento de pessoas, sujeitos à atividade correcional do juízo, serão visitados uma vez por mês (art. 66, inciso VII, da LEP)."], 'Correição ordinária e visitas'),
 'n15': X(NS, ["I – Apuração preliminar: quando a infração não estiver suficientemente caracterizada ou definida a autoria. Ao final, poderá ser arquivada ou ensejar a instauração de Sindicância ou Processo Administrativo;",
  "II – Sindicância: quando a falta disciplinar, por sua natureza, possa determinar as penas de repreensão, suspensão ou multa;",
  "§ 1° Os procedimentos disciplinares previstos nos incisos I, II e III serão instaurados por Portaria, dispensado o registro em livro, com a descrição dos fatos e a identificação do servidor (nome completo, matrícula, cargo e posto de trabalho), exceto nas apurações preliminares em que não houver autoria definida.",
  "§ 6º. Os prazos relativos a procedimentos disciplinares serão contados em dias corridos e ficarão suspensos no período de 20 de dezembro a 20 de janeiro."], 'Procedimentos disciplinares'),
 'n49': X(NS, ["§ 1º É vedado ao funcionário credenciado ceder a respectiva senha ou permitir que outrem, funcionário ou não, use-a para acessar indevidamente o sistema informatizado.",
  "Art. 51. Os escrivães judiciais do serviço de distribuição e dos ofícios de justiça realizarão auditoria semanal no sistema, de acordo com os níveis de criticidade definidos, comunicando à Corregedoria Geral da Justiça qualquer irregularidade.",
  "Art. 53. A inserção de dados no sistema informatizado oficial será a mais completa e abrangente possível, de modo que todas as ocorrências do processo físico constem do ambiente virtual, formando banco de dados que servirá de memória permanente.",
  "§ 3º As vítimas identificadas na denúncia ou queixa, e também as testemunhas de processo criminal – sejam estas de acusação, defesa ou comuns –, terão suas qualificações lançadas no sistema informatizado oficial, exceto quando, ao darem conta de coação ou grave ameaça, após deferimento do juiz, pedirem para não haver identificação de seus dados de qualificação e endereço.",
  "Art. 57. Nos ofícios de justiça, o registro e controle da movimentação dos feitos realizar-se-ão exclusivamente pelo sistema informatizado oficial, vedadas a elaboração de fichário por nome de autor e a utilização de fichas individuais materializadas em papel ou constantes de outros sistemas informatizados.",
  "§ 2º O segredo de justiça poderá, ainda, ser gerado automaticamente pelo sistema informatizado, a depender da natureza da ação.",
  "Art. 62. Quando a mesma parte estiver vinculada a processos que tramitam em outros ofícios de justiça, as eventuais retificações de seus dados não serão aplicadas aos feitos de outro juízo."], 'Sistema informatizado oficial'),
 'n81': X(NS, ["Art. 81. Na escrituração serão evitadas as seguintes práticas:", "II - anotações de “sem efeito”;",
  "Art. 82. Na escrituração é vedada:",
  "II - a assinatura de atos ou termos em branco, total ou parcialmente;",
  "III - a utilização de abreviaturas, abreviações, acrônimos, siglas ou símbolos, excetuando-se as formas consagradas pelo Vocabulário Ortográfico da Língua Portuguesa da Academia Brasileira de Letras, as adotadas por órgãos oficiais e as convencionadas por determinada área do conhecimento humano;",
  "IV - a utilização de chancela, ou de qualquer recurso que propicie a reprodução mecânica da assinatura do juiz.",
  "Art. 84. Os instrumentos de ordens, requisições, precatórias, ofícios e autorizações judiciais, bem como dos demais atos e termos processuais (sentenças, decisões e despachos), conterão, de forma legível, o nome completo, o cargo ou função da autoridade judiciária e dos servidores que os lavrem, confiram e subscrevam, a fim de se permitir a rápida identificação."], 'Escrituração'),
 'n85': X(NS, ["Art. 85. Os mandados, as cartas postais, os ofícios gerais de comunicação, expedidos em cumprimento de ato judicial, em não havendo determinação do juiz em sentido contrário, serão assinados pelos escrivães, declarando que o fazem por ordem do juiz.",
  "§ 1º A subscrição do juiz é obrigatória quando:",
  "II - houver determinação de desconto de pensão alimentícia;",
  "III - os documentos ou papéis forem dirigidos a autoridades (por exemplo, membros do Poder Judiciário, do Ministério Público e do Poder Legislativo; chefe do Poder Executivo; Delegados de Polícia; Comandantes da Polícia Militar e das Forças Armadas).",
  "§ 2º A emissão de cartas postais, considerada inclusive a expedição por meio eletrônico, independerão da assinatura do escrivão ou escreventes, desde que do documento conste o nome e o cargo do funcionário emitente, inexista determinação do juiz em sentido contrário, a hipótese não se enquadre nas disposições contidas no § 1º deste artigo e seja observado o disposto no parágrafo único do art. 94."], 'Assinatura de mandados e ofícios'),
 'n104': X(NS, ["§ 2º As certidões serão expedidas no prazo de 5 (cinco) dias, contados da data do recebimento do respectivo pedido pelo ofício de justiça, fornecido ao interessado protocolo de requerimento.",
  "§ 3º Serão atendidos em 5 (cinco) dias úteis os pedidos de certidões de objeto e pé formulados pelo correio eletrônico (e-mail) institucional de um ofício de justiça para outro. A certidão será elaborada e encaminhada pelo ofício de Justiça diretamente à unidade solicitante.",
  "§ 5º - A expedição de certidão de processos que correm em segredo de justiça dependerá de despacho do juiz competente, exceto se requerida por parte ou procurador regularmente habilitado nos autos."], 'Certidões'),
 'n157': X(NS, ["Art. 157. O acesso aos autos judiciais e administrativos de processos em andamento ou findos, mesmo sem procuração, quando não estejam sujeitos a segredo de justiça, é assegurado aos advogados, estagiários de Direito e ao público em geral, por meio do exame em balcão do ofício de justiça ou seção administrativa, podendo ser tomados apontamentos, solicitadas cópias reprográficas, bem como utilizado escâner portátil ou máquina fotográfica10, vedado, nestas hipóteses, o desencarte das peças processuais para reprodução.",
  "Art. 164. Não havendo fluência de prazo, os autos somente serão retirados em carga mediante requerimento.",
  "§ 2º Na fluência de prazo comum, só em conjunto ou mediante prévio ajuste por petição nos autos os procuradores das partes ou seus prepostos retirarão os autos, ressalvada a obtenção de cópias para a qual cada procurador ou preposto poderá retirálos pelo prazo de 2 (duas) a 6 (seis) horas, mediante carga, independentemente de ajuste, observado o término do expediente forense.",
  "Art. 166. É vedada a retenção do documento de identificação do advogado ou do estagiário de Direito no ofício de justiça, para a finalidade de controle de carga de autos, em qualquer modalidade ou circunstância."], 'Consulta e carga'),
 'n176': X(NS, ["Art. 177. Após a publicação da decisão que determinou o arquivamento, os processos permanecerão no ofício de justiça por 30 (trinta) dias, findo o prazo, serão arquivados após realizadas as anotações e atos necessários no sistema informatizado oficial e no sistema da empresa terceirizada (SGDAU).",
  "Art. 178. Quando o cumprimento da sentença condenatória cível se der em juízo diverso daquele que a proferiu (art. 516, parágrafo único, do CPC), o arquivamento dos autos, no âmbito do Poder Judiciário do Estado de São Paulo, deverá ser promovido pelo juízo da execução, que realizará todos os cadastramentos pertinentes à extinção do processo, quando for o caso.",
  "Art. 180. Fica vedada às partes e advogados a consulta ou retirada de processos nos depósitos do Arquivo Terceirizado.",
  "Parágrafo único. O interessado no desarquivamento será intimado, por qualquer meio idôneo de comunicação, da chegada dos autos ao cartório e do prazo de 30 (trinta) dias para manifestação, bem como de que, decorrido o prazo sem manifestação, os autos retornarão ao arquivo.",
  "Parágrafo único. A extração de cópia reprográfica ou certidão de processos com segredo de justiça, bem como o desentranhamento de documentos, dependerão de despacho do juiz competente.",
  "Art. 188. Os requerimentos de desarquivamento de autos, ressalvadas as exceções legais, serão instruídos com o comprovante de recolhimento da respectiva taxa."], 'Arquivamento e desarquivamento'),
 'n1220': X(NS, ["Art. 1.220. As petições intermediárias serão apresentadas pelo peticionamento eletrônico e encaminhadas diretamente ao ofício de justiça correspondente.",
  "Parágrafo único. Na hipótese de materialização do processo, cuja tramitação era em meio eletrônico, passarão a ser admitidas petições em meio físico. Retomada a tramitação no meio eletrônico, não mais serão admitidas petições em meio físico.",
  "§ 1º Em caso de recebimento indevido, caberá ao Setor de Protocolo de origem cancelar o protocolo e intimar o peticionário pelo Diário da Justiça Eletrônico – antes do cadastramento, devolverá a petição ao protocolo de origem. Se a verificação ocorrer após o cadastramento da petição pelo Ofício de Justiça, caberá a este adotar as providências necessárias para a devida regularização.",
  "§ 2º Admitir-se-á, nos Foros Digitais, o protocolo integrado de petições em papel dirigidas a processos físicos em tramitação nas demais Comarcas do Estado.",
  "§ 3º Nos casos dos parágrafos anteriores, cientificar-se-á o requerente de que terá 45 (quarenta e cinco) dias, a partir da digitalização, para retirar a petição, sob pena de inutilização da peça e dos documentos pelo ofício de justiça."], 'Petições intermediárias'),
 'n1237': X(NS, ["Art. 1.237. Na elaboração dos documentos, serão utilizados os modelos de expediente institucionais padronizados, autorizados e aprovados pela Corregedoria Geral da Justiça.",
  "§ 3º - Sempre que cabível, a fim de possibilitar trabalho em lote e filtro nas filas de trabalho pela serventia judicial, deverão ser utilizados modelos de grupo, que conterão, obrigatoriamente, as seguintes características:",
  "b) Nomeação do modelo com termos que correspondam ao teor do documento, inclusive com a informação do ato a ele vinculado, se o caso;"], 'Modelos de documentos'),
}
from interna_L2 import L2
L.update(L2)
QC = {'Q3769022': (2025, 'TJ-SP'), 'Q3769023': (2025, 'TJ-SP'), 'Q3769024': (2025, 'TJ-SP'), 'Q3769025': (2025, 'TJ-SP'), 'Q3769026': (2025, 'TJ-SP'),
      **{f'Q32525{i}': (2024, 'TJ-SP (reaplicação)') for i in range(28, 33)}, **{f'Q31740{i}': (2024, 'TJ-SP') for i in range(72, 76)},
      **{f'Q21767{i}': (2023, 'TJ-SP') for i in range(54, 59)}}
FONTES = {R850: 'GECON/TJSP, texto compilado até 25/04/2022', R963: 'GECON/TJSP', LC: 'ALESP', RI: 'PDF oficial do TJSP, texto atualizado até 12/11/2026', NS: 'PDF oficial da CGJ, texto atualizado até 22/10/2026'}
Q = []
q = factory(Q, L, 'Legislação Interna do TJSP', QC, 'Texto conferido em 24/11/2026')
G1 = 'Teletrabalho (Res. 850/2021)'; G2 = 'eproc (Res. 963/2025)'; G3 = 'Plano de Cargos e Carreiras (LC 1.111/2010)'; G4 = 'Regimento Interno: sessões e julgamento'
G5 = 'Normas CGJ: correições e procedimentos disciplinares'; G6 = 'Normas CGJ: sistema informatizado e escrituração'; G7 = 'Normas CGJ: certidões, carga e arquivo'; G8 = 'Normas CGJ: processo eletrônico'

# G1
q('TEL-003-01', G1, 'Res. 850, arts. 3º e 11, VI', ['t3', 't11'], 'Felipe, escrevente em estágio probatório há dois anos, pode ser enquadrado no teletrabalho e, se o for, perderá o auxílio-transporte, mas não o auxílio-alimentação.', 'C',
  'Só é vedado o teletrabalho no PRIMEIRO ANO do estágio probatório (art. 11, VI). Mantém o auxílio-alimentação; perde o auxílio-transporte (art. 3º).', tags=['caso-concreto'], qc='Q3769023', letra='C')
q('TEL-011-01', G1, 'Res. 850, art. 11, VI', ['t11'], 'É vedado o teletrabalho ao servidor que ainda não concluiu o estágio probatório.', 'E', 'A vedação é só para o PRIMEIRO ANO do estágio probatório.',
  alt='que ainda não concluiu o estágio probatório', orig='estejam no primeiro ano do estágio probatório', tags=['literal'], qc='Q3769023', letra='B')
q('TEL-020-01', G1, 'Res. 850, arts. 4º e 20', ['t3'], 'O servidor em teletrabalho tem direito a auxílio tecnológico para adquirir os bens e serviços necessários ao trabalho remoto.', 'E',
  'O TJ "NÃO ARCARÁ com nenhum custo"; o teletrabalho não pode implicar despesa ao Tribunal.', alt='tem direito a auxílio tecnológico', orig='O Tribunal de Justiça não arcará com nenhum custo', tags=['literal'], qc='Q3769023', letra='E')
q('TEL-009-01', G1, 'Res. 850, art. 9º, III e IV', ['t9'], 'Nas unidades de primeiro grau, exceto os gabinetes, até 50% do quadro pode estar em teletrabalho; nos gabinetes, o número é definido pelo juiz ou desembargador.', 'C', 'Unidades ligadas à Presidência, à Vice, à CGJ e às Presidências de Seção: até 70%.', tags=['literal'], qc='Q3769023', letra='D')
q('TEL-016-01', G1, 'Res. 850, art. 16', ['t12'], 'Enquadrado no teletrabalho, o servidor só pode voltar a trabalhar presencialmente com autorização do juiz titular da vara.', 'E',
  'Pode prestar serviços na unidade mediante autorização do(a) GESTOR(A).', alt='com autorização do juiz titular da vara', orig='mediante autorização do(a) gestor(a)', tags=['literal'], qc='Q3769023', letra='A')
q('TEL-011-02', G1, 'Res. 850, art. 11', ['t11'], 'É vedado o teletrabalho ao servidor que sofreu penalidade disciplinar nos 2 anos anteriores à solicitação ou que foi relotado por remoção nos últimos 6 meses.', 'C', 'Incisos II e IV.', tags=['literal'])
q('TEL-009-02', G1, 'Res. 850, art. 9º, X', ['t9'], 'Superar a meta de produtividade em teletrabalho gera banco de horas para o servidor.', 'E', '"Não implica pagamento de gratificação de horas extras OU a formação de banco de horas."',
  alt='gera banco de horas', orig='a superação dela não implica pagamento de gratificação de horas extras ou a formação de banco de horas', tags=['literal'])
q('TEL-018-01', G1, 'Res. 850, art. 18', ['t12'], 'A produtividade do servidor em teletrabalho deve ser, no mínimo, igual à produtividade aferida na atividade presencial da unidade.', 'E',
  'Deve ser SUPERIOR (salvo os do Capítulo IV, dispensados do acréscimo, § 3º).', alt='no mínimo, igual', orig='deverá ser superior à produtividade aferida na atividade presencial', tags=['literal'])
q('TEL-013-01', G1, 'Res. 850, art. 13', ['t12'], 'Descumpridos os deveres do teletrabalho, o servidor deverá prestar esclarecimentos ao gestor em 2 dias úteis, podendo o teletrabalho ser suspenso.', 'C', 'Literal.', tags=['literal'])
q('TEL-012-01', G1, 'Res. 850, art. 12, VII', ['t12'], 'O servidor em teletrabalho pode contar com a ajuda de colegas da unidade para cumprir suas metas.', 'E', 'É vedada a utilização de terceiros, "servidores(as) ou não".',
  alt='pode contar com a ajuda de colegas da unidade', orig='sendo vedada a utilização de terceiros, servidores(as) ou não', tags=['literal'])
q('TEL-019-01', G1, 'Res. 850, art. 19, § 1º', ['t19'], 'Cessado o teletrabalho, o servidor terá até 5 dias úteis para retornar ao trabalho presencial.', 'C', 'Literal.', tags=['literal'])
q('TEL-009-03', G1, 'Res. 850, art. 9º, VIII', ['t9'], 'O intervalo de almoço do servidor em teletrabalho é de 1 hora, a ser usufruído livremente ao longo do expediente.', 'E',
  '30 minutos (tolerância de 15), obrigatoriamente entre 12h e 14h.', alt='é de 1 hora, a ser usufruído livremente ao longo do expediente', orig='intervalo para almoço, de 30 minutos', tags=['literal'])
q('TEL-024-01', G1, 'Res. 850, art. 24', ['t24'], 'O juiz titular de comarca de entrância final em teletrabalho deve comparecer ao fórum pelo menos 3 dias úteis por semana; o de entrância inicial, pelo menos 4.', 'C', 'Art. 24, caput e § 1º.', tags=['literal'])
q('TEL-032-01', G1, 'Res. 850, art. 32', ['t32'], 'O servidor com filho com deficiência pode requerer à Presidência condição especial de trabalho, independentemente de compensação laboral posterior e sem prejuízo da remuneração, apresentando laudo médico anual.', 'C', 'Art. 32, caput e § 5º.', tags=['literal'])

# G2
q('EPR-011-01', G2, 'Res. 963, art. 11', ['e10'], 'Os processos ajuizados antes da implantação do eproc, com seus recursos, incidentes e processos dependentes ou conexos, continuam no sistema legado até o encerramento, ressalvada a migração.', 'C', 'Literal.', tags=['literal'], qc='Q3769022', letra='E')
q('EPR-010-01', G2, 'Res. 963, art. 10', ['e10'], 'Na fase de implantação, as ações poderão ser propostas no eproc ou no e-SAJ por 60 dias, e só depois disso o eproc será exclusivo.', 'E',
  'Implantado o eproc em uma competência, novos processos serão admitidos EXCLUSIVAMENTE nele.', alt='poderão ser propostas no eproc ou no e-SAJ por 60 dias', orig='será admitido exclusivamente por meio do eproc', tags=['literal'], qc='Q3769022', letra='B')
q('EPR-014-01', G2, 'Res. 963, art. 14', ['e10'], 'O protocolo de petição no sistema processual errado não prejudica a parte: a Secretaria deve intimar o advogado para regularizar em 5 dias.', 'E',
  'Identificar o sistema correto compete EXCLUSIVAMENTE ao peticionante, sob pena de não produção de efeitos.', alt='não prejudica a parte', orig='competem exclusivamente ao peticionante, sob pena de não produção dos respectivos efeitos jurídicos', tags=['literal'], qc='Q3769022', letra='A')
q('EPR-011-02', G2, 'Res. 963, art. 11, § 2º', ['e10'], 'O cumprimento definitivo de sentença de processo que tramitou no sistema legado deve ser iniciado no eproc, por petição inicial autônoma com cópia integral do processo de conhecimento.', 'E',
  'Deve ser iniciado no SISTEMA LEGADO até que o eproc tenha funcionalidade específica.', alt='deve ser iniciado no eproc', orig='deverá ser iniciado nesse mesmo sistema', tags=['literal'], qc='Q3769022', letra='D')
q('EPR-004-01', G2, 'Res. 963, arts. 4º e 8º', ['e4'], 'A governança do eproc é exercida pelo Comitê Gestor (CGe), pelo Núcleo de Gestão Negocial (NGN) e pelo Núcleo de Gestão Técnica (NGT); usuários externos só apresentam demandas pelo Comitê Interinstitucional.', 'C', 'Arts. 4º e 8º, parágrafo único.', tags=['literal'])
q('EPR-021-01', G2, 'Res. 963, art. 21', ['e21'], 'Prorroga-se o prazo para o dia útil seguinte quando a indisponibilidade do eproc for superior a 60 minutos entre 12h e 23h, ou de qualquer duração entre 23h01 e 0h.', 'C', 'Entre 0h01 e 11h59, e em feriados e fins de semana, não há prorrogação.', tags=['literal'])
q('EPR-021-02', G2, 'Res. 963, art. 21, § 1º', ['e21'], 'A indisponibilidade do eproc das 8h às 11h de um dia útil prorroga o prazo que vence nesse dia.', 'E',
  'Indisponibilidade entre 00h01 e 11h59 NÃO produz prorrogação.', alt='prorroga o prazo que vence nesse dia', orig='não produzirão o efeito do caput deste artigo', tags=['caso-concreto'])
q('EPR-026-01', G2, 'Res. 963, art. 26', ['e26'], 'No eproc, é tempestivo o ato transmitido integralmente até as 24 horas do último dia do prazo, pelo horário de Brasília.', 'C', 'Literal.', tags=['literal'])
q('EPR-031-01', G2, 'Res. 963, art. 31, parágrafo único', ['e26'], 'No eproc, a certidão narratória tem a mesma validade da certidão de objeto e pé.', 'C', 'Literal.', tags=['literal'])
q('EPR-034-01', G2, 'Res. 963, art. 34', ['e34'], 'O agravo de instrumento de processo no eproc é interposto no sistema de primeiro grau, e o agravante deve juntar cópia integral do processo de origem.', 'E',
  'Juntará APENAS a petição do agravo com as razões, dispensada a juntada de peças do processo de origem.', alt='deve juntar cópia integral do processo de origem', orig='dispensada a juntada de quaisquer peças existentes no processo de primeiro grau', tags=['literal'])
q('EPR-016-01', G2, 'Res. 963, art. 16, § 1º', ['e16'], 'O gestor do sistema deve interromper o acesso de usuário interno em até 24 horas após o encerramento do vínculo com a unidade.', 'C', 'Literal.', tags=['literal'])
q('EPR-041-01', G2, 'Res. 963, art. 41', ['e34'], 'Em indisponibilidade absoluta e certificada do eproc, para evitar perecimento de direito ou ofensa à liberdade de locomoção, a petição pode ser protocolizada em meio físico.', 'C', 'Literal.', tags=['literal'])

# G3
q('LC-031-01', G3, 'LC 1.111, art. 31', ['lc29'], 'Para ser nomeada Chefe de Seção Judiciário, Tânia deve ter exercido antes cargos dessa natureza, ainda que em substituição, ou comprovar experiência adequada, segundo critérios do Comitê de Recursos Humanos.', 'C', 'Literal.', tags=['caso-concreto'], qc='Q3769024', letra='E')
q('LC-030-01', G3, 'LC 1.111, art. 30, I', ['lc29'], 'O cargo de Chefe de Seção Judiciário é reservado em 70% a servidores efetivos do Quadro do TJSP.', 'E', 'Reservado EM SUA TOTALIDADE. 70% é para Diretor.',
  alt='em 70%', orig='em sua totalidade, os de Chefe de Seção Judiciário', tags=['literal'], qc='Q3769024', letra='C')
q('LC-011-01', G3, 'LC 1.111, art. 11', ['lc11'], 'O estágio probatório dos servidores do TJSP dura 36 meses.', 'C', 'Literal.', tags=['literal'])
q('LC-013-01', G3, 'LC 1.111, arts. 13 e 21', ['lc11'], 'Progressão é a passagem do servidor para o nível e grau imediatamente superior, dentro da mesma referência.', 'E',
  'Isso é PROMOÇÃO. Progressão é a passagem de um GRAU para o imediatamente superior, mesma referência e nível.', alt='Progressão é a passagem do servidor para o nível e grau imediatamente superior', orig='A Progressão é a passagem do servidor de cargo de provimento efetivo de um grau para o imediatamente superior', tags=['troca-de-rubrica'])
q('LC-018-01', G3, 'LC 1.111, art. 18', ['lc11'], 'Do resultado da Progressão cabe recurso ao Comitê de Recursos Humanos em até 30 dias corridos.', 'C', 'Literal.', tags=['literal'])
q('LC-037B-01', G3, 'LC 1.111, art. 37-B', ['lc37'], 'O Adicional de Qualificação é de 20% para doutor, 15% para mestre, 10% para especialização e 7,5% para graduação, sem cumulação.', 'C', 'Literal.', tags=['literal'])
q('LC-037A-01', G3, 'LC 1.111, art. 37-A, § 1º', ['lc37'], 'O escrevente com graduação em Direito recebe Adicional de Qualificação de 7,5%, ainda que o curso seja requisito para o cargo.', 'E',
  'Não é concedido quando o curso é requisito ou do mesmo nível de escolaridade exigido para o cargo. Para o escrevente (ensino médio), a graduação gera o AQ.', alt='ainda que o curso seja requisito para o cargo', orig='não será concedido quando o curso constituir requisito', tags=['literal'])
q('LC-032-01', G3, 'LC 1.111, art. 32, III', ['lc29'], 'Para o acesso a cargos de chefia, exigem-se resultados positivos nos últimos 3 processos anuais de Avaliação de Desempenho.', 'C', 'Literal.', tags=['literal'])

# G4
q('RI-134-01', G4, 'RITJSP, art. 134', ['ri134'], 'Nenhum feito será julgado na ausência do relator, ainda que já tenha votado, salvo se, iniciado o julgamento, ele se afastar, computando-se os votos proferidos.', 'C', 'Literal.', tags=['literal'], qc='Q3769025', letra='A')
q('RI-123-01', G4, 'RITJSP, art. 123, § 3º', ['ri123'], 'No TJSP, só o habeas corpus e os embargos de declaração em matéria criminal podem ser julgados sem prévia inclusão em pauta.', 'E',
  'Também independem de pauta: desaforamento e conflitos de jurisdição, competência ou atribuição.', alt="só o habeas corpus e os embargos de declaração em matéria criminal", orig="Independe de pauta o julgamento de 'habeas corpus', de desaforamento, de conflito de jurisdição", tags=['literal'], qc='Q3769025', letra='C')
q('RI-124-01', G4, 'RITJSP, art. 124', ['ri123'], 'Se a sessão cair em feriado, os feitos em pauta serão julgados na sessão ordinária seguinte, mediante nova publicação.', 'E', '"INDEPENDENTEMENTE de nova publicação".',
  alt='mediante nova publicação', orig='independentemente de nova publicação', tags=['literal'], qc='Q3769025', letra='D')
q('RI-138-01', G4, 'RITJSP, art. 138', ['ri134'], 'Formando-se correntes divergentes sem maioria em questão indecomponível, prevalece o voto do presidente do órgão julgador.', 'E',
  'Prevalece a MÉDIA DOS VOTOS ou o VOTO INTERMEDIÁRIO.', alt='prevalece o voto do presidente do órgão julgador', orig='prevalecerá a média dos votos ou o voto intermediário', tags=['literal'], qc='Q3769025', letra='E')
q('RI-120-01', G4, 'RITJSP, art. 120', ['ri116'], 'A ata da sessão de julgamento deve ser aprovada e assinada ao final da própria sessão.', 'E', 'É submetida à aprovação na sessão SUBSEQUENTE.',
  alt='ao final da própria sessão', orig='na sessão subsequente', tags=['literal'], qc='Q3769025', letra='B')
q('RI-127-01', G4, 'RITJSP, art. 127', ['ri123'], 'A pauta de julgamento será publicada pelo menos 5 dias antes da sessão.', 'C', 'Literal.', tags=['literal'])
q('RI-122-01', G4, 'RITJSP, art. 122', ['ri116'], 'O interessado pode reclamar contra erro na ata em até 48 horas da publicação ou, não havendo, da aprovação.', 'C', 'A reclamação não suspende o prazo de recurso.', tags=['literal'])
q('RI-139-01', G4, 'RITJSP, art. 139, §§ 2º e 3º, III', ['ri134'], 'Havendo empate no julgamento de agravo, considera-se mantida a decisão agravada; em matéria criminal, persistindo o empate sobre a pena, prevalece a decisão mais favorável ao réu se o presidente já votou.', 'C', 'Literal.', tags=['literal'])
q('RI-118-01', G4, 'RITJSP, art. 118', ['ri116'], 'Se o magistrado não comparecer à audiência no Tribunal até 15 minutos após a hora marcada, os presentes podem retirar-se.', 'E', 'Até TRINTA minutos.',
  alt='até 15 minutos', orig='até trinta minutos após a hora marcada', tags=['literal'])

# G5
q('NS-013-01', G5, 'NSCGJ, art. 13', ['n8'], 'Os estabelecimentos destinados ao recolhimento de pessoas, sujeitos à atividade correcional do juízo, serão visitados uma vez por mês.', 'C', 'Art. 66, VII, da LEP.', tags=['literal'], qc='Q3252528', letra='B')
q('NS-009-01', G5, 'NSCGJ, art. 9º, § 1º', ['n8'], 'Na visita correcional, o juiz deve comunicar previamente à unidade o dia e o horário.', 'E', 'A visita correcional "INDEPENDE de edital ou qualquer outra providência".',
  alt='deve comunicar previamente à unidade o dia e o horário', orig='A visita correcional independe de edital ou qualquer outra providência', tags=['literal'], qc='Q3252528', letra='A')
q('NS-011-01', G5, 'NSCGJ, art. 11', ['n8'], 'Durante os serviços correcionais, os funcionários ficam à disposição do Juiz Corregedor Permanente, se houver anuência do juiz titular da unidade.', 'E', 'Não há essa condição: todos permanecem à disposição.',
  alt='se houver anuência do juiz titular da unidade', orig='todos os funcionários da unidade permanecerão à disposição', tags=['literal'], qc='Q3252528', letra='C')
q('NS-006-01', G5, 'NSCGJ, art. 6º, § 4º', ['n6'], 'As atas são encaminhadas à CGJ em até 60 dias da correição ordinária e em até 15 dias da correição extraordinária ou da visita correcional.', 'C', 'Literal.', tags=['literal'], qc='Q3174072', letra='B')
q('NS-006-02', G5, 'NSCGJ, art. 6º, § 4º', ['n6'], 'A ata da correição ordinária deve ser elaborada em até 15 dias.', 'E', 'Ordinária: até 60 dias. Extraordinária e visita: até 15.',
  alt='em até 15 dias', orig='correição ordinária – até 60 (sessenta) dias após realizada', tags=['literal'], qc='Q3252528', letra='D')
q('NS-006-03', G5, 'NSCGJ, art. 6º, § 5º', ['n6'], 'São vedadas correições virtuais.', 'E', 'A CGJ implementará, gradativamente, a correição virtual.',
  alt='São vedadas correições virtuais.', orig='A Corregedoria Geral da Justiça implementará, gradativamente, a correição virtual', tags=['literal'], qc='Q3252528', letra='E')
q('NS-008-01', G5, 'NSCGJ, art. 8º', ['n8'], 'A correição ordinária é feita uma vez por ano, de preferência em dezembro, anunciada por edital com pelo menos 15 dias de antecedência.', 'C', 'Art. 8º, caput e § 1º.', tags=['literal'], qc='Q2176757', letra='C')
q('NS-008-02', G5, 'NSCGJ, art. 8º', ['n8'], 'A correição ordinária será realizada uma vez por ano, de preferência no mês de fevereiro.', 'E', 'De preferência em DEZEMBRO.',
  alt='no mês de fevereiro', orig='de preferência no mês de dezembro', tags=['literal'], qc='Q3174072', letra='C')
q('NS-006-04', G5, 'NSCGJ, art. 6º, § 2º', ['n6'], 'A correição extraordinária é realizada a qualquer momento, com prévio anúncio, e pode ser geral ou parcial.', 'E', '"SEM prévio anúncio".',
  alt='com prévio anúncio', orig='realizada a qualquer momento e sem prévio anúncio', tags=['literal'], qc='Q3174072', letra='D')
q('NS-010-01', G5, 'NSCGJ, art. 10', ['n8'], 'O escrivão auxiliará o Juiz Corregedor Permanente nas diligências correcionais, vedada a nomeação de escrivão ad hoc.', 'E', '"FACULTADA a nomeação de escrivão ad hoc".',
  alt='vedada a nomeação de escrivão ad hoc', orig='facultada a nomeação de escrivão ‘ad hoc’', tags=['literal'], qc='Q3174072', letra='A')
q('NS-007-01', G5, 'NSCGJ, art. 7º, § 1º', ['n6'], 'O Corregedor Geral da Justiça, após consulta ao Presidente do Tribunal, pode alterar a designação do Corregedor Permanente.', 'E',
  'Com APROVAÇÃO DO CONSELHO SUPERIOR DA MAGISTRATURA.', alt='após consulta ao Presidente do Tribunal', orig='com aprovação do Conselho Superior da Magistratura', tags=['literal'], qc='Q3174072', letra='E')
q('NS-015-01', G5, 'NSCGJ, art. 15, I e § 1º', ['n15'], 'Falta que pode gerar suspensão, sem autoria definida, é apurada por apuração preliminar instaurada por portaria.', 'C',
  'Sem autoria definida → apuração preliminar (por portaria; só dispensa a identificação do servidor).', tags=['caso-concreto'], qc='Q3174073', letra='D')
q('NS-015-02', G5, 'NSCGJ, art. 15', ['n15'], 'Falta que pode gerar suspensão, sem autoria definida, deve ser apurada por sindicância instaurada por resolução.', 'E',
  'Apuração PRELIMINAR (autoria indefinida), instaurada por PORTARIA.', alt='por sindicância instaurada por resolução', orig='Apuração preliminar: quando a infração não estiver suficientemente caracterizada ou definida a autoria', tags=['caso-concreto'], qc='Q3174073', letra='A/B/C')
q('NS-015-03', G5, 'NSCGJ, art. 15, § 6º', ['n15'], 'Os prazos dos procedimentos disciplinares contam-se em dias corridos e ficam suspensos de 20 de dezembro a 20 de janeiro.', 'C', 'Literal.', tags=['literal'])

# G6
q('NS-082-01', G6, 'NSCGJ, art. 82, IV', ['n81'], 'Na escrituração, é vedado usar chancela ou qualquer recurso que reproduza mecanicamente a assinatura do juiz.', 'C', 'Literal.', tags=['literal'], qc='Q3252529', letra='D')
q('NS-082-02', G6, 'NSCGJ, art. 82, III', ['n81'], 'Na escrituração, é vedado em qualquer hipótese o uso de abreviaturas, siglas ou símbolos.', 'E',
  'Exceto as formas do VOLP, as adotadas por órgãos oficiais e as convencionadas por área do conhecimento.', alt='em qualquer hipótese', orig='excetuando-se as formas consagradas', tags=['literal'], qc='Q3252529', letra='A')
q('NS-084-01', G6, 'NSCGJ, art. 84', ['n81'], 'Ofícios e demais atos conterão o nome e o cargo da autoridade judiciária, sendo facultativa a identificação dos servidores que os lavram.', 'E',
  'Conterão o nome completo e o cargo da autoridade E DOS SERVIDORES que os lavrem, confiram e subscrevam.', alt='sendo facultativa a identificação dos servidores', orig='da autoridade judiciária e dos servidores que os lavrem, confiram e subscrevam', tags=['literal'], qc='Q3252529', letra='E')
q('NS-085-01', G6, 'NSCGJ, art. 85, § 1º, II', ['n85'], 'É obrigatória a assinatura do juiz no documento que determina desconto de pensão alimentícia.', 'C', 'Literal.', tags=['literal'], qc='Q2176758', letra='A')
q('NS-085-02', G6, 'NSCGJ, art. 85, § 1º, II', ['n85'], 'O ofício que determina desconto de pensão alimentícia pode ser assinado pelo escrivão.', 'E', 'Exige subscrição do JUIZ.',
  alt='pode ser assinado pelo escrivão', orig='houver determinação de desconto de pensão alimentícia', tags=['literal'], qc='Q3252529', letra='B')
q('NS-085-03', G6, 'NSCGJ, art. 85, § 1º, III', ['n85'], 'César, escrevente, pode assinar ofício ao Prefeito com ordem judicial de fornecer notas fiscais, por ser mera comunicação de decisão já assinada pelo juiz.', 'E',
  'Documento dirigido a AUTORIDADE (chefe do Poder Executivo) exige assinatura do JUIZ.', alt='pode assinar ofício ao Prefeito', orig='os documentos ou papéis forem dirigidos a autoridades', tags=['caso-concreto'], qc='Q3769026', letra='A/E')
q('NS-085-04', G6, 'NSCGJ, art. 85, § 1º, III', ['n85'], 'Documentos dirigidos a membros do Ministério Público podem ser assinados pelo escrivão, por ordem do juiz.', 'E', 'Dirigidos a autoridades → assinatura do JUIZ obrigatória.',
  alt='podem ser assinados pelo escrivão', orig='os documentos ou papéis forem dirigidos a autoridades', tags=['literal'], qc='Q2176758', letra='C')
q('NS-085-05', G6, 'NSCGJ, art. 85, § 2º', ['n85'], 'A emissão de cartas postais depende sempre da assinatura do escrivão ou de escrevente.', 'E',
  '"INDEPENDERÃO da assinatura", desde que conste nome e cargo do emitente e não haja ordem contrária.', alt='depende sempre da assinatura', orig='independerão da assinatura do escrivão ou escreventes', tags=['literal'], qc='Q3252529', letra='C')
q('NS-081-01', G6, 'NSCGJ, art. 81, II', ['n81'], 'Havendo equívoco na escrituração, recomenda-se lançar a anotação "sem efeito" seguida da redação correta.', 'E',
  'Anotações de "sem efeito" devem ser EVITADAS (art. 81, II).', alt='recomenda-se lançar a anotação "sem efeito"', orig='Na escrituração serão evitadas as seguintes práticas:', tags=['literal'], qc='Q2176758', letra='E')
q('NS-049-01', G6, 'NSCGJ, arts. 49 e 53', ['n49'], 'É vedado ao funcionário credenciado ceder sua senha do SAJ, e a inserção de dados no sistema será a mais completa possível, formando memória permanente.', 'C', 'Art. 49, § 1º, e art. 53.', tags=['literal'], qc='Q3252532', letra='E')
q('NS-051-01', G6, 'NSCGJ, art. 51', ['n49'], 'Os escrivães realizarão auditoria mensal no sistema informatizado.', 'E', 'Auditoria SEMANAL.',
  alt='auditoria mensal', orig='auditoria semanal', tags=['literal'], qc='Q3252532', letra='A')
q('NS-061-01', G6, 'NSCGJ, art. 61, § 2º', ['n49'], 'O segredo de justiça não pode ser gerado automaticamente pelo sistema.', 'E', 'Pode ser gerado automaticamente, conforme a natureza da ação.',
  alt='não pode ser gerado automaticamente', orig='O segredo de justiça poderá, ainda, ser gerado automaticamente', tags=['literal'], qc='Q3252532', letra='B')
q('NS-057-01', G6, 'NSCGJ, art. 57', ['n49'], 'O controle da movimentação dos feitos é feito preferencialmente pelo sistema, admitidas fichas em papel por ordem do juiz.', 'E',
  'EXCLUSIVAMENTE pelo sistema; VEDADAS as fichas.', alt='preferencialmente pelo sistema, admitidas fichas em papel', orig='exclusivamente pelo sistema informatizado oficial, vedadas a elaboração de fichário', tags=['literal'], qc='Q3252532', letra='C')
q('NS-062-01', G6, 'NSCGJ, art. 62', ['n49'], 'Retificados os dados de uma parte, a correção se aplica também aos processos dela em outros ofícios de justiça.', 'E', '"NÃO serão aplicadas aos feitos de outro juízo".',
  alt='se aplica também aos processos dela em outros ofícios', orig='não serão aplicadas aos feitos de outro juízo', tags=['literal'], qc='Q3252532', letra='D')
q('NS-055-01', G6, 'NSCGJ, art. 55, § 3º', ['n49'], 'A testemunha de processo criminal que relata coação ou grave ameaça pode, com deferimento do juiz, não ter lançados no sistema seus dados de qualificação e endereço.', 'C',
  'Vale para testemunhas de acusação, defesa ou comuns, e para vítimas.', tags=['caso-concreto'], qc='Q3174074', letra='C')
q('NS-055-02', G6, 'NSCGJ, art. 55, § 3º', ['n49'], 'Só as testemunhas de acusação podem ter seus dados omitidos do sistema por receio de coação.', 'E', 'Testemunhas "de acusação, defesa ou comuns".',
  alt='Só as testemunhas de acusação', orig='sejam estas de acusação, defesa ou comuns', tags=['literal'], qc='Q3174074', letra='A')

# G7
q('NS-104-01', G7, 'NSCGJ, art. 104, § 2º', ['n104'], 'As certidões são expedidas em 5 dias do recebimento do pedido pelo ofício de justiça, com protocolo ao interessado.', 'C', 'Literal.', tags=['literal'], qc='Q3174075', letra='A')
q('NS-104-02', G7, 'NSCGJ, art. 104, § 5º', ['n104'], 'A certidão de processo em segredo de justiça depende sempre de despacho do juiz, após parecer do Ministério Público.', 'E',
  'Depende de despacho, EXCETO se requerida por parte ou procurador habilitado; não há parecer do MP.', alt='depende sempre de despacho do juiz, após parecer do Ministério Público', orig='exceto se requerida por parte ou procurador regularmente habilitado nos autos', tags=['literal'], qc='Q3174075', letra='C/E')
q('NS-104-03', G7, 'NSCGJ, art. 104, § 3º', ['n104'], 'Não são admitidos pedidos de certidão de objeto e pé por e-mail institucional entre ofícios de justiça.', 'E', 'São atendidos em 5 dias ÚTEIS.',
  alt='Não são admitidos', orig='Serão atendidos em 5 (cinco) dias úteis os pedidos de certidões de objeto e pé', tags=['literal'], qc='Q3174075', letra='D')
q('NS-164-01', G7, 'NSCGJ, art. 164, § 2º', ['n157'], 'Em prazo comum, cada procurador pode retirar os autos para cópia por 2 a 6 horas, independentemente de ajuste, até o fim do expediente.', 'C', 'Literal.', tags=['literal'], qc='Q2176756', letra='A')
q('NS-157-01', G7, 'NSCGJ, art. 157', ['n157'], 'O acesso aos autos não sigilosos é assegurado só a advogados e estagiários com procuração, vedado ao público em geral.', 'E',
  'É assegurado, mesmo sem procuração, a advogados, estagiários E AO PÚBLICO EM GERAL, no balcão.', alt='só a advogados e estagiários com procuração, vedado ao público em geral', orig='mesmo sem procuração, quando não estejam sujeitos a segredo de justiça, é assegurado aos advogados, estagiários de Direito e ao público em geral', tags=['literal'], qc='Q2176756', letra='B')
q('NS-164-02', G7, 'NSCGJ, art. 164', ['n157'], 'Não havendo prazo em curso, a parte pode retirar os autos em carga independentemente de requerimento.', 'E', 'Só "MEDIANTE REQUERIMENTO".',
  alt='independentemente de requerimento', orig='os autos somente serão retirados em carga mediante requerimento', tags=['literal'], qc='Q2176756', letra='D')
q('NS-166-01', G7, 'NSCGJ, art. 166', ['n157'], 'É permitido reter o documento do advogado no cartório para controle da carga rápida.', 'E', 'É VEDADA a retenção, em qualquer modalidade.',
  alt='É permitido reter', orig='É vedada a retenção do documento de identificação do advogado', tags=['literal'], qc='Q2176756', letra='E')
q('NS-178-01', G7, 'NSCGJ, art. 178', ['n176'], 'Se o cumprimento de sentença correu em Campinas e o processo em Várzea Paulista, o arquivamento é promovido pelo juízo da execução (Campinas).', 'C', 'Literal (art. 178).', tags=['caso-concreto'], qc='Q3252531', letra='C')
q('NS-182-01', G7, 'NSCGJ, art. 182, parágrafo único', ['n176'], 'Desarquivado processo que correu em segredo de justiça, a extração de cópia depende de despacho do juiz competente.', 'C', 'Literal.', tags=['caso-concreto'], qc='Q3252531', letra='A')
q('NS-180-01', G7, 'NSCGJ, art. 180', ['n176'], 'O advogado pode retirar o processo diretamente nos depósitos do Arquivo Terceirizado.', 'E', '"Fica VEDADA às partes e advogados a consulta ou retirada".',
  alt='pode retirar o processo diretamente', orig='Fica vedada às partes e advogados a consulta ou retirada', tags=['literal'], qc='Q3252531', letra='D')
q('NS-181-01', G7, 'NSCGJ, art. 181, parágrafo único', ['n176'], 'O interessado no desarquivamento será intimado da chegada dos autos e do prazo de 15 dias para manifestação.', 'E', 'Prazo de 30 (trinta) dias.',
  alt='prazo de 15 dias', orig='prazo de 30 (trinta) dias para manifestação', tags=['literal'], qc='Q3252531', letra='B')
q('NS-188-01', G7, 'NSCGJ, art. 188', ['n176'], 'O desarquivamento, em regra, dispensa recolhimento de taxa.', 'E', 'Instruído com o comprovante da TAXA, ressalvadas as exceções legais.',
  alt='dispensa recolhimento de taxa', orig='serão instruídos com o comprovante de recolhimento da respectiva taxa', tags=['literal'], qc='Q3252531', letra='E')
q('NS-177-01', G7, 'NSCGJ, art. 177', ['n176'], 'Publicada a decisão que determinou o arquivamento, o processo fica 30 dias no ofício de justiça antes de ser arquivado.', 'C', 'Literal.', tags=['literal'])

# G8
q('NS-1220-01', G8, 'NSCGJ, art. 1.220, parágrafo único', ['n1220'], 'Materializado o processo eletrônico, passam a ser admitidas petições em papel; retomada a tramitação eletrônica, não mais.', 'C', 'Literal.', tags=['literal'], qc='Q3252530', letra='C')
q('NS-1221-01', G8, 'NSCGJ, art. 1.221, § 1º', ['n1220'], 'Recebida indevidamente petição em papel para processo eletrônico, o protocolo cancela o registro e intima o peticionário por carta.', 'E',
  'A intimação é pelo DIÁRIO DA JUSTIÇA ELETRÔNICO.', alt='intima o peticionário por carta', orig='intimar o peticionário pelo Diário da Justiça Eletrônico', tags=['literal'], qc='Q3252530', letra='B')
q('NS-1221-02', G8, 'NSCGJ, art. 1.221, § 1º', ['n1220'], 'Se o setor de protocolo verificar, antes do cadastramento, petição física indevida em processo eletrônico, cancelará o protocolo e intimará o peticionário.', 'C', 'Literal.', tags=['literal'], qc='Q2176754', letra='B')
q('NS-1220-02', G8, 'NSCGJ, art. 1.220', ['n1220'], 'Mesmo em processo eletrônico, a parte pode optar por peticionar em papel.', 'E', 'Petições intermediárias são apresentadas por PETICIONAMENTO ELETRÔNICO.',
  alt='a parte pode optar por peticionar em papel', orig='As petições intermediárias serão apresentadas pelo peticionamento eletrônico', tags=['literal'], qc='Q2176754', letra='E')
q('NS-1221-03', G8, 'NSCGJ, art. 1.221, § 2º', ['n1220'], 'Nos foros digitais, não se admite protocolo integrado de petições em papel para processos físicos de outras comarcas.', 'E', '"ADMITIR-SE-Á" o protocolo integrado.',
  alt='não se admite protocolo integrado', orig='Admitir-se-á, nos Foros Digitais, o protocolo integrado', tags=['literal'], qc='Q2176754', letra='C')
q('NS-1222-01', G8, 'NSCGJ, art. 1.222, § 3º', ['n1220'], 'Recebida petição em papel por indisponibilidade do sistema, o requerente terá 45 dias da digitalização para retirá-la, sob pena de inutilização.', 'C', 'Quem digitaliza é o ofício de justiça, não a parte.', tags=['literal'], qc='Q3252530', letra='E')
q('NS-1238-01', G8, 'NSCGJ, art. 1.238, § 3º', ['n1237'], 'Sempre que cabível, para permitir trabalho em lote e filtros nas filas, devem ser usados modelos de grupo.', 'C', 'Literal.', tags=['literal'], qc='Q2176755', letra='C')
q('NS-1237-01', G8, 'NSCGJ, art. 1.237', ['n1237'], 'Os modelos institucionais de expedientes do processo eletrônico são autorizados e homologados pelo Juiz Diretor do Foro.', 'E', 'Autorizados e aprovados pela CORREGEDORIA GERAL DA JUSTIÇA.',
  alt='pelo Juiz Diretor do Foro', orig='autorizados e aprovados pela Corregedoria Geral da Justiça', tags=['literal'], qc='Q2176755', letra='A')

# ===== v2.7: Regimento (texto de 12/11/2026) e NSCGJ (Cap. III e XI) =====
G9 = 'Regimento Interno: organização e órgãos'; G10 = 'Normas CGJ: rotinas do ofício de justiça'; G11 = 'Normas CGJ: intimações e audiências'
MR = ['literal', 'mudanca-recente']
# G4 — complementos (sessões, sustentação, votação, acórdão, agravo)
q('RI-134-02', G4, 'RITJSP, art. 134, § 1º', ['ri134'], 'A ausência do revisor que ainda não votou acarreta o adiamento do julgamento, salvo se o afastamento for superior a 40 dias, quando será substituído.', 'C', 'Redação do AR 587/2023, que também prevê a substituição, no julgamento virtual, do vogal que ainda não votou.', tags=MR)
q('RI-134-03', G4, 'RITJSP, art. 134, § 2º', ['ri134'], 'A ausência ocasional de vogal sempre acarreta o adiamento do julgamento convertido de virtual para presencial.', 'E',
  'Não acarreta adiamento, "inclusive em julgamento presencial fruto de conversão de julgamento iniciado virtualmente", se possível a substituição.', alt='sempre acarreta o adiamento', orig='A ausência ocasional de vogal não acarretará adiamento', tags=MR)
q('RI-146-01', G4, 'RITJSP, art. 146, II', ['ri146'], 'Adotada a inscrição prévia por e-mail, o pedido de sustentação oral deve ser feito com antecedência mínima de 24 horas da hora prevista para o início da sessão.', 'C', 'Redação do AR 588/2023.', tags=MR)
q('RI-146-02', G4, 'RITJSP, art. 146, II', ['ri146'], 'Adotada a inscrição prévia por e-mail, o pedido de sustentação oral deve ser feito com antecedência mínima de 48 horas do início da sessão.', 'E', 'Antecedência mínima de 24 HORAS.',
  alt='48 horas', orig='antecedência mínima de 24 horas', tags=MR)
q('RI-146-03', G4, 'RITJSP, art. 146, § 4º', ['ri146'], 'Não há sustentação oral no julgamento de embargos de declaração, incidente de suspeição e conflito de competência.', 'C', 'Nem em agravo, salvo o de instrumento sobre tutelas provisórias e o interno do art. 937, VI, do CPC.', tags=['literal'])
q('RI-146-04', G4, 'RITJSP, art. 146, § 4º', ['ri146'], 'É vedada a sustentação oral em qualquer agravo.', 'E',
  'Exceto no agravo de instrumento sobre tutelas provisórias de urgência ou da evidência e no agravo interno contra extinção de feito originário (art. 937, VI, CPC).', alt='em qualquer agravo', orig='exceto no de instrumento referente às tutelas provisórias', tags=['literal'])
q('RI-146-05', G4, 'RITJSP, art. 146, § 4º-A', ['ri146'], 'No agravo em execução penal, a sustentação oral não excederá cinco minutos.', 'C', 'Incluído pelo AR 585/2023.', tags=MR)
q('RI-146-06', G4, 'RITJSP, art. 146, § 5º', ['ri146'], 'A sustentação oral por videoconferência deve ser requerida até o início da sessão de julgamento.', 'E', 'Até o DIA ANTERIOR ao da sessão.',
  alt='até o início da sessão de julgamento', orig='desde que o advogado a requeira até o dia anterior ao da sessão', tags=['literal'])
q('RI-146-07', G4, 'RITJSP, art. 146, § 3º', ['ri146'], 'A sustentação oral não admite interrupções ou apartes, e o presidente pode cassar a palavra do orador em caso de reiteração de incontinência de conduta ou linguagem.', 'C', 'Primeiro adverte; cassa na reiteração.', tags=['literal'])
q('RI-147-01', G4, 'RITJSP, art. 147', ['ri147'], 'Havendo mais de uma sustentação oral em recurso, fala primeiro o recorrente e, por último, o Ministério Público, quando não for recorrente.', 'C', 'Nos feitos originários, fala primeiro o autor ou impetrante.', tags=['literal'])
q('RI-149-01', G4, 'RITJSP, art. 149', ['ri147'], 'Representada a parte por mais de um advogado, cada um terá o tempo integral da sustentação oral.', 'E', 'O tempo SE DIVIDIRÁ entre eles, salvo ajuste diverso.',
  alt='cada um terá o tempo integral', orig='o tempo se dividirá entre eles', tags=['literal'])
q('RI-153-01', G4, 'RITJSP, art. 153', ['ri152'], 'O Presidente do Tribunal não vota nas sessões que preside, salvo em matéria constitucional, para desempate em qualquer matéria e quando for relator nato.', 'C', 'Literal.', tags=['literal'])
q('RI-152-01', G4, 'RITJSP, art. 152', ['ri152'], 'Após os votos do relator e do revisor, se houver, os demais julgadores votam do mais moderno para o mais antigo.', 'E', 'Votam "em ordem de ANTIGUIDADE".',
  alt='do mais moderno para o mais antigo', orig='serão tomados os votos dos demais julgadores em ordem de antiguidade', tags=['literal'])
q('RI-144-01', G4, 'RITJSP, art. 144, IV', ['ri144'], 'Tem preferência o julgamento com pedido de preferência apresentado até o início da sessão, presente advogado ou estagiário.', 'C', 'Também os com magistrado convocado, os adiados e aqueles com MP, Procurador do Estado ou sustentação oral.', tags=['literal'])
q('RI-155-01', G4, 'RITJSP, art. 155', ['ri155'], 'Vencido o relator no mérito, ainda que em parte, o acórdão será redigido pelo desembargador designado, preferencialmente o que primeiro expôs a tese vencedora.', 'C', 'Art. 155, caput e § 1º.', tags=['literal'])
q('RI-155-02', G4, 'RITJSP, art. 155, § 2º', ['ri155'], 'Publicado o acórdão, cessa a vinculação do relator designado, salvo quanto aos embargos de declaração, aos infringentes no processo criminal e ao reexame do art. 1.040, II, do CPC.', 'C', 'Redação do AR 591/2025.', tags=MR)
q('RI-160-01', G4, 'RITJSP, art. 160', ['ri155'], 'Se o redator do acórdão se aposentar sem assiná-lo, o acórdão será assinado pelo presidente da sessão.', 'E',
  'Assina o desembargador que, com voto vencedor, o seguiu IMEDIATAMENTE NA ORDEM DE VOTAÇÃO.', alt='será assinado pelo presidente da sessão', orig='caberá fazê-lo o desembargador que, com voto vencedor, o seguiu imediatamente na ordem de votação', tags=['literal'])
q('RI-163-01', G4, 'RITJSP, art. 163', ['ri155'], 'As conclusões do acórdão são publicadas no órgão oficial, para intimação, nos cinco dias seguintes ao registro.', 'C', 'Literal.', tags=['literal'])
q('RI-253-01', G4, 'RITJSP, art. 253', ['ri253'], 'Das decisões monocráticas que possam causar prejuízo ao direito da parte cabe agravo, com efeito suspensivo, em cinco dias.', 'E', 'SEM efeito suspensivo, no prazo de QUINZE dias.',
  alt='com efeito suspensivo, em cinco dias', orig='cabe agravo, sem efeito suspensivo, no prazo de quinze dias', tags=['literal'])
q('RI-255-01', G4, 'RITJSP, art. 255', ['ri253'], 'Mantida a decisão agravada, o prolator coloca o feito em mesa, independentemente de inclusão em pauta, proferindo voto.', 'C', 'Pode antes reconsiderar.', tags=['literal'])
q('RI-254-01', G4, 'RITJSP, art. 254', ['ri253'], 'Faltando peça no agravo, o relator concederá cinco dias ao agravante para complementar a documentação.', 'C', 'Em processo eletrônico, as peças obrigatórias são dispensadas (§ 2º).', tags=['literal'])
q('RI-141-01', G4, 'RITJSP, art. 141', ['ri134'], 'O desembargador pode modificar seu voto até a publicação do acórdão.', 'E', 'Até a PROCLAMAÇÃO DO RESULTADO.',
  alt='até a publicação do acórdão', orig='até a proclamação do resultado', tags=['literal'])
q('RI-108-01', G4, 'RITJSP, arts. 108 e 109', ['ri108'], 'É juiz certo o desembargador com visto nos autos, mas deixa de sê-lo se se afastar por mais de 60 dias depois do visto.', 'C', 'Art. 108, I (AR 587/2023) e art. 109.', tags=['literal'])
q('RI-105-01', G4, 'RITJSP, art. 105, § 1º', ['ri105'], 'O afastamento dos juízes que participaram do julgamento anterior rompe a prevenção da Câmara.', 'E', '"NÃO rompe a prevenção": o processo vai a quem os substituir ou assumir a cadeira.',
  alt='rompe a prevenção', orig='não rompe a prevenção', tags=['literal'])
q('RI-106-01', G4, 'RITJSP, art. 106', ['ri105'], 'O julgamento de agravo em execução penal só determina a prevenção para incidentes do processo em que foi interposto.', 'C', 'Literal.', tags=['literal'])
q('RI-113-01', G4, 'RITJSP, art. 113', ['ri113'], 'Da decisão do Presidente que arquiva petição de suspeição manifestamente inconsistente cabe agravo interno para o Órgão Especial.', 'C', 'Literal.', tags=['literal'])
# G9 — organização
q('RI-002-01', G9, 'RITJSP, art. 2º, VI-A', ['ri2'], 'A Ouvidoria passou a figurar entre os órgãos que compõem o Tribunal de Justiça.', 'C', 'Inciso VI-A incluído pelo AR 589/2024.', tags=MR)
q('RI-004-01', G9, 'RITJSP, art. 4º', ['ri4'], 'Compete ao Tribunal Pleno eleger o Presidente, o Vice-Presidente, o Corregedor Geral da Justiça e doze desembargadores do Órgão Especial.', 'C', 'Literal.', tags=['literal'])
q('RI-008-01', G9, 'RITJSP, art. 8º', ['ri4'], 'O Órgão Especial é constituído por trinta desembargadores.', 'E', 'VINTE E CINCO desembargadores (12 eleitos pelo Pleno).',
  alt='trinta desembargadores', orig='constituído por vinte e cinco desembargadores', tags=['literal'])
q('RI-011-01', G9, 'RITJSP, art. 11', ['ri4'], 'O Órgão Especial instala-se com a presença de, no mínimo, treze desembargadores.', 'C', 'Maioria absoluta de 25.', tags=['literal'])
q('RI-015-01', G9, 'RITJSP, art. 15', ['ri15'], 'O Conselho Superior da Magistratura é composto pelo Presidente, Vice-Presidente, Corregedor Geral, Decano e Presidentes das Seções; no empate, prevalece o voto do presidente do Conselho.', 'C', 'Art. 15, caput e § 2º.', tags=['literal'])
q('RI-015-02', G9, 'RITJSP, art. 15', ['ri15'], 'O Conselho Superior da Magistratura é presidido pelo Corregedor Geral da Justiça.', 'E', 'É presidido pelo PRESIDENTE DO TRIBUNAL.',
  alt='presidido pelo Corregedor Geral da Justiça', orig='composto pelo Presidente do Tribunal, que o preside', tags=['literal'])
q('RI-016-01', G9, 'RITJSP, art. 16, XIII', ['ri15'], 'Compete ao Conselho Superior da Magistratura julgar os recursos de candidatos aos concursos para cargos do quadro de servidores da Justiça.', 'C', 'Também julga as dúvidas dos Registros Públicos e aprecia suspeição por foro íntimo de juiz de 1º grau.', tags=['literal'])
q('RI-016-02', G9, 'RITJSP, art. 16, XV', ['ri15'], 'A suspensão do expediente forense nos feriados municipais das comarcas do interior é aprovada pelo Órgão Especial.', 'E', 'Compete ao CONSELHO SUPERIOR DA MAGISTRATURA.',
  alt='é aprovada pelo Órgão Especial', orig='aprovar a suspensão do expediente forense nos feriados municipais', tags=['literal'])
q('RI-017-01', G9, 'RITJSP, arts. 17 e 22', ['ri17'], 'A eleição do Presidente, Vice-Presidente e Corregedor Geral ocorre na segunda quarta-feira de novembro do ano em que findam os mandatos, por votação secreta.', 'C', 'Arts. 17 e 22.', tags=['literal'])
q('RI-019-01', G9, 'RITJSP, art. 19, § 3º', ['ri17'], 'Havendo empate na eleição para cargo de direção, vence o candidato mais idoso.', 'E', 'Vence o MAIS ANTIGO.',
  alt='vence o candidato mais idoso', orig='será considerado vencedor o mais antigo', tags=['literal'])
q('RI-021-01', G9, 'RITJSP, art. 21, parágrafo único', ['ri17'], 'Vagando cargo de direção quando restam menos de seis meses de mandato, não há eleição: ocorre substituição pela ordem regimental.', 'C', 'Literal.', tags=['literal'])
q('RI-024-01', G9, 'RITJSP, art. 24', ['ri24'], 'Nas ausências, o Presidente do Tribunal é substituído pelo Corregedor Geral da Justiça.', 'E', 'Pelo VICE-PRESIDENTE e, na falta, pelo DECANO.',
  alt='substituído pelo Corregedor Geral da Justiça', orig='o Presidente é substituído pelo Vice-Presidente e, na falta, pelo Decano', tags=['literal'])
q('RI-029A-01', G9, 'RITJSP, art. 29-A', ['ri29a'], 'O Ouvidor e seu substituto são eleitos pelo Órgão Especial, para dois anos coincidentes com o mandato do Presidente, permitida uma reeleição.', 'C', 'Vedados mais de 4 anos consecutivos (§ 5º) e a acumulação com cargos diretivos e de juiz assessor (§ 2º).', tags=MR)
q('RI-029A-02', G9, 'RITJSP, art. 29-A', ['ri29a'], 'O Ouvidor do TJSP é eleito pelo Tribunal Pleno para mandato de quatro anos.', 'E', 'Eleito pelo ÓRGÃO ESPECIAL, para 2 anos (uma reeleição).',
  alt='eleito pelo Tribunal Pleno para mandato de quatro anos', orig='serão eleitos pelo Órgão Especial, para o período de 2 (dois) anos', tags=MR)
q('RI-033-01', G9, 'RITJSP, art. 33', ['ri33'], 'A Câmara Especial, presidida pelo Vice-Presidente e integrada pelos Presidentes das Seções e pelo Decano, julga os processos e recursos de Infância e Juventude.', 'C', 'E as suspeições e impedimentos de juiz de 1º grau.', tags=['literal'])
q('RI-033A-01', G9, 'RITJSP, art. 33-A', ['ri33'], 'A Câmara Especial de Presidentes é presidida pelo Vice-Presidente do Tribunal.', 'E', 'É presidida pelo PRESIDENTE DO TRIBUNAL. Quem preside a Câmara Especial é o Vice.',
  alt='presidida pelo Vice-Presidente do Tribunal', orig='integrada pelo Presidente do Tribunal, que a presidirá', tags=['literal'])
q('RI-063-01', G9, 'RITJSP, art. 63', ['ri62'], 'Não podem integrar a mesma Câmara parentes na linha colateral até o terceiro grau, inclusive.', 'C', 'Também cônjuges, conviventes e parentes em linha reta.', tags=['literal'])
q('RI-062-01', G9, 'RITJSP, art. 62, § 1º', ['ri62'], 'A antiguidade no Tribunal conta-se da posse; no empate, prevalece a maior idade.', 'E', 'Empate: antiguidade na entrância anterior, depois na carreira e, só então, maior idade.',
  alt='no empate, prevalece a maior idade', orig='havendo empate, prevalecerá a antiguidade na entrância anterior', tags=['literal'])
# G10 — rotinas do ofício
q('NS-033-01', G10, 'NSCGJ, art. 33', ['n30'], 'Os servidores registrarão diariamente, na entrada e na saída, o ponto biométrico, salvo exceções definidas pela Presidência do Tribunal.', 'C', 'Literal.', tags=['literal'])
q('NS-034-01', G10, 'NSCGJ, art. 34, parágrafo único', ['n30'], 'Os documentos que geram regularizações do ponto ficam arquivados na unidade por dois anos e depois são inutilizados.', 'E', 'Por CINCO anos; depois são ENTREGUES AO SERVIDOR para guarda.',
  alt='por dois anos e depois são inutilizados', orig='pelo prazo de cinco anos, findo o qual serão entregues ao servidor', tags=['literal'])
q('NS-032-01', G10, 'NSCGJ, art. 32, III', ['n30'], 'O escrivão deve abrir a caixa de e-mails do ofício pelo menos uma vez no início e uma vez antes do término dos trabalhos.', 'C', 'E consultar diariamente o DJE (inciso II).', tags=['literal'])
q('NS-087-01', G10, 'NSCGJ, art. 87', ['n87'], 'Recebida a petição inicial ou a denúncia, o ofício de justiça providenciará a autuação em 48 horas.', 'E', 'Em 24 (vinte e quatro) horas.',
  alt='em 48 horas', orig='em 24 (vinte e quatro) horas, a autuação', tags=['literal'])
q('NS-089-01', G10, 'NSCGJ, art. 89', ['n87'], 'Cada volume dos autos não excederá 200 folhas, salvo determinação judicial ou para manter peça com seus documentos anexos.', 'C', 'Literal.', tags=['literal'])
q('NS-091-01', G10, 'NSCGJ, art. 91, § 1º', ['n87'], 'Constatado erro na numeração das folhas, o escrevente deve renumerar os autos e certificar.', 'E', 'Certifica-se a ocorrência, VEDADA a renumeração; na repetida, acrescenta-se letra (188-a).',
  alt='deve renumerar os autos', orig='sendo vedada a renumeração', tags=['literal'])
q('NS-092-01', G10, 'NSCGJ, art. 92, I', ['n92'], 'O ofício de justiça pode receber diretamente do interessado petição de juntada de procuração ou substabelecimento, mencionando essa circunstância no termo de juntada.', 'C', 'Exceção à regra do protocolo.', tags=['caso-concreto'])
q('NS-093-01', G10, 'NSCGJ, art. 93, §§ 1º e 2º', ['n92'], 'Juntadas na mesma oportunidade duas ou mais petições, lavra-se um termo para cada uma, podendo ser lançado na própria petição.', 'E', 'UM ÚNICO termo com a relação das peças; é VEDADO lançá-lo na própria petição.',
  alt='lavra-se um termo para cada uma', orig='será confeccionado um único termo de juntada', tags=['literal'])
q('NS-096-01', G10, 'NSCGJ, art. 96', ['n92'], 'Constatada cota marginal ou interlinear nos autos, o serventuário deve comunicá-la imediatamente ao juiz.', 'C', 'Também sublinhar palavras ou usar expressões injuriosas.', tags=['literal'])
q('NS-097-01', G10, 'NSCGJ, art. 97', ['n97'], 'A conclusão dos autos é feita em 1 dia e os atos processuais executados em 5 dias.', 'C', 'Mesmos prazos do art. 228 do CPC.', tags=['literal'])
q('NS-099-01', G10, 'NSCGJ, art. 99', ['n97'], 'Aguardando resposta a ofício há mais de 30 dias, o ofício de justiça reiterará a diligência quantas vezes forem necessárias antes de abrir conclusão.', 'E', 'Reitera UMA ÚNICA VEZ; sem atendimento, conclusão ao juiz.',
  alt='quantas vezes forem necessárias', orig='reiterará a diligência uma única vez', tags=['literal'])
q('NS-098-01', G10, 'NSCGJ, art. 98, § 5º', ['n97'], 'A conclusão dos autos ao juiz é feita diariamente, limitada a 30 processos por dia.', 'E', '"Sem limitação de número".',
  alt='limitada a 30 processos por dia', orig='sem limitação de número', tags=['literal'])
q('NS-100-01', G10, 'NSCGJ, art. 100, VI', ['n100'], 'Processos de réu preso paralisados há mais de 3 meses são levados à análise do juiz, que informará a Corregedoria Geral por relatório.', 'C', 'Literal.', tags=['literal'])
q('NS-171-01', G10, 'NSCGJ, art. 171', ['n170'], 'Não haverá substituição por cópia do documento desentranhado que se refira a manifestação intempestiva do peticionário.', 'C', 'Também documentação estranha aos autos ou que não serviu de base a decisão.', tags=['literal'])
q('NS-172-01', G10, 'NSCGJ, art. 172, III', ['n170'], 'Desentranhado o documento, o interessado será intimado a retirá-lo em 10 dias, se outro prazo não fixar o juiz.', 'E', 'Prazo de 5 (cinco) dias.',
  alt='em 10 dias', orig='no prazo de 5 (cinco) dias', tags=['literal'])
q('NS-174-01', G10, 'NSCGJ, art. 174', ['n170'], 'Transitada em julgado a sentença, os objetos anexados serão devolvidos mediante solicitação ou intimação para retirada em até 30 dias, sob pena de destruição.', 'C', 'Literal.', tags=['literal'])
# G11 — intimações e audiências
q('NS-132-01', G11, 'NSCGJ, art. 132, parágrafo único', ['n132'], 'O servidor do ofício de justiça pode informar por telefone aos advogados o teor dos despachos já publicados.', 'E', 'É VEDADO prestar informações por telefone sobre atos e termos do processo.',
  alt='pode informar por telefone', orig='É vedado ao servidor dos ofícios de justiça prestar informações por telefone', tags=['literal'])
q('NS-133-01', G11, 'NSCGJ, art. 133', ['n132'], 'Despachos, decisões e sentenças devem ser encaminhados à publicação no DJE em até 3 dias da devolução dos autos em cartório.', 'C', 'Mesmo prazo para a intimação eletrônica.', tags=['literal'])
q('NS-136-01', G11, 'NSCGJ, art. 136', ['n132'], 'A publicação que omite o nome do advogado é nula, ainda que não cause prejuízo à parte.', 'E', 'Só é nula a que cause EFETIVO PREJUÍZO.',
  alt='ainda que não cause prejuízo à parte', orig='que cause efetivo prejuízo a qualquer das partes será considerada nula', tags=['literal'])
q('NS-138-01', G11, 'NSCGJ, art. 138', ['n132'], 'Em processo sob segredo de justiça, as publicações no DJEN trazem apenas as iniciais das partes.', 'C', 'Inclusive na sentença (relatório, fundamentação e dispositivo).', tags=['literal'])
q('NS-141-01', G11, 'NSCGJ, art. 141, III', ['n141'], 'A publicação de edital em jornal local é providenciada pelo ofício de justiça e comprovada por certidão.', 'E', 'Providenciada pela PARTE e comprovada pela juntada do EXEMPLAR ORIGINAL.',
  alt='providenciada pelo ofício de justiça e comprovada por certidão', orig='será providenciada pela parte ou por agência de publicidade', tags=['literal'])
q('NS-143-01', G11, 'NSCGJ, art. 143', ['n143'], 'A designação de audiências pode ser delegada ao escrivão por portaria do juiz.', 'E', 'Atribuição EXCLUSIVA E INDELEGÁVEL do juiz, salvo nos juizados especiais.',
  alt='pode ser delegada ao escrivão', orig='A designação de audiências é atribuição exclusiva e indelegável do juiz', tags=['literal'])
q('NS-145-01', G11, 'NSCGJ, art. 145', ['n143'], 'Os termos de audiência são lavrados sob ditado do juiz, rubricados por ele em todas as folhas e juntados aos autos em sua versão original.', 'C', 'Subscritos por juiz, advogados, MP e escrevente.', tags=['literal'])
q('NS-148-01', G11, 'NSCGJ, art. 148', ['n143'], 'O servidor encarregado examinará os processos 5 dias antes das audiências para verificar as intimações.', 'E', '10 (dez) dias antes.',
  alt='5 dias antes', orig='10 (dez) dias antes', tags=['literal'])
q('NS-152-01', G11, 'NSCGJ, art. 152', ['n152'], 'Depoimentos registrados em meio audiovisual não são transcritos, salvo, pelo ofício, se houver recurso e for impossível enviar a documentação eletrônica.', 'C', 'Literal.', tags=['literal'])
q('NS-156A-01', G11, 'NSCGJ, art. 156-A', ['n152'], 'Para ouvir testemunha residente em outra comarca paulista, a regra é expedir carta precatória.', 'E', 'É VEDADA a precatória para oitiva em outra comarca do Estado: agenda-se na Estação Passiva (ressalvado o art. 122, § 3º).',
  alt='a regra é expedir carta precatória', orig='É vedada a expedição de carta precatória para a realização de oitivas', tags=['caso-concreto'])
# G8 — processo eletrônico (complementos)
q('NS-1198-01', G8, 'NSCGJ, art. 1.198', ['n1198'], 'No processo eletrônico, a petição é tempestiva quando recebida até as 24 horas do último dia do prazo, pela hora de Brasília.', 'C', 'Recebida em dia sem expediente, considera-se protocolada no primeiro dia útil seguinte.', tags=['literal'])
q('NS-1201-01', G8, 'NSCGJ, art. 1.201', ['n1198'], 'Durante a suspensão dos prazos processuais, fica impedido o encaminhamento de petições eletrônicas.', 'E', 'A suspensão "NÃO IMPEDIRÁ" o envio; os pedidos são apreciados depois, salvo urgência.',
  alt='fica impedido o encaminhamento de petições', orig='não impedirá o encaminhamento de petições', tags=['literal'])
q('NS-1205-01', G8, 'NSCGJ, art. 1.205', ['n1205'], 'Pelas NSCGJ, prorroga-se o prazo quando a indisponibilidade do sistema for superior a 60 minutos entre 6h e 23h, ou ocorrer entre 23h e 24h.', 'C',
  'Atenção: no eproc (Res. 963/2025, art. 21) a janela é das 12h às 23h.', tags=['literal'])
q('NS-1205-02', G8, 'NSCGJ, art. 1.205, § 1º', ['n1205'], 'A indisponibilidade ocorrida num sábado, por qualquer período, prorroga o prazo que vence nesse dia.', 'E', 'Feriados e fins de semana, a qualquer hora: NÃO prorrogam.',
  alt='prorroga o prazo que vence nesse dia', orig='as ocorridas em feriados e finais de semana, a qualquer hora, não produzirão o efeito', tags=['literal'])
q('NS-1205B-01', G8, 'NSCGJ, art. 1.205-B', ['n1205b'], 'A indisponibilidade severa por dois ou mais dias consecutivos suspende automaticamente os prazos a partir do segundo dia, sem prejudicar a realização de audiências.', 'C', 'Art. 1.205-B, caput e § 3º.', tags=['literal'])
q('NS-1193-01', G8, 'NSCGJ, art. 1.193', ['n1192'], 'O titular do certificado digital pode alegar uso indevido por terceiro para invalidar o ato praticado com sua chave.', 'E', 'É sua exclusiva responsabilidade; a alegação de uso indevido não é oponível "em nenhuma hipótese".',
  alt='pode alegar uso indevido', orig='não sendo oponível, em nenhuma hipótese, alegação de seu uso indevido', tags=['literal'])
q('NS-1212-01', G8, 'NSCGJ, art. 1.212, § 3º', ['n1209'], 'Indeferida a distribuição da petição inicial em papel, ela poderá ser recebida mediante despacho do juiz corregedor.', 'E', '"Em NENHUMA HIPÓTESE será recebida".',
  alt='poderá ser recebida mediante despacho do juiz corregedor', orig='Em nenhuma hipótese será recebida a petição inicial em papel', tags=['literal'])
q('NS-1214-01', G8, 'NSCGJ, art. 1.214', ['n1209'], 'Os embargos à execução de processo físico tramitam em formato digital, com peticionamento eletrônico obrigatório.', 'C', 'Também embargos de terceiro, cumprimento de sentença e restauração de autos.', tags=['caso-concreto'])
q('NS-1226A-01', G8, 'NSCGJ, art. 1.226-A', ['n1224'], 'A senha de terceiro interessado para consultar processo digital não sigiloso vale por 24 horas após a emissão.', 'C', 'Senha pessoal e intransferível.', tags=['literal'])
q('NS-1225-01', G8, 'NSCGJ, art. 1.225', ['n1224'], 'Processo eletrônico em segredo de justiça pode ser consultado por qualquer advogado cadastrado no portal.', 'E', 'Só pelas PARTES E PROCURADORES HABILITADOS no processo.',
  alt='por qualquer advogado cadastrado', orig='só poderão ser consultados pelas partes e procuradores habilitados', tags=['literal'])
q('NS-1207-01', G8, 'NSCGJ, art. 1.207, § 1º', ['n1207'], 'Nos "alimentos de balcão", digitalizada a petição, os documentos físicos aguardam retirada pelo autor por 45 dias, findo o qual são inutilizados.', 'C', 'Mesmo prazo de 45 dias das petições em papel (art. 1.222, § 3º).', tags=['literal'])

if __name__ == '__main__':
    import json, collections
    e = validar(Q); print(len(Q), 'erros', e)
    print(collections.Counter(x['grupo'] for x in Q)); print(collections.Counter(x['gabarito'] for x in Q))
    print('QC', len({x['fonte'].split('QConcursos ')[1][:8] for x in Q if 'QConcursos' in x['fonte']}))
    for x in Q:
        x['fonte'] = x['fonte'].replace('Texto conferido em 24/11/2026', 'Texto conferido em 24/11/2026 (' + FONTES[x['lei']] + ')')
        x['textoLei'] = x['textoLei'].replace('máquina fotográfica10', 'máquina fotográfica').replace('lavrandose', 'lavrando-se').replace('retirálos', 'retirá-los')
    json.dump(Q, open('interna.json', 'w'), ensure_ascii=False, indent=1)
