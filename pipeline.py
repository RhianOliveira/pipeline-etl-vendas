import pandas as pd
import sqlite3

# EXTRAÇÃO
print("Lendo os arquivos CSV")
df_clientes = pd.read_csv('clientes.csv')
df_produtos = pd.read_csv('produtos.csv')
df_vendas = pd.read_csv('vendas.csv')



# TRANSFORMAÇÃO
print("INICIANDO")

# CLIENTES
df_clientes = df_clientes.drop_duplicates(subset=['id_cliente'])
df_clientes['nome_cliente'] = df_clientes['nome_cliente'].str.strip().str.title()
df_clientes['cidade'] = df_clientes['cidade'].str.strip().str.title()
df_clientes['uf'] = df_clientes['uf'].str.strip().str.upper().str[:2]
df_clientes['tipo_pessoa'] = df_clientes['tipo_pessoa'].replace({'1': 'PF', '2': 'PJ'}).str.upper()


# PRODUTOS
df_produtos['nome_produto'] = df_produtos['nome_produto'].str.strip().str.title()
df_produtos['valor_base'] = df_produtos['valor_base'].astype(str)
df_produtos['valor_base'] = df_produtos['valor_base'].str.replace('R$', '', regex=False)
df_produtos['valor_base'] = df_produtos['valor_base'].str.replace(',', '.', regex=False)
df_produtos['valor_base'] = pd.to_numeric(df_produtos['valor_base'], errors='coerce')
df_produtos = df_produtos.dropna(subset=['valor_base'])


# VENDAS
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'], format='mixed', dayfirst=True, errors='coerce').dt.strftime('%Y-%m-%d')
qtd_vendas_antes = len(df_vendas)
df_vendas = df_vendas[df_vendas['id_cliente'].isin(df_clientes['id_cliente'])]
df_vendas = df_vendas[df_vendas['id_produto'].isin(df_produtos['id_produto'])]
qtd_vendas_depois = len(df_vendas)
print(f"{qtd_vendas_antes - qtd_vendas_depois} vendas foram barradas pois estavam sem cliente ou produto cadastrado.")

# LOAD
print(" Salvando os dados no Banco de Dados...")
conexao = sqlite3.connect('data_warehouse.db')

df_clientes.to_sql('tb_cad_clientes', conexao, if_exists='replace', index=False)
df_produtos.to_sql('tb_cad_produtos', conexao, if_exists='replace', index=False)
df_vendas.to_sql('tb_vendas', conexao, if_exists='replace', index=False)

conexao.close()
print(" FINALIZADO!!!")