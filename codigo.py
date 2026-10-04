#TITULO (SISTEMA DE VENDAS)
#Seccao cadastrar vendas
    #Campo Data
    #Campo Vendedor(Ana, Bruno, Carla)
    #Campo Produto (Produto A, Produto B, Produto C)
    #Quantidade 
    #Valor
    #Botao Cadastrar Venda
        #Ao clicar no botao cadastrar venda, a venda deve ser adicionada a tabela de vendas cadastradas e o faturamento total deve ser atualizado.
#Seccao vendas cadastradas
    #Tabela Com as Vendas
#Secao Do Dashboard
    #Card/Metrica = Faturamento Total
    #Grafico De Barra/Coluna -> Venda por Vendedor
    #Grafico de Pizza -> Venda por Produto



#streamlit = permite criar esse sites com python puro e ebm bonito
#pandas = trabalha com base de dados
#plotly = serve para criar graficos 

import streamlit as st #deves estudar isso
import pandas as pd #trabalha cobase de dados no python
import plotly.express as px #criar graficos (ele tem varios graficos dentro de si)


#Carregar A Base de Vendas o botao cadastar dadsod eve ser ja colocada aqui ou sej a minha base de dados deve ser ela ja carrregada aqui
tabela_vendas = pd.read_csv("vendas.csv") #pd.read_csv = ler um arquivo csv, sep=";" = separador do arquivo csv



#TITULO (SISTEMA DE VENDAS) usamos o streamlit para criar o titulo do site
st.title("Sistema De Vendas") #(#) significaque ele vai colocar o maior titulo que ele conseguir


#SECCAO CADASTRO DE VENDAS

st.sidebar.subheader("Cadastrar Vendas") #(##) significa que ele vai colocar um titulo menor que o anterior
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Iphone", "NOTEBOOK", "IMOVEIS", "Fone", "Notebook", "Celular"])
quantidade = st.sidebar.number_input("Quantidade", min_value=0, step=1)
valor = st.sidebar.number_input("Valor", min_value=0.0, step=0.01)
botao_cadastrar = st.sidebar.button("Cadastrar Venda") #(##) significa que ele vai colocar um titulo menor que o anterior
#LOGICAD DO BOTAO CADASTRAR VENDA
if botao_cadastrar:
    if valor <= 0 or quantidade <= 0 or vendedor == "" or produto == "":
        st.warning("Venda com erros de preenchimento. Verifique os campos e tente novamente.")
    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False) #index=False = nao vai colocar o index da tabela
        st.success("Venda Cadastrada com sucesso!")


#SECCAO VISUALIZAR VENDAS
st.subheader("Vendas Cadastradas") #(##) significa que ele vai colocar um titulo menor que o anterior
st.dataframe(tabela_vendas) #Ele e uma tabela do pandas, ele o pandas chama as sua stabrla sd e dtaframe

id_venda = st.number_input("ID Venda", step=1)
botao_pesquisar = st.button("Editar") #(##) significa que ele vai colocar um titulo menor que o anterior

#SECCAO DASHBOARD
st.subheader("Dashboard") #(##) significa que ele vai colocar um titulo menor que o anterior
#Card/Metrica = Faturamento Total
faturamento = tabela_vendas["valor"].sum()  #soma todos os valores da coluna valor
#NAO SE USA PRINT, POR QUE ELE NAO MOSTRA NADA DENTRO DO MEU SITE SIMPLESMENTE MOSTRA COISAS NO MEU CMD, PARA MOSTRAR DENTRO DO SITE SE USA O st.write
st.metric("Faturamento Total", f"R${faturamento:.2f}") #st.metric = mostra uma metrica dentro do site, f"R${faturamento:.border=,2f}" = formata o valor para duas casas decimais e coloca o simbolo de real



#Grafico De Barra/Coluna -> Venda por Vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto") #text_auto=True = mostra o valor de cada barra
st.plotly_chart(grafico1) #plotly_chart = mostra o grafico dentro do site

#Grafico de Pizza -> Venda por Produt
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5) #text_auto=True = mostra o valor de cada barra
st.plotly_chart(grafico2) #plotly_chart = mostra o grafico dentro do site

#NO CMD SE COLOCA "streamlit run codigo.py" PARA RODAR O PROGRAMA


