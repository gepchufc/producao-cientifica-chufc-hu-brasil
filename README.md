# Produção Científica CH-UFC / HU Brasil

Painel público de indicadores bibliométricos agregados da produção científica identificada por afiliação ao Hospital Universitário Walter Cantídio (HUWC), à Maternidade-Escola Assis Chateaubriand (MEAC) e ao Complexo Hospitalar da Universidade Federal do Ceará (CH-UFC).

## Escopo público

- Quantidade de artigos distintos por ano e por unidade.
- Evolução histórica da produção científica, com tratamento do ano corrente como período parcial.
- Comparação entre instituições e exportação apenas de séries agregadas.
- Sem nomes de autores, títulos, resumos, DOI/PMID, afiliações individuais ou dados de pacientes.

**Nota metodológica:** os registros são identificados por afiliação bibliográfica declarada. Isso não comprova vínculo funcional atual ou uso de dados assistenciais. A cobertura não é exaustiva. Um mesmo artigo pode aparecer em mais de uma unidade.

## Execução local

```bash
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

## Publicação

Este repositório contém **somente dados agregados**, em `data/indicadores_agregados.json`. O arquivo é estático: a atualização exige a geração de uma nova versão a partir do ambiente privado de coleta, seguida de revisão e publicação. Não há conexão do aplicativo público ao banco detalhado.

No Streamlit Community Cloud: `main` → `streamlit_app.py`.

## Política de dados e responsabilidade

Não há cadastro de visitantes no aplicativo e não se expõe informação bibliográfica individualizada. Dados técnicos de navegação podem ser processados pelo provedor de hospedagem. Dúvidas e solicitações de correção: use a seção **Issues** do repositório sem enviar informações pessoais, ou um canal privado que o responsável pelo repositório venha a indicar.

Esta aplicação é uma iniciativa independente de portfólio técnico. Não é um serviço oficial da UFC ou da HU Brasil/Ebserh. A apresentação e denominação institucional devem ser revisadas antes da divulgação pública.

Consulte [docs/METODOLOGIA_E_PRIVACIDADE.md](docs/METODOLOGIA_E_PRIVACIDADE.md) para detalhes.
