# Nicolas Oliveira - RA: 2303181
# Nírya Giaquinto - RA: 1903778

import sqlalchemy as sqa 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image #exibir imagem


#Criar a interface com o banco
engine = sqa.create_engine("sqlite:///df_yahoo.db", echo=True)
conn = engine.connect()

#Ler os dados e criar um dataframe
df_yahoo= pd.read_sql('cotacao_yahoo.db', con=conn)
df_yahoo_cotacao = pd.DataFrame(df_yahoo, columns=['name', 'price', 'change', 'per_market', 'market'])

#Personalizar o título da página
st.set_page_config(
    page_title="Cripto Currencies",
    page_icon="💸",
    layout="wide")

###### Imagem do App 

# Carregue a imagem da sua logo
logo = Image.open('bitcoin2.png')  # Substitua 'caminho/para/sua/logo.png' pelo caminho correto para sua imagem

col1, col2, col3 = st.columns([1, 20, 1])

# Coluna vazia para espaço em branco à esquerda da logo
with col1:
    st.write("")

# Coluna com a logo
with col2:
    st.image(logo, width=100)  # Defina a largura desejada para a logo

# Coluna vazia para espaço em branco à direita da logo
with col3:
    st.write("")

st.title('CriptoMoedas Ao Vivo')

st.write("# CRYPTO CURRENCIES💸")

st.write("""
Criptomoedas são moedas digitais ou virtuais que usam criptografia para segurança. 
Elas operam de forma descentralizada na maioria das vezes, utilizando a tecnologia blockchain.
A seguir, apresentamos algumas das principais criptomoedas com suas respectivas mudanças de preço e valor de mercado.
""")

st.header('Tabela de Dados Gerais')
st.dataframe(df_yahoo_cotacao, width=1500, height=500, hide_index=True)