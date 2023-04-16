from requests_html import HTMLSession
# import chompjs

# session = HTMLSession()
url = 'https://www.rei.com/s/road-trip-gear?ir=collection&page=2'
baseUrl = 'https://www.rei.com'
r = HTMLSession().get(url)
result = r.html.find('#search-results > ul > li > a')
products_links = []
for link in result:
    products_links.append(baseUrl + link.attrs['href'])
links = list(dict.fromkeys(products_links))
print(links)
