from bs4 import BeautifulSoup
import requests
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scraper_utils_functions
import streamlit as st
from datetime import date


DEFAULT_COMPANIES = ['AAPL', 'AMZN', 'INTC', 'GOOG', 'CSCO']
data_content = []

def fetch_default(array = DEFAULT_COMPANIES ):
  data = yf.download(array, start='2021-01-01', end=date.today())
  data = data[-200:]
  for i,v in enumerate(data):
    if i in range(0,5) or i in range(25,30):
      data_content.append(data[v])
  df = pd.DataFrame(data_content).T
  return df


def fetch_info(symbol):
  url_profile = f'https://finance.yahoo.com/quote/{symbol}/profile?p={symbol}'
  try:
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
  except:
    print("Bad request! An exxeption ocorred")
    return None


def fetch_company_data_history(symbol):
  data = yf.download(symbol, period='1mo')['Adj Close']
  return data


def render_graph(arg, array):
  my_chart = st.line_chart(fetch_default(array)[arg][array[0]])
  for company in array[1:]:
    my_chart.add_rows(fetch_default(array)[arg][company])
