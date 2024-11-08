# EXEMPLO 2
import pandas as pd
import numpy as np

# Obter dados
try:
    print("Obtendo dados...")
    ENDERECO_DADOS="https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"
    
    #encodings: utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=";", encoding="iso-8859-1")
    # Delimitando somente as variáveis do Exemplo01: munic e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[["munic","roubo_veiculo"]]

    # totalizar roubo veiculo por munic
    # utilizando varios metodos de uma vez:
    df_roubo_veiculo = df_roubo_veiculo.groupby(["munic"]).sum(["roubo_veiculo"]).reset_index()

    print(df_roubo_veiculo.head())

    print("\nDados obtidos com sucesso!")

except Exception as e:
    print(f"Erro ao obter dados: {e}")
    exit()


# Gerando informações
try:
    print("Calculando informações sobre padrão de roubo de veículos...")
    # Array Numpy
    array_roubo_veiculo = np.array(df_roubo_veiculo["roubo_veiculo"])
    # Média de roubo de veículos
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    # Mediana de roubo de veículo - Divide distribuição em 2 partes iguais
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

    # Calculando a distancia entre média e mediana
    dist_roubo_veiculo = abs((media_roubo_veiculo-mediana_roubo_veiculo)/mediana_roubo_veiculo)

    print("\nMedidas de tendência central:")
    print(f"Média de roubo de veículo: {media_roubo_veiculo}")
    print(f"Mediana de roubo de veículo: {mediana_roubo_veiculo}")
    print(f"Distância entre média e mediana: {dist_roubo_veiculo}%")

except Exception as e:
    print(f"Erro ao obter informações sobre padrão de roubo de veículos: {e}")
    exit()
