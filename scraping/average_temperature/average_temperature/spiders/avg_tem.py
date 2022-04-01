import scrapy
from average_temperature.items import AverageTemperatureItem


class AvgTemSpider(scrapy.Spider):
    name = 'avg_temp'
    allowed_domains = ['worldpopulationreview.com/country-rankings/hottest-countries-in-the-world']
    start_urls = ['https://worldpopulationreview.com/country-rankings/hottest-countries-in-the-world']

    def parse(self, response):
        countries = response.xpath("//tr")

        for country in countries:
            item = AverageTemperatureItem()
            item['country_name'] = country.xpath(".//td[1]/a/text()").get()
            item['avg_temp'] = country.xpath(".//td[2]/text()").get()
            yield item
