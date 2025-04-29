import os # Utilizada para manipulação de arquivos e diretórios
from os.path import join # Juntar paths
import pandas as pd # Biblioteca para manipulação de dados
from datetime import datetime, timedelta # Para manipulação de datas e horas

# intervalo de datas para aprevisao do tempo
# Aqui define o intervalo de datas em uma semana a partir de hoje
# data_inicio = datetime.today() # Data atual
# data_fim = data_inicio + timedelta(days=7) # Data de fim é 7 dias após a data atual
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# formatando as datas
# Aqui as datas são formatadas para o formato 'YYYY-MM-DD' que é o padrão aceito pela API
# Isso é feito para garantir que as datas estejam no formato correto para a requisição da API
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

city = 'Boston'
key = 'GYDHYHQDYQ2NVNL4EWCFH4BPD'

# O join fuizado para juntar o URL base da API com os parâmetros necessários para a requisição
# Aqui a URL é construída com os parâmetros necessários para a requisição da API
URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
            f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')

dados = pd.read_csv(URL) # Lê os dados da URL e armazena em um DataFrame do pandas
# Aqui os dados são lidos a partir da URL e armazenados em um DataFrame do pandas       
print(dados.head()) 

# Definindo o caminho
file_path = f'/root/data_pipeline_tempo/seamana={data_inicio}'
os.mkdir(file_path) #Para que a pasta seja criada no caminho

# Criando o csv com o pandas
dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv') # Info mais importantes 
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')# Info mais importantes 