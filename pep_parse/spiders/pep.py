import scrapy

from urllib.parse import urljoin

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        section_tag = response.css('section#numerical-index')
        table_body = section_tag.css('tbody')
        for row in table_body.css('tr'):
            pep_link = urljoin(
                self.start_urls, row.css('td:nth-child(3) a::attr(href)')
            )
            status = response.follow(pep_link, callback=self.parse_status)
            date = {
                'name': row.css('td:nth-child(3) a::text').get(),
                'number': row.css('td:nth-child(2) a::text').get(),
                'status': status
            }
            yield PepParseItem(date)

    def parse_status(self, response):
        return response.css('dl.rfc2822 dd:nth-child(4) abbr::text').get()