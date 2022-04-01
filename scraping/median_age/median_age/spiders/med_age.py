import scrapy
from median_age.items import MedianAgeItem


class MedAgeSpider(scrapy.Spider):
    name = 'med_age'
    allowed_domains = ['worldpopulationreview.com/country-rankings/median-age']
    start_urls = ['https://worldpopulationreview.com/country-rankings/median-age']

    def parse(self, response):
        countries = response.xpath("//tr")

        for country in countries:
            item = MedianAgeItem()
            item['country_name'] = country.xpath(".//td[1]/a/text()").get()
            item['median_age'] = country.xpath(".//td[2]/text()").get()
            yield item
