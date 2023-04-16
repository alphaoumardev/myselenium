import scrapy
from ..items import ScraponeItem
from scrapy.loader import ItemLoader


class TitleSpider(scrapy.Spider):
    name = 'title'
    allowed_domains = ['magnatiles.com']
    start_urls = ['https://www.magnatiles.com/products/page/1']

    def parse(self, response, **kwargs):
        products = response.css('ul.products li')
        for p in products:
            il = ItemLoader(item=ScraponeItem(), selector=p)
            il.add_css('sku', 'a::attr(data-product_sku)')
            il.add_css('name', 'h2')
            il.add_css('price', 'span.price bdi')
            il.add_css('link', 'a::attr(href)')
            yield il.load_item()
            # // *[ @ id = "productTitle"]

            # yield {
            #     "name": p.css('h2::text').getall(),
            #     "sku": response.css('ul.products li a::attr(data-product_sku)').getall(),
            #     "price": p.css('span.price bdi::text').getall()
            # }
        next_page = response.css("ul.page-numbers a.next::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
