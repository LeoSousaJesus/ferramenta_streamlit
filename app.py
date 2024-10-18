import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Função para formatar números
def formata_numero(valor, simbolo):
    return f"{simbolo}{valor:,.2f}"

# Carregar os dados (substitua pelo seu caminho ou método de carregamento)
# Exemplo de dados: você deve carregar seus próprios dados em um DataFrame.
dados = pd.DataFrame({
    'Local da compra': ['Goiás', 'Mato Grosso', 'Goiás', 'Minas Gerais'],
    'Preço': [100, 200, 150, 300],
    'lat': [-15.7801, -16.5000, -15.7801, -17.5000],
    'lon': [-47.9292, -52.0000, -47.9292, -45.0000]
})

# Layout
coluna1, coluna2 = st.columns(2)

with coluna1:
    st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))

with coluna2:
    st.metric('Quantidade de vendas', formata_numero(dados.shape[0], ''))

st.dataframe(dados)

# Tabelas
receita_estados = dados.groupby('Local da compra')[['Preço']].sum()
receita_estados = dados.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(
    receita_estados, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)

# Gráficos
fig_mapa_receita = px.scatter_geo(receita_estados,
                                   lat='lat',
                                   lon='lon',
                                   scope='south america',
                                   size='Preço',
                                   template='seaborn',
                                   hover_name='Local da compra',
                                   hover_data={'lat': False, 'lon': False},
                                   title='Receita por Estado')

with coluna1:
    st.plotly_chart(fig_mapa_receita)

# Execute a aplicação com: streamlit run app.py
