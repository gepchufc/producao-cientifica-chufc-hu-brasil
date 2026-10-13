# Metodologia e privacidade — painel público

## Finalidade

Exibir exclusivamente indicadores agregados de referências bibliográficas relacionadas ao CH-UFC/HU Brasil, para análise da evolução temporal e comparação entre unidades. O indicador não equivale ao número de estudos que utilizaram dados assistenciais dos hospitais.

## Origem

Os registros consolidados foram recuperados de fontes científicas públicas (PubMed, OpenAlex e Europe PMC). O ambiente de coleta trabalha com outros provedores de metadados em validação; a presença desses provedores em código interno não constitui evidência de coleta efetiva.

## Método

1. Identificar registros candidatos por termos de afiliação de HUWC, MEAC e CH-UFC.
2. Analisar cada afiliação de autor separadamente para evitar associações erradas entre autores de um mesmo artigo.
3. Deduplicar artigos mediante identificadores bibliográficos (prioridade DOI, PMID e identificadores das fontes), com revisão de casos ambíguos.
4. Manter somente artigos com afiliação hospitalar explícita nos agregados públicos.
5. Contar uma publicação uma única vez no consolidado de cada ano. Na comparação de unidades, ela pode constar em mais de uma instituição, por isso os totais não são somáveis.
6. Exportar somente `ano → quantidade` e `ano × instituição → quantidade`. Não exportar metadados individuais.

O ano de publicação segue os metadados bibliográficos; pode haver correções ou atrasos de indexação. O ano corrente é parcial. A cobertura científica não é exaustiva.

## Proteção e minimização

O repositório público **não contém** nomes de autores, afiliações, e-mails, títulos, resumos, DOI, PMID, identificadores de registros, tabelas de autoria, logs de coleta, credenciais ou dados assistenciais. O arquivo `data/indicadores_agregados.json` contém somente agrupamentos de contagem.

Não é possível inferir identidade de pessoas diretamente do conjunto publicado, mas grupos muito pequenos podem ser correlacionados com fontes públicas externas. Avalie supressão/agrupamento em futuras versões se indicadores permitirem identificação indireta.

A publicação não implica parecer jurídico definitivo de conformidade à LGPD. Revisão institucional, definição do controlador, base legal, responsabilidades, contato de privacidade e práticas de hospedagem devem ser estabelecidos pelo responsável antes de um uso institucional formal.

## Atualização

A atualização do conjunto público depende da execução de `exportar_indicadores_publicos.py` no ambiente privado, da revisão do JSON gerado e da posterior atualização do repositório público. O painel não acessa o banco interno em tempo de execução.

## Uso institucional

Trata-se de uma iniciativa independente de portfólio, sem representação oficial da UFC ou da HU Brasil/Ebserh. A nomenclatura, identidade visual e apresentação institucional devem ser validadas antes de uso oficial.
