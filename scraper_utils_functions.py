def get_full_name(soup):
  return soup.find('h3', class_= 'Fz(m)').text


def get_full_adress(soup):
  get_adress = soup.find('p', class_= 'D(ib)')
  full_address = ''
  for index, value in enumerate(get_adress):
    if index in [0,2,4]:
      full_address += f'{value}. '
  return full_address


def get_phone(soup):
  phone = soup.find('p', class_= 'D(ib)').find('a', class_ = 'C($linkColor)').text
  return phone


def get_sector(soup):
  sector = soup.find('span', class_= 'Fw(600)').text
  return sector


def get_industry(soup):
  sector = soup.find_all('span', class_= 'Fw(600)')[1].text
  return sector


def get_total_employees(soup):
  sector = soup.find_all('span', class_= 'Fw(600)')[-1].text
  return sector.replace(',','.')


def get_key_executives(soup):
  names = soup.find_all('tr', class_ = "Bdc($seperatorColor)")
  key_executive_names = [f"{name.find('td').text}\n" for name in names[1:]]
  return key_executive_names
