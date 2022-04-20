import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
import streamlit as st
import scraper

stocks = ['AAPL', 'AMZN', 'INTC', 'GOOG', 'CSCO']

# data= yf.download(['GOOG', 'META'], start='2021-12-10', end='2021-12-30', groupby='ticker')
# print(data.head)
def main():
     st.title("Gráficos")    
     

if st.sidebar.checkbox("Deseja procurar alguma ação?"):
    symbol = st.sidebar.text_input("Dígite o símbolo da ação desejada")
    # if len(symbol) != 4:
    #     st.error('Digite o símbolo de 4 digitos: ex.: AAPL') 
st.sidebar.multiselect('Ações', [*scraper.DEFAULT_COMPANIES], default = [*scraper.DEFAULT_COMPANIES])


if __name__ == "__main__":
    main()


