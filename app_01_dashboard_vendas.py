import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(page_title="Dashboard de Vendas", page_icon="📊", layout="wide")

# Gerar dados aleatórios
def generate_sales_data():
    np.random.seed(42)
    products = ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E']
    regions = ['Norte', 'Sul', 'Leste', 'Oeste']
    
    # Dados de vendas por produto
    sales_data = pd.DataFrame({
        'Produto': products,
        'Vendas': np.random.randint(100, 1000, size=len(products)),
        'Lucro': np.random.uniform(1000, 5000, size=len(products)).round(2),
        'Custo': np.random.uniform(500, 3000, size=len(products)).round(2)
    })
    
    # Dados temporais
    dates = pd.date_range(end=datetime.today(), periods=30).to_pydatetime().tolist()
    time_series = pd.DataFrame({
        'Data': dates,
        'Vendas': np.random.randint(50, 200, size=len(dates)),
        'Clientes': np.random.randint(10, 50, size=len(dates))
    })
    
    # Dados por região
    region_data = pd.DataFrame({
        'Região': regions,
        'Vendas': np.random.randint(200, 800, size=len(regions)),
        'Satisfação': np.random.uniform(3.5, 5, size=len(regions)).round(1)
    })
    
    return sales_data, time_series, region_data

sales_data, time_series, region_data = generate_sales_data()

# Layout do dashboard
st.title("📊 Dashboard de Vendas - Análise de Desempenho")

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Vendas Totais", f"R$ {sales_data['Vendas'].sum():,.0f}", "+12% vs último mês")
col2.metric("Lucro Total", f"R$ {sales_data['Lucro'].sum():,.2f}", "+8% vs último mês")
col3.metric("Custo Total", f"R$ {sales_data['Custo'].sum():,.2f}", "-5% vs último mês")
col4.metric("Margem de Lucro", f"{(sales_data['Lucro'].sum() / sales_data['Vendas'].sum() * 100):.1f}%", "+3%")

# Gráficos
st.markdown("---")
st.subheader("Análise de Produtos")

col1, col2 = st.columns(2)

with col1:
    fig = px.pie(sales_data, values='Vendas', names='Produto', 
                 title='Distribuição de Vendas por Produto',
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.bar(sales_data, x='Produto', y=['Vendas', 'Lucro', 'Custo'], 
                 title='Comparação de Vendas, Lucro e Custo por Produto',
                 barmode='group', 
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("Tendência Temporal")

fig = px.line(time_series, x='Data', y=['Vendas', 'Clientes'], 
              title='Vendas e Novos Clientes nos Últimos 30 Dias',
              markers=True,
              color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_xaxes(title_text='Data')
fig.update_yaxes(title_text='Quantidade')
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("Desempenho por Região")

col1, col2 = st.columns(2)

with col1:
    fig = px.bar(region_data, x='Região', y='Vendas', 
                 title='Vendas por Região',
                 color='Região',
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.scatter(region_data, x='Vendas', y='Satisfação', 
                     size='Vendas', color='Região',
                     title='Relação entre Vendas e Satisfação do Cliente',
                     hover_name='Região',
                     size_max=60,
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

# Informações adicionais
st.markdown("---")
st.subheader("Insights Gerados Automaticamente")

insights = [
    "📌 Produto B apresenta a maior margem de lucro (32.5%)",
    "📌 Região Oeste tem o maior índice de satisfação (4.7/5.0)",
    "📌 Vendas estão crescendo em média 5% semanalmente",
    "📌 Custo do Produto D está 15% acima da média"
]

for insight in insights:
    st.info(insight)

st.caption("Dados atualizados em: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))