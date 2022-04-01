import scrapy
from population.items import PopulationItem


class PopSpider(scrapy.Spider):
    name = 'pop'
    allowed_domains = ['worldpopulationreview.com/countries']
    start_urls = ['https://worldpopulationreview.com/countries']

    def parse(self, response):
        countries = response.xpath("//tr")

        for country in countries:
            item = PopulationItem()
            item['country_name'] = country.xpath(".//td[2]/a/text()").get()
            item['population'] = country.xpath(".//td[4]/text()").get()
            item['area'] = country.xpath(".//td[6]/text()").get()
            yield item
