import itertools

import pandas.io.json
from requests_html import HTMLSession
# import chompjs
import pandas as ps

# session = HTMLSession()
url = 'https://www.rei.com/s/road-trip-gear?ir=collection&page=2'
baseUrl = 'https://www.rei.com'


def fetch(page):
    r = HTMLSession().get(f'https://www.rei.com/s/road-trip-gear?ir=collection&page={page}')
    result = [baseUrl + link.attrs['href'] for link in r.html.find('#search-results > ul > li > a')]
    return list(dict.fromkeys(result))


def parse_product(url):
    r = HTMLSession().get(url)
    details = r.html.find('script[type=application/ld+json]')
    data = chompjs.parse - js - object(details.text)
    return data


def main():
    return fetch(1)


if __name__ == '__main__':
    df = ps.json_normalize(main())
    df.to_csv('rei.csv', index=False)
    print("done")
