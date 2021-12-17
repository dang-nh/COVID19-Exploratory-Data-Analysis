import scrapy
from gdp.items import GdpItem


class SeaGdpSpider(scrapy.Spider):
    name = 'sea_gdp'
    allowed_domains = ['www.worldometers.info/gdp/gdp-by-country']
    start_urls = ['https://www.worldometers.info/gdp/gdp-by-country']

    def parse(self, response):
        countries = response.xpath("//tr")

        for country in countries:
            item = GdpItem()
            item['country_name'] = country.xpath(".//td[2]/a/text()").get()
            item['gdp'] = country.xpath(".//td[3]/text()").get()
            yield item
