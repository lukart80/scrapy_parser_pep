import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        section = response.css('#index-by-category')
        links = section.css('td.num a::attr(href)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        item = PepParseItem(
            number=response.css('#pep-content dd::text').get().strip(''""''),
            name=response.css('#pep-content dd.field-even::text').get(),
            status=response
            .xpath('//dt[contains(text(), "Status")]/following-sibling::dd['
                   '1]/text()')
            .get()



        )
        yield item
