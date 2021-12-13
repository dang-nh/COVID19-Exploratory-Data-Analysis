import scrapy


class AvgRainfallSpider(scrapy.Spider):
    name = 'avg_rainfall'
    allowed_domains = ['https://en.wikipedia.org/wiki/List_of_countries_by_average_annual_precipitation']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_countries_by_average_annual_precipitation']

    def parse(self, response):
        countries = response.xpath("//tr")

        for country in countries:
            name = country.xpath("(.//td)[2]/span/a/text()").get()
            avg_rainfall = country.xpath("(.//td)[3]/text()").get()

            yield {
                'name': name,
                'avg_rainfall': avg_rainfall,
            }
