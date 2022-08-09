from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import excel


with open('C:\\Users\\1\\Desktop\\project\\API DATA\\COIN MARKET CAP\\api.py', 'r', encoding='utf-8') as file:
  API_KEY = file.read()


def main():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start': '1',
    'limit': '1000',
    'CMC_PRO_API_KEY': API_KEY,
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
    return data

  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


if __name__ == "__main__":
  data = main()
  excel.create_table(data)
