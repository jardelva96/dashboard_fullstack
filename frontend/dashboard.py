import streamlit as st
import requests
import pandas as pd

# Título do dashboard
st.title("Dashboard Interativo")

# URL base do backend (pode ser ajustada conforme necessário)
backend_url = "http://backend:8000"

# Visualizar dados do banco
st.header("Dados do Banco")

# Carregar dados do backend
try:
    response = requests.get(f"{backend_url}/data")
    if response.status_code == 200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.warning("Nenhum dado encontrado!")
    else:
        st.error(f"Erro ao carregar os dados: {response.status_code}")
except requests.exceptions.RequestException as e:
    st.error(f"Erro de conexão com o backend: {e}")

# Adicionar novos dados
st.header("Adicionar Dados")

# Campos para entrada de novos dados
label = st.text_input("Label", placeholder="Digite o nome do rótulo")
value = st.number_input("Value", min_value=0.0, step=0.1, format="%.2f")

# Botão para enviar os dados
if st.button("Adicionar Dados"):
    if label.strip():  # Verifica se o label não está vazio
        try:
            response = requests.post(f"{backend_url}/data", json={"label": label, "value": value})
            if response.status_code == 200:
                st.success("Dados adicionados com sucesso!")
            else:
                st.error(f"Erro ao adicionar dados: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Erro de conexão com o backend: {e}")
    else:
        st.warning("O campo 'Label' não pode estar vazio!")
