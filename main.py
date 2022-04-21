import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
import streamlit as st
import scraper


stock = ['AAPL', 'AMZN', 'INTC', 'GOOG', 'CSCO']

     
if st.sidebar.checkbox("Deseja procurar alguma ação?"):
    symbol = st.sidebar.text_input("Dígite o símbolo da ação desejada")
    if len(symbol) == 4:
      new_company_info = scraper.fetch_info(symbol)
      stock.append(symbol)
      if new_company_info != None:
        scraper.fetch_default(stock)


stock_symbol_info = st.sidebar.selectbox(
  'Informações da ação',
  ['', *stock],
  )

stock_chart = st.sidebar.multiselect(
  'Ações para mostrar no gráfico',
  stock,
  default=stock
  )

chart_data = st.sidebar.radio(
  'Gráfico do volume ou da cotação de fechamento ajustado', ('Volume', 'Adj Close')
  )


def main():
  if len(stock_chart) > 0: 
    scraper.render_graph(chart_data, [*stock_chart])
  if (stock_symbol_info): 
    st.title(f'Informações: {stock_symbol_info}')
    st.text(scraper.fetch_info(stock_symbol_info))


if __name__ == "__main__":
    main()

