import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Análise de Vendas de Carros')

try:
    car_data = pd.read_csv('vehicles.csv')
except FileNotFoundError:
    st.error('Arquivo "vehicles.csv" não encontrado. Verifique se está no diretório correto.')
    st.stop()

# Filtro de preço interativo
st.subheader('Filtro de Preço')
price_min = int(car_data['price'].min())
price_max = int(car_data['price'].max())
price_range = st.slider(
    'Selecione a faixa de preço:',
    min_value=price_min,
    max_value=price_max,
    value=(price_min, price_max),
    format="$%d"  # <-- formata como dólar
)

# Aplicar o filtro
filtered_data = car_data[(car_data['price'] >= price_range[0]) & (car_data['price'] <= price_range[1])]

# Escolha do tipo de gráfico
chart_type = st.radio("Escolha o tipo de gráfico:", ("Histograma", "Dispersão"))

# Gráfico de histograma
if chart_type == "Histograma":
    st.write('Análise da quilometragem dos veículos disponíveis para venda:')
    fig_hist = px.histogram(filtered_data, x="odometer")
    fig_hist.update_layout(
        title='Distribuição da Quilometragem',
        xaxis_title='Quilometragem (milhas)',
        yaxis_title='Número de Veículos'
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersão
elif chart_type == "Dispersão":
    st.write('Comparação entre preço e quilometragem dos veículos anunciados:')
    fig_scatter = px.scatter(filtered_data, x="odometer", y="price")
    fig_scatter.update_layout(
        title='Preço vs Quilometragem',
        xaxis_title='Quilometragem (milhas)',
        yaxis_title='Preço (USD)'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)