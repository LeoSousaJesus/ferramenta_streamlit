import streamlit as st
import requests
import pandas as pd
import plotly.express as px


def formata_numeros(valor):
    if valor >= 1000000:
        return f"R$ {valor / 1000000:,.2f} milhões".replace(',', '.')
    elif valor >= 1000:
        return f"{valor/1000:,.2f}mil"
    else:
        return f"{valor:,.2f}" 

# inicio minha jornada low code
st.title("Dashboard de Vendas :shopping_trolley:")
url = 'https://labdados.com/produtos'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())
st.dataframe(dados)


if st.button("todos"):
    st.balloons()
    st.metric('Receita',dados['Preço'].sum())
    st.metric('Quantidade de vendas (linhas)',formata_numeros(dados.shape[0]))
    st.metric('Quantidade de variáveis (colunas)',dados.shape[1])
    st.dataframe(dados)
    st.snow()
else:
    st.write("clique no botão todos")