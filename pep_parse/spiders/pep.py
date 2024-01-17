from urllib.parse import urljoin

import scrapy


from pep_parse.items import PepParseItem
from pep_parse.settings import (
    PEP_NAME,
    PEP_DOMAINS,
    PEP_URLS
)


class PepSpider(scrapy.Spider):
    name = PEP_NAME
    allowed_domains = PEP_DOMAINS
    start_urls = PEP_URLS

    def parse(self, response):
        section_tag = response.css('section#numerical-index')
        table_body = section_tag.css('tbody')
        for row in table_body.css('tr'):
            pep_link = urljoin(
                self.start_urls[0],
                row.css('a::attr(href)').get()
            )
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        num_and_name = (
            response.css('h1.page-title::text').re(r'^PEP (.*\d) . (.*)')
        )
        info_block = response.css('dl.rfc2822')
        status = info_block.css('dt:contains("Status") + dd abbr::text').get()
        date = {
            'name': num_and_name[1],
            'number': num_and_name[0],
            'status': status
        }
        yield PepParseItem(date)
