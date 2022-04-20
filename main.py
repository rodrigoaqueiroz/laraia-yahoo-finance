import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
import streamlit as st
import scraper

stocks = ['AAPL', 'AMZN', 'INTC', 'GOOG', 'CSCO']

# data= yf.download(['GOOG', 'META'], start='2021-12-10', end='2021-12-30', groupby='ticker')
# print(data.head)
     
if st.sidebar.checkbox("Deseja procurar alguma ação?"):
    symbol = st.sidebar.text_input("Dígite o símbolo da ação desejada")
    # if len(symbol) != 4:
    #     st.error('Digite o símbolo de 4 digitos: ex.: AAPL') 
stock_symbol_info = st.sidebar.selectbox(
  'Informações da ação',
  ['', *scraper.DEFAULT_COMPANIES],
  )

stock_chart = st.sidebar.multiselect(
  'Ações para mostrar no gráfico',
  [*scraper.DEFAULT_COMPANIES],
  default = [*scraper.DEFAULT_COMPANIES]
  )
if (not stock_chart and stock_symbol_info): 
  st.title('Informações:')
  st.text(scraper.fetch_info(stock_symbol_info))



def main():
  scraper.graph('Adj Close', stocks)


if __name__ == "__main__":
    main()


