import pandas as pd
from sqlalchemy import create_engine

def extrair_dados(caminho_arquivo):
    print("Iniciando extração dos dados...")
    df = pd.read_csv(caminho_arquivo)
    print(f"Dados extraídos com sucesso! Total de linhas: {len(df)}")
    return df

def transformar_dados(df):
    print("\nIniciando transformation e limpeza dos dados...")
    
    df_limpo = df.drop_duplicates()
    df_limpo['cliente'] = df_limpo['cliente'].str.strip().str.title()
    df_limpo['produto'] = df_limpo['produto'].str.strip()
    
    df_limpo['data_venda'] = pd.to_datetime(df_limpo['data_venda'], errors='coerce', format='mixed')
    
    df_limpo['produto'] = df_limpo['produto'].fillna('Não Informado')
    df_limpo['valor_total'] = df_limpo['valor_total'].fillna(0.0)
    
    print("Transformação concluída com sucesso!")
    return df_limpo

def carregar_dados(df, nome_banco, nome_tabela):

    print(f"\nConectando ao banco de dados {nome_banco}...")
    engine = create_engine(f"sqlite:///{nome_banco}")
    
    print(f"Carregando dados na tabela '{nome_tabela}'...")
    df.to_sql(nome_tabela, con=engine, if_exists='replace', index=False)
    print("Carga concluída com sucesso! O banco de dados está pronto.")

if __name__ == "__main__":
    arquivo_origem = "vendas_bruto.csv"
    banco_destino = "data_warehouse.db"
    tabela_destino = "vendas_calculadas"
    
    dados_brutos = extrair_dados(arquivo_origem)
    dados_tratados = transformar_dados(dados_brutos)
    carregar_dados(dados_tratados, banco_destino, tabela_destino)
    
    print("\n--- PIPELINE EXECUTADO COM SUCESSO DE PONTA A PONTA ---")