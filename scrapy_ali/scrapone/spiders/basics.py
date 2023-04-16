from abc import ABC
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


# https://sipwhiskey.com/collections/champagne
# https://sipwhiskey.com/collections/champagne/products/moet-chandon-ice-imperial
class BasicSpider(CrawlSpider, ABC):
    name = "sip"
    allowed_domains = ['sipwhiskey.com/']
    start_urls = ['https://sipwhiskey.com//']

    rule = (
        Rule(LinkExtractor(allow='collections/champagne', deny='products')),
        Rule(LinkExtractor(allow='products'), callback='parse_item')
    )

    def parse_item(self, response):
        yield {
            "name": response.css('div.vendor a::text').get(),
            "title": response.css('h1.title::text').get(),
            "price": response.css('span.price::text').get(),

        }
