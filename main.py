from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

with open('C:\\Users\\1\\Desktop\\project\\API DATA\\COIN MARKET CAP\\api.py', 'r', encoding='utf-8') as file:
  API_KEY = file.read()

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1000',
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)

  for i in data['data']:
    print(i['name'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)