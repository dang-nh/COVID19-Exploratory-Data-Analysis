import scrapy
from covid.items import CovidItem

class Covid19Spider(scrapy.Spider):
    name = 'covid19'
    allowed_domains = ['www.worldometers.info/coronavirus/#countries']
    start_urls = ['https://www.worldometers.info/coronavirus/#countries/']

    def parse(self, response):
        countries = response.xpath("//*[@id='main_table_countries_today']/tbody[1]/tr")

        for country in countries:
            item = CovidItem()
            item['country_name'] = country.xpath(".//td[2]/a/text()").get()
            item['total_cases'] = country.xpath(".//td[3]/text()").get()
            item['total_deaths'] = country.xpath(".//td[5]/text()").get()
            item['total_recovered'] = country.xpath(".//td[7]/text()").get()
            item['active_cases'] = country.xpath(".//td[9]/text()").get()
            yield item

