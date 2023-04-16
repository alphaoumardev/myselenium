import scrapy
from scrapy.spiders import Spider


class ProductsSpider(scrapy.Spider):
    # spider_name = "products"
    name = "products"
    start_urls = ['https://www.whiskyshop.com/single-malt-scotch-whisky/distilleries/macallan']

    # def parse(self, response, **kwargs):
    #     page = response.url.split('/')[-1]
    #     pathname = 'posts-%s.html' % page
    #     with open(pathname, 'wb') as f:
    #         f.write(response.body)

    def parse(self, response, **kwargs):
        for product in response.css('div.product-item-info'):
            try:
                yield {
                    'name': product.css('a.product-item-link::text').get(),
                    'price': product.css('span.price::text').get().replace('£', '$'),
                    'link':  product.css('a.product-item-link').attrib['href'],
                }
            except:
                yield {
                    'name': product.css('a.product-item-link::text').get(),
                    'price': 'Sold out',
                    'link': product.css('a.product-item-link').attrib['href'],
                }
# import scrapy
#
#
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#         'http://quotes.toscrape.com/page/2/',
#     ]
#
#     def parse(self, response, **kwargs):
#         page = response.url.split("/")[-2]
#         filename = f'quotes-{page}.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)
