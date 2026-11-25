# Ferramentas — app de lei seca (Certo/Errado + Anki) a partir de um edital

Tudo o que foi usado para montar o app do Escrevente TJ-SP (VUNESP, 2026), pronto para repetir com outro edital.

## Estrutura
| Pasta / arquivo | Para que serve |
|---|---|
| `base/` | App-base (PWA de um arquivo só: `index.html`, `sw.js`, `manifest.json`, ícones). Agendador SM-2, mixes, quadros "Não confunda", importação, backup, Certo/Errado e múltipla escolha com tabela. |
| `build_app.py` | Injeta os bancos (`.json`) e os quadros no app-base e gera a pasta pronta para publicar. |
| `common.py` | Matérias de **lei**: `norm()` (normaliza texto legal), `h()` (hash), `factory()` (cria questões C/E a partir dos trechos de lei) e `validar()`. |
| `nl.py` | Matérias **sem lei** (Português, Informática, RL, Matemática): `banco()`, `validar()`, `VU()` (origem de prova anterior). |
| `verificacao/hashjs.js` | Roda no navegador, na página oficial da lei: gera hashes de cada parágrafo **sem o texto riscado** (revogado). |
| `verificacao/jsnorm.py` | Mesmo `norm()`/hash do lado Python, para comparar com os hashes da página. |
| `verificacao/parse_pdf_paragrafos_*.py` | Exemplos de como quebrar o texto de um PDF oficial (normas, regimento) em parágrafos. |
| `verificacao/gerar_trechos_de_pdf.py` | Exemplo de como gerar os trechos de lei (`L`) direto dos parágrafos do PDF, para não digitar texto legal à mão. |
| `exemplos/` | Bancos reais: `interna.py` (lei, com PDF), `pcd.py` (lei, Planalto), `info.py`, `por.py`, `rl.py`, `mat.py` (sem lei), quadros e o `edital_tjsp_2026.js`. |
| `testes/` | Testes com Playwright: carga do app e atualização de uma versão para outra sem perder o progresso. |

## Gerar o app para outro edital
1. Escreva o objeto do edital em `meu_edital.js` (copie o formato de `exemplos/edital_tjsp_2026.js`: `prova`, `blocos[]`, `materias[]` com `nome`, `questoes`, `leis[]` e `recorte`). Matérias sem lei ficam com `leis: []`.
2. Gere um `.json` por matéria (rodando os scripts de banco) e, se quiser, `quadros_*.json`.
3. Monte o app:
   ```bash
   LEISECA_BASE=base LEISECA_EDITAL=meu_edital.js LEISECA_SEM_TJSP=1 \
   LEISECA_TITULO="Lei Seca C/E — ÓRGÃO" \
   python3 build_app.py ../saida 1.0.0 banco1.json,banco2.json quadros1.json,quadros2.json ""
   ```
   - 2º argumento: versão (`MAJOR.MINOR.PATCH`). **Aumente a cada publicação**: é ela que faz o app baixar as questões novas e as revisadas, sem mexer no progresso.
   - 5º argumento (opcional): ids de questões a remover, separados por vírgula.
4. Teste (`testes/teste_carga.py`, `testes/teste_atualizacao.py`) e publique a pasta de saída (GitHub Pages ou Netlify).

## Campos de uma questão
`id, tipo ("CE"|"ME"), materia, lei, grupo, artigo, enunciado, gabarito, textoLei, comentario, tags[], verificado, fonte` e, quando houver: `trechoAlterado` (obrigatório se gabarito "E": trecho errado no enunciado), `trechoOriginal` (o trecho certo no texto), `rubrica`, `origem {banca, ano, cargo, adaptada}`, `alternativas {A..E}` (tipo ME) e `tabela {colunas, linhas, rotulos}`.
