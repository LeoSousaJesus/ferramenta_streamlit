import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# inicio minha jornada low code
st.title("Dashboard de Vendas :shopping_trolley:")
url = 'https://labdados.com/produtos'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())
st.dataframe(dados)
