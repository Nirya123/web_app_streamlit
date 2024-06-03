# Nicolas Oliveira - RA: 2303181
# Nírya Giaquinto - RA: 1903778

#Importar as bibliotecas
import sqlalchemy as sqa 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

#Criar o objeto para o controle do navegador - abre o navegador (Chrome)
navegador = webdriver.Chrome()

#Selenium tem a função que chama o método get informando o site para coletar os dados
navegador.get('https://finance.yahoo.com/crypto?offset=0&count=100')

#Encontrar os elementos - utilizar a função By e a string que foi selecionada
navegador.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[2]/span/div/span/span').click()

#Copiar os elementos
name = navegador.find_element(By.XPATH,'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[2]').text
price = navegador.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[3]').text
change = navegador.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[4]').text
per_change = navegador.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[5]').text
market = navegador.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[6]').text

#Exibir na tela os elementos criados
print(name)
print(price)
print(change)
print(per_change)
print(market)

#Criar uma lista com os elementos copiados
lista = []
for i in range(1,100):
    name = navegador.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[1]/table/tbody/tr['+str(i)+']/td[2]').text
    price = navegador.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[1]/table/tbody/tr['+str(i)+']/td[3]').text
    change = navegador.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[1]/table/tbody/tr['+str(i)+']/td[4]').text
    per_change = navegador.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[1]/table/tbody/tr['+str(i)+']/td[5]').text
    market = navegador.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[1]/table/tbody/tr['+str(i)+']/td[6]').text
    
    lista.append([name, price, change, per_change, market])

print(lista)

#Converter a lista em uma tabela (dataframe)
df_yahoo = pd.DataFrame(lista, columns=['name', 'price', 'change', 'per_market', 'market'])

#Fazer a tratativa dos dados
df_yahoo['per_market'] = df_yahoo['per_market'].str.replace('+','').str.replace('%','').str.replace(',','.').astype(float)

df_yahoo['market'] = df_yahoo['market'].str.replace('.','').str.replace('T','').str.replace('B','').astype(float)

#Salvar o dataframe dentro das bases originais em formato csv e json
df_yahoo.to_csv('../0_bases_originais/dados_originais.csv', sep=';' ,index=False, encoding='utf-8')
df_yahoo.to_json('../0_bases_originais/dados_originais.json')

#Criar uma instância em um banco de dados e armazenar - sqlalchemy
engine = sqa.create_engine("sqlite:///df_yahoo.db", echo=True)

#Criar a conexão com o Banco
conn = engine.connect()

#Armazenar o dataframe dentro do banco
df_yahoo.to_sql('cotacao_yahoo.db', con=conn)

#Encerrar a sessão do navegador
navegador.quit()