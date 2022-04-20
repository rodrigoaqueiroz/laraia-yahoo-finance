from bs4 import BeautifulSoup
import requests
import yfinance as yf
import pandas as pd
import scraper_utils_functions


DEFAULT_COMPANIES = ['AAPL', 'AMZN', 'INTC', 'GOOG', 'CSCO']


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

  return info

print(fetch_info('AAPL'))