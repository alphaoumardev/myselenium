import scrapy
import json


class GlassSpider(scrapy.Spider):
    name = 'glass'
    allowed_domains = ['sunglasshut.com']
    start_urls = ['https://www.sunglasshut.com/us/mens-sunglasses']

    def parse(self, response, **kwargs):
        # print(response.body.decode('utf-8'))
        data = json.loads(response.body)
        yield from data['plpView']['products']['products']['product']
        next_page = data['plpView']['nextPageUrl']
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
