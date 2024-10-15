# Escolha qualquer dataset no Kaggle

# Faça você mesmo! Faça como eu fiz!

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("Dashboard de Queimadas Setembro 2024")

url = "https://raw.githubusercontent.com/LeoSousaJesus/dados_queimadas2024/refs/heads/main/queimadas_resumo.csv"
df = pd.read_csv(url)

st.dataframe(df)