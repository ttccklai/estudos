import streamlit as st
import pandas as pd
from funcoes_app import visualiza_estoque, realiza_venda, relatorio_vendas

st.title("Sistema de Gerenciamento de Estoque")

acao = st.selectbox("Escolha uma ação:",
                    ["Visualizar Estoque", 
                     "Realizar Venda", 
                     "Relatório de Vendas"])

map_acao_titulo = {
    "Visualizar Estoque": "Gerenciando Estoque",
    "Realizar Venda": "Realizando de Venda",
    "Relatório de Vendas": "Exibindo Relatório de Vendas"
}

st.subheader(map_acao_titulo[acao])

estoque_atualizado = None

if acao == "Visualizar Estoque":
    if estoque_atualizado is None:
        st.table(visualiza_estoque('base_original_produtos_naturais.csv'))
    else:
        st.table(visualiza_estoque(estoque_atualizado.csv))
        

elif acao == "Realizar Venda":
    produtos_possiveis = pd.read_csv('base_original_produtos_naturais.csv')['Produto'].sort_values().unique()
    
    with st.form("form_venda"):
        st.subheader("Formulário de Venda")
        st.write("Selecione os produtos e a quantidade:")
        produto = st.selectbox("Selecione o produto", produtos_possiveis)
        total_vendido = st.number_input("Quantidade vendida", min_value=0, step=1)
        submit_button = st.form_submit_button(label = "Registrar Venda")
        
        venda = None
        
        if submit_button:
            venda = realiza_venda(produto, total_vendido)
            
        if venda is not None:
            if venda is True:
                st.success(f"Venda registrada com sucesso de {total_vendido} unidades do produto {produto}.")
            else:
                st.error(f"Erro ao registrar venda de {total_vendido} unidades do produto {produto}. Verifique o estoque.")
                
elif acao == "Relatório de Vendas":
    st.subheader("Relatório de Vendas")
    dict_analise = relatorio_vendas()
    
    st.write(f"Valor toal vendido: R$ {dict_analise['valor_total_vendido']:.2f}")
    st.write(f"Total de vendas: {dict_analise['total_vendas']}")
    st.write(f"Ticket médio: R$ {dict_analise['ticket_medio']:.2f}")
    st.write(f"Produtos mais vendidos (R$): {dict_analise['produtos_mais_vendidos_reais']}")
    st.write(f"Produtos mais vendidos (KG): {dict_analise['produtos_mais_vendidos_kilos']}")