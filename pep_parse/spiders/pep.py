import re

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
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        raw_string = response.css('h1.page-title::text').get()
        group_string = re.search(r'^PEP (.*\d) . (.*)', raw_string)
        info_block = response.css('dl.rfc2822')
        date = {
            'name': group_string[1],
            'number': group_string[0],
            'status': info_block.css('dd:nth-child(4) abbr::text').get()
        }
        yield PepParseItem(date)
