import sqlite3
import pandas as pd

print("Conectando ao Banco de Dados...")
conexao = sqlite3.connect('data_warehouse.db')

query_relatorio = """
SELECT 
    v.id_venda,
    v.data_venda,
    c.nome_cliente,
    c.uf,
    p.nome_produto,
    v.valor_final
FROM tb_vendas AS v
INNER JOIN tb_cad_clientes AS c ON v.id_cliente = c.id_cliente
INNER JOIN tb_cad_produtos AS p ON v.id_produto = p.id_produto
ORDER BY v.data_venda;
"""

df_relatorio = pd.read_sql_query(query_relatorio, conexao)
print("\n RELATÓRIO DE VENDAS INTEGRADAS:")
print(df_relatorio.to_string(index=False))

query_faturamento = """
SELECT 
    c.uf AS Estado, 
    SUM(v.valor_final) AS Faturamento_Total
FROM tb_vendas AS v
INNER JOIN tb_cad_clientes AS c ON v.id_cliente = c.id_cliente
GROUP BY c.uf
ORDER BY Faturamento_Total DESC;
"""

df_faturamento = pd.read_sql_query(query_faturamento, conexao)
print("\nFATURAMENTO POR ESTADO:")
print(df_faturamento.to_string(index=False))

conexao.close()