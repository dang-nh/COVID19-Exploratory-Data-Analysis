import scrapy


class GdpSpider(scrapy.Spider):
    name = 'gdp'
    allowed_domains = ['https://www.worldometers.info/gdp/gdp-by-country']
    start_urls = ['https://www.worldometers.info/gdp/gdp-by-country/']

    def parse(self, response):
        countries = response.xpath("//tr")

        for country in countries:
            name = country.xpath("(.//td)[2]/a/text()").get()
            gdp = country.xpath("(.//td)[3]/text()").get()
            gdp_growth = country.xpath("(.//td)[5]/text()").get()
            gdp_per_capita = country.xpath("(.//td)[7]/text()").get()
            yield {
                'name': name,
                'gdp': gdp,
                'gdp_growth': gdp_growth,
                'gdp_per_capita': gdp_per_capita,
            }
