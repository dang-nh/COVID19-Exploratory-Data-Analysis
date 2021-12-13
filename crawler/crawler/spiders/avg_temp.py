import scrapy


class AvgTempSpider(scrapy.Spider):
    name = 'avg_temp'
    allowed_domains = ['https://worldpopulationreview.com/country-rankings/hottest-countries-in-the-world']
    start_urls = ['https://worldpopulationreview.com/country-rankings/hottest-countries-in-the-world/']

    def parse(self, response):
        countries = response.xpath("//tr")

        for country in countries:
            name = country.xpath("(.//td)[1]/a/text()").get()
            avg_temp = country.xpath("(.//td)[2]/text()").get()

            yield {
                'name': name,
                'avg_temp': avg_temp,
            }
