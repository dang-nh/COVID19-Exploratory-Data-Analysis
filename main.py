from scrapy import Spider
from scrapy.selector import Selector


class WorldPopulationSpider(Spider):
    name = 'world_population'
    allowed_domains = ['https://worldpopulationreview.com/countries']
    start_urls = ['https://worldpopulationreview.com/countries/']

    def parse(self, response):
        countries = Selector(response).xpath('//*[@id="popTable"]/div[1]/div/div/div/div/div[2]/table/tbody')

        for country in countries:
            item = CrawlerItem()

            item['rank'] = country.xpath(
                '//*[@id="popTable"]/div[1]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]')
            item['country'] = country.xpath(
                '//*[@id="popTable"]/div[1]/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]/a')


