import streamlit as st
import pandas as pd
from dataset import df
from utils import convert_csv, mensagem_sucesso

st.title("Dataset de Vendas")

with st.expander("Colunas"):
    colunas = st.multiselect(
        "Selecione as colunas",
        list(df.columns),
        list(df.columns),
    )

st.sidebar.title("Filtros")
with st.sidebar.expander("Categoria do Produto"):
    categorias = st.multiselect(
        "Selecione as categorias",
        df["Categoria do Produto"].unique(),
        df["Categoria do Produto"].unique(),
    )

with st.sidebar.expander("Preço do Produto"):
    preco = st.slider(
        "Selecione o preço",
        0, 5000,
        (0, 5000)
    )
with st.sidebar.expander("Data da Compra"):
    data_compra = st.date_input(
        "Selecione a data",
        (df["Data da Compra"].min(),
         df["Data da Compra"].max())
    )

# Usar máscaras pandas em vez de df.query para evitar problemas com numexpr
# (colunas com espaços/backticks e operador 'between' causavam SyntaxError)
mask_categoria = df['Categoria do Produto'].isin(categorias)
mask_preco = df['Preço'].between(preco[0], preco[1])

# Converter as datas selecionadas (datetime.date) para pandas.Timestamp antes da comparação
start_dt = pd.to_datetime(data_compra[0])
end_dt = pd.to_datetime(data_compra[1])
mask_data = df['Data da Compra'].between(start_dt, end_dt)

filtro_dados = df.loc[mask_categoria & mask_preco & mask_data, colunas]

st.dataframe(filtro_dados)

st.markdown(
    f'A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas.')


st.markdown("Escreva um nome para o arquivo CSV")

coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input("", label_visibility='collapsed')
with coluna2:
    st.download_button(
        label="Download CSV",
        data=convert_csv(filtro_dados),
        file_name=f"{nome_arquivo}.csv",
        mime="text/csv",
        on_click=mensagem_sucesso
    )
