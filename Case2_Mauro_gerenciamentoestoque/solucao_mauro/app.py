import streamlit as st
import pandas as pd
from funcoes_app import visualiza_estoque, realiza_venda, relatorio_vendas

st.title("Sistema de estoque")
acao = st.selectbox("Escolha uma ação", 
                    ["Visualizar estoque", 
                     "Realizar venda", 
                     "Relatório de vendas"
                     ])

map_acao_titulo = {
    "Visualizar estoque": "Gerenciando estoque",
    "Realizar venda": "Realizando uma venda",
    "Relatório de vendas": "Exibindo relatório de vendas"
}

st.subheader(map_acao_titulo[acao])

if acao == "Visualizar estoque":
    st.table(visualiza_estoque())

elif acao == "Realizar venda":
    produtos_possiveis = pd.read_csv('base_estoque_produtos_naturais.csv')['Produto'].sort_values().unique()
    
    with st.form("form_venda"):
        st.subheader("Formulário de venda")
        st.write("Selecione o produto e a ser quantidade vendida")
        
        produto = st.selectbox("selecione o produto", produtos_possiveis)
        
        total_vendido = st.number_input("Quantidade vendida (em gramas)", min_value = 0, step = 100) / 1000 # Convertendo para kg
        
        submit_button = st.form_submit_button("Registrar venda")
        
    if submit_button:
        
        venda = realiza_venda(produto, total_vendido)
        
        if venda:
            st.success(f"Venda registrada com sucesso! Produto: {produto}, Quantidade: {total_vendido} kg")
        else:
            st.error(f"Venda não registrada. Estoque insuficiente para o produto: {produto}.")
            
elif acao == "Relatório de vendas":
    
    st.subheader("Relatório de vendas")
    
    dict_analise = relatorio_vendas()
    
    st.write(f"Valor total vendido: R$ {dict_analise['valor_total_vendido']:.2f}")
    st.write(f"Número total de vendas: {dict_analise['numero_total_vendas']}")
    st.write(f"Ticket médio: R$ {dict_analise['ticket_medio']:.2f}")
    
    st.write(f"Produtos mais vendidos (vendas): {dict_analise['produtos_mais_vendidos_vendas']}")
    st.write(f"Produto mais vendido (em valor): {dict_analise['produtos_mais_vendidos_reais']}")
    st.write(f"Produto mais vendido (em quantidade): {dict_analise['valor_total_vendido_kgs']}")