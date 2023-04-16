import scrapy
from scrapy.loader import ItemLoader
from ..items import Product


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['hub.wotokol.com']

    def start_requests(self):
        baseurl = "https://hub.wotokol.com/"
        with open('asins.csv') as f:
            for line in f:
                if not line.strip():
                    continue
                yield scrapy.Request(baseurl + line)

    def parse(self, response):
        loader = ItemLoader(item=Product(), response=response)
        loader.add_css('name', 'span#productTitle')
        loader.add_css('price', 'span.a-price span')
        yield loader.load_item()
