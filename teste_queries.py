import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data_warehouse.db")

print("--- EXECUTANDO QUERIES SQL DE VALIDAÇÃO ---\n")

print("1. Buscando todos os registros limpos:")
query_todos = "SELECT * FROM vendas_calculadas;"
df_todos = pd.read_sql(query_todos, con=engine)
print(df_todos)
print("-" * 50)

print("\n2. Agrupando faturamento total por Status (Métrica de Negócio):")
query_BI = """
    SELECT 
        status, 
        COUNT(id_pedido) as total_pedidos,
        SUM(valor_total) as faturamento_total
    FROM vendas_calculadas
    GROUP BY status
    ORDER BY faturamento_total DESC;
"""
df_BI = pd.read_sql(query_BI, con=engine)
print(df_BI)
print("-" * 50)