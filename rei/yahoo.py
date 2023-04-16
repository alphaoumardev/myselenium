import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"}
url = 'https://finance.yahoo.com/cryptocurrencies'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title.text)
