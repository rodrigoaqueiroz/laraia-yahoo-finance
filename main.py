import streamlit as st
import scraper


stock = ['AAPL', 'AMZN', 'INTC', 'GOOG', 'CSCO']

search_btn = False

if st.sidebar.checkbox("Deseja procurar alguma ação?"):
    symbol = st.sidebar.text_input("Dígite o símbolo da ação desejada")
    if len(symbol) == 4:
      new_company_info = scraper.fetch_info(symbol)
      stock.append(symbol)
    search_btn = st.sidebar.button('Buscar')     


def get_new(symbol):
  if new_company_info != None:
    st.header(symbol)
    new_graph = scraper.fetch_company_data_history(chart_data, symbol)
    my_chart = st.line_chart(new_graph[chart_data], height=400, width=400)
    st.header(f'Informações: {stock_symbol_info}')
    st.text(scraper.fetch_info(symbol))
  return my_chart

stock_symbol_info = st.sidebar.selectbox(
  'Informações da ação',
  ['', *stock],
  )

stock_chart = st.sidebar.multiselect(
  'Ações para mostrar no gráfico',
  scraper.DEFAULT_COMPANIES,
  default=scraper.DEFAULT_COMPANIES
  )

chart_data = st.sidebar.radio(
  'Gráfico do volume ou da cotação de fechamento ajustado', ('Volume', 'Adj Close')
  )

def main():
  if search_btn: get_new(str(symbol))
  else:
    st.header('Gráficos')
    if len(stock_chart) > 0: 
      scraper.render_graph(chart_data, [*stock_chart])
    if (stock_symbol_info): 
      st.header(f'Informações: {stock_symbol_info}')
      st.text(scraper.fetch_info(stock_symbol_info))


if __name__ == "__main__":
    main()
