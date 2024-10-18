<<<<<<< HEAD
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("Dashboard de Vendas:shopping_trolley:")

url = "https://labdados.com/produtos"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())
# balões
st.balloons()
# valor total
st.metric('Receita',df['Preço'].sum())
# a quantidade de vendas
st.metric('Qtde Vendas',df.shape[0])
# a quantidade de variáveis
st.metric('Qtde de variáveis',df.shape[1])
st.snow()
st.dataframe(df)
=======
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

def formatar_numero(valor):
    if valor >= 1000000:
        return f"R$ {valor / 1000000:,.2f} milhões".replace(',', '.')
    elif valor >= 1_000:
        return f"R$ {valor / 1000:,.2f} mil".replace(',', '.')
    else:
        return f"R$ {valor:.2f}".replace(',', '.')

st.title("Dashboard de Vendas :shopping_trolley:")

url = "https://labdados.com/produtos"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())

# balões
st.balloons()

# valor total
receita = df['Preço'].sum()
st.metric('Receita', formatar_numero(receita))

# a quantidade de vendas
qtde_vendas = df.shape[0]
st.metric('Qtde Vendas',formatar_numero(df.shape[0]))

# a quantidade de variáveis
qtde_variaveis = df.shape[1]
st.metric('Qtde de variáveis', qtde_variaveis)

st.snow()
st.dataframe(df)
>>>>>>> master
