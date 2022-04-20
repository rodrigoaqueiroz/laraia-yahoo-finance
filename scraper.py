from bs4 import BeautifulSoup
import requests
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scraper_utils_functions
import streamlit as st
import seaborn as sns


DEFAULT_COMPANIES = ['AAPL', 'AMZN', 'INTC', 'GOOG', 'CSCO']
data_content = []

def fetch_default(array = DEFAULT_COMPANIES ):
  data = yf.download(array, period='1mo')
  for i,v in enumerate(data):
    if i in range(0,5) or i in range(25,30):
      # print(data[v])
      data_content.append(data[v])
  # print(data.columns[1])
  # return data
  df = pd.DataFrame(data_content).T
  return df


def graph(arg, array):
  plt.style.use('seaborn')
  plt.figure(figsize=(12,8))
  my_chart = st.line_chart(fetch_default()[arg][array[0]])
  for company in array[1:]:
    # sns.lineplot(data=fetch_default()[arg][company], x='arg' , y='company', hue="month")
    my_chart.add_rows(fetch_default()[arg][company])
    # st.line_chart(fetch_default()[arg][company])


def fetch_info(symbol):
  url_profile = f'https://finance.yahoo.com/quote/{symbol}/profile?p={symbol}'
  page = requests.get(url_profile, headers = {'User-agent': 'Mozilla/5.0'})
  soup = BeautifulSoup(page.content, 'html.parser')
  info = {
    'full_name': scraper_utils_functions.get_full_name(soup),
    'address': scraper_utils_functions.get_full_adress(soup),
    'phone': scraper_utils_functions.get_phone(soup),
    'sector': scraper_utils_functions.get_sector(soup),
    'industry': scraper_utils_functions.get_industry(soup),
    'total_employees': scraper_utils_functions.get_total_employees(soup),
    'key_executives': scraper_utils_functions.get_key_executives(soup),
  }

  company_info = (f"Nome: {info['full_name']}\nEndereço: {info['address']}\nPhone: {info['phone']}\nSector: {info['sector']}\nIndustry: {info['industry']}\nNúmero de funcionários: {info['total_employees']}\nPrincipais executivos: {''.join(info['key_executives']).rjust(20,'-')}")
  
  return company_info

# print(fetch_default(DEFAULT_COMPANIES))
print(fetch_default()['Adj Close']['AMZN'])
# print(data_content)
