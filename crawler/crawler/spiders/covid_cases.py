import scrapy


class CovidCasesSpider(scrapy.Spider):
    name = 'covid_cases'
    allowed_domains = ['https://www.worldometers.info/coronavirus/#countries']
    start_urls = ['https://www.worldometers.info/coronavirus/#countries/']

    def parse(self, response):
        countries = response.xpath("//tr")

        for country in countries:
            name = country.xpath("(.//td)[2]/a/text()").get()
            total_case = country.xpath("(.//td)[3]/text()").get()
            total_deaths = country.xpath("(.//td)[5]/text()").get()
            total_recovered = country.xpath("(.//td)[7]/text()").get()
            active_cases = country.xpath("(.//td)[9]/text()").get()
            serious_critical = country.xpath("(.//td)[10]/text()").get()
            yield {
                'name': name,
                'total_case': total_case,
                'total_deaths': total_deaths,
                'total_recovered': total_recovered,
                'active_cases': active_cases,
                'serious_critical': serious_critical
            }
