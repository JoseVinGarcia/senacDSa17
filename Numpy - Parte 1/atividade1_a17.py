# ATIVIDADE 1 - Encontrando total por produto usando Numpy

from sqlalchemy import create_engine
import pandas as pd
import numpy as np

host = "localhost"
user = "root"
password = "root"
database = "bd_loja"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

# leitura dos dados da tabela de produtos
df_estoque = pd.read_sql("tb_produtos",engine)

# calcula o valor do estoque por linha
df_estoque["TotalEstoque"] = df_estoque["QuantidadeEstoque"] * df_estoque["Valor"]

print("\n")
print(df_estoque[["NomeProduto","TotalEstoque"]])

# METODO 1
# print(f"\nTotal geral em estoque: R${df_estoque['TotalEstoque'].sum()}")

# media = np.mean(df_estoque["TotalEstoque"])
# mediana = np.median(df_estoque["TotalEstoque"])

# print(f"\nMédia do estoque total: {media}")
# print(f"\nMediana do estoque total: {mediana}")

# METODO 2
ttp = np.median(df_estoque['TotalEstoque'])
print(f"\nTotal por produto em estoque: R${ttp}")
