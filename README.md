# Pipeline de ETL Automatizado: Integração de Sistemas e Star Schema 📊

Este projeto foi desenvolvido para resolver um problema clássico de Engenharia e Análise de Dados: a **integração de sistemas isolados**. 

Construí um pipeline de ETL (Extração, Transformação e Carga) ponta a ponta para unificar dados dispersos de três fontes diferentes (simulando um CRM, um ERP e um Gateway de Pagamentos), tratar inconsistências críticas e consolidar as informações em um Data Warehouse local utilizando a modelagem **Star Schema**.

## 🛠️ Tecnologias e Bibliotecas
- **Python (Pandas):** Responsável por toda a extração, tratamento de strings/datas, remoção de duplicatas e regras de cruzamento para barrar anomalias.
- **SQL (SQLite):** Banco de dados relacional escolhido para armazenar as tabelas.
- **Git & GitHub:** Controle de versão e documentação.

## 🏗️ Estrutura e Modelagem do Projeto
O fluxo ingere dados de três arquivos brutos, aplica as regras de negócio e modela o banco nas seguintes tabelas:

- `clientes.csv` ➡️ Limpo e carregado na dimensão **`tb_cad_clientes`**.
- `produtos.csv` ➡️ Limpo e carregado na dimensão **`tb_cad_produtos`**.
- `vendas.csv` ➡️ Validado contra clientes/produtos órfãos e carregado na fato **`tb_vendas`**.
- `pipeline.py`: Script principal contendo o motor do ETL.
- `teste_queries.py`: Script de validação analítica executando `INNER JOINs` e agregações financeiras para testar a integridade do banco.

## 📈 Resultados e Impacto
- Eliminação completa do retrabalho manual na preparação e limpeza de relatórios diários.
- Construção de um banco de dados íntegro e relacional, garantindo que vendas sem clientes ou produtos cadastrados sejam barradas antes de poluírem os relatórios.
- Base de dados pronta para consumo imediato e criação de dashboards em ferramentas de Business Intelligence (como Power BI ou Tableau), sem necessidade de modelagem adicional na ferramenta visual.
