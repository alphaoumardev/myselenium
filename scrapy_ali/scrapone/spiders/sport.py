import scrapy


class SportSpider(scrapy.Spider):
    name = 'sport'
    start_urls = ['https://www.neweracap.co.uk/en-gb/sports/american-football/']
    allowed_domains = ['neweracap.co.uk']

    def start_requests(self):
        yield scrapy.Request(f'https://www.neweracap.co.uk/en-gb/sports/american-football/{self.team}')

    def parse(self, response, **kwargs):
        products = response.css('div.product.product--listing')
        for product in products:
            yield {
                "name": product.css("p.product__name::text").get(),
                "price": product.css("p.product-detail__price::text").get(),
                "link": product.css("a::attr(href)").get()
            }
        next_page = response.css("a.pagination__next::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
