import pandas as pd
import streamlit as st
import os
import json

def inicializa_estoque(estoque_base: str = 'base_original_produtos_naturais.csv') -> None:
    
    if not os.path.exists("controle_estoque"):
        os.makedirs("controle_estoque")
        
    if not os.path.exists("controle_estoque/estoque_0.json"):
        print("Arquivo estoque_0.json não encontrado")
        
        # como eu leio um arquivo que não existe?
        estoque = pd.read_csv(estoque_0)
        # Cria um dicionario em que a chave é o produto e o valor é o estoque
        # Mas pq eu preciso do zip?
        dict_estoque = dict(zip(estoque['Produto'], estoque['Estoque (kg)']))
        
        # Dump  é usado para salvar um objeto Python em um arquivo JSON
        json.dump(dict_estoque, open("controle_estoque/estoque_0.json", "w"), ensure_ascii=True)
        print("Estoque inicializado com sucesso!")
        
    else:
        print("Estoque já inicializado, não é necessário reinicializar.")
        
def visualiza_estoque() -> pd.DataFrame:
    
    inicializa_estoque()
    
    estoques = sorted(os.listdir("controle_estoque"))
    ultimo_estoque = estoques[-1]  # Pega o último arquivo de estoque
    
    estoque_atual = json.load(open(f"controle_estoque/{ultimo_estoque}", "r"))
    
    df_estoque = pd.DataFrame(estoque_atual.items(), columns=['Produto', 'Estoque (kg)'])
    
    return df_estoque

def atualiza_estoque(venda: dict) -> None:
        
    # Lê o último arquivo de estoque
    estoques = sorted(os.listdir("controle_estoque"))
    ultimo_estoque = estoques[-1]
    i = int(ultimo_estoque.split('_')[1].split('.')[0]) + 1
    
    estoque_atual = json.load(open(f"controle_estoque/{ultimo_estoque}", "r"))
    
    estoque_atual[venda['produto']] -= venda['quantidade']
    
    json.dump(estoque_atual, open(f"controle_estoque/estoque_{i}.json", "w"), ensure_ascii=True)
    
def verifica_estoque(venda: dict) -> bool:
    
    inicializa_estoque()
    
    estoques = sorted(os.listdir("controle_estoque"))
    ultimo_estoque = estoques[-1]  # Pega o último arquivo de estoque
    
    estoque_atual = json.load(open(f"controle_estoque/{ultimo_estoque}", "r"))
    
    if venda['produto'] in estoque_atual and [venda['total_vendido']] <= estoque_atual[venda['produto']]:
        return True
    else:
        return False
    
def realiza_venda(produto, total_vendido) -> bool:
    
    obj_venda = {"produto": produto, "total_vendido": total_vendido}
    
    if not os.path.exists("controle_vendas"):
        os.makedirs("controle_vendas")
        
    vendas_efetivadas = os.listdir("controle_vendas")
    
    if len(vendas_efetivadas) == 0:
        i = 0
    else:
        i = int(vendas_efetivadas[-1].split('_')[1].split('.')[0]) + 1
    
    venda = {"produto": produto, "total_vendido": total_vendido}
    
    venda_possivel = verifica_estoque(venda)
    
    if venda_possivel:
        json.dump(obj_venda, open(f"controle_vendas/venda_{i}.json", "w"), ensure_ascii=True)
        atualiza_estoque(venda)
        return True
    else:
        return False
    
def relatorio_vendas() -> dict:
    
    vendas = os.listdir("controle_vendas")
    vendas_df = pd.DataFrame()
    
    for venda in vendas:
        with open(f"controle_vendas/{venda}", "r") as f:
            venda_json = json.load(f)
            df_venda = pd.DataFrame([venda_json])
            vendas_df = pd.concat([vendas_df, df_venda], ignore_index=True)
        
    df_precos = pd.read_csv('base_preco_produtos_naturais.csv')[['Produto', 'Preço (por kg)']]
    vendas_df = vendas_df.merge(df_precos, left_on='Produto', right_on='Produto', how='left')
    
    vendas_df['valor_venda'] = vendas_df['total_vendido'] * vendas_df['Preço (por kg)']
    
    agg_vendas = vendas_df.groupby(['produto']).agg({'total_vendido': 'sum', 'valor_venda': 'sum', 'Produto': 'count'})
    st.table(vendas_df[['produto', 'total_vendido', 'Preço (kg)' 'valor_venda']])
    
    mais_vendido_vendas = agg_vendas[agg_vendas['Produto']==agg_vendas['Produto'].max()].index
    mais_vendido_reais = agg_vendas[agg_vendas['valor_venda']==agg_vendas['valor_venda'].max()].index
    mais_vendido_kg = agg_vendas[agg_vendas['total_vendido']==agg_vendas['total_vendido'].max()].index

    dict_analise_vendas = {
        'valor_total_vendido': vendas_df['valor_venda'].sum(),
        'total_vendas': len(vendas_df),
        'ticket_medio': vendas_df['valor_venda'].mean(),
        'produtos_mais_vendidos_vendas': ','.join(mais_vendido_vendas),
        'produtos_mais_vendidos_reais': ','.join(mais_vendido_reais),
        'produtos_mais_vendidos_kilos': ','.join(mais_vendido_kg),
    }
    
    return dict_analise_vendas