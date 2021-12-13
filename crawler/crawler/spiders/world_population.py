import scrapy
# from scrapy.selector import Selector
# from crawler.items import CrawlerItem


class WorldPopulationSpider(scrapy.Spider):
    name = 'world_population'
    allowed_domains = ['https://worldpopulationreview.com/countries']
    start_urls = ['https://worldpopulationreview.com/countries']

    def parse(self, response):
        countries = response.xpath("//tr")

        for country in countries:
            name = country.xpath("(.//td)[2]/a/text()").get()
            population_2021 = country.xpath("(.//td)[3]/text()").get()
            population_2020 = country.xpath("(.//td)[4]/text()").get()
            area = country.xpath("(.//td)[6]/text()").get()
            density = country.xpath("(.//td)[7]/text()").get()
            yield {
                'name': name,
                'population_2021': population_2021,
                'population_2020': population_2020,
                'area': area,
                'density': density
            }