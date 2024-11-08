# EXEMPLO 1 - Correção da Atividade 1

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

# AGRUPANDO OS PRODUTOS COM O MESMO NOME E SOMANDO AS QUANTIDADES E VALORES
df_agrupado = df_estoque.groupby("NomeProduto").agg({
    "QuantidadeEstoque": "sum",
    "TotalEstoque": "sum"
}).reset_index() # nao pega o nome da coluna e coloca como indice


# Ordenando os produtos pelo total de estoque
df_ordenado = df_agrupado.sort_values(by="TotalEstoque", ascending=False)

print("\n")
print(df_ordenado)
# print(df_estoque[["NomeProduto","TotalEstoque"]])

# METODO 3
# Transformando o campo em array numpy
array_total_estoque = np.array(df_agrupado["TotalEstoque"])

media = np.mean(array_total_estoque)
mediana = np.median(array_total_estoque)

# CALCULO DO VALOR DEFINITIVO
distance = abs((media-mediana)/mediana)*100

# quando a distancia dá acima ou igual a 25%, a mediana nao é confiavel
# nesse caso usamos o ABS para usarmos o valor absoluto e evitar numeros negativos
# quando o numero dá negativo, a media está sendo afetada por valores menores

print(f"\nDistância entre Média e Mediana: {distance}")
# print(f"\nValor por produto total: {distance}")
