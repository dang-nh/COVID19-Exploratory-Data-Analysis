import scrapy


class MedAgeSpider(scrapy.Spider):
    name = 'med_age'
    allowed_domains = ['https://www.worlddata.info/average-age.php']
    start_urls = ['https://www.worlddata.info/average-age.php/']

    def parse(self, response):
        countries = response.xpath("//tr")

        for country in countries:
            name = country.xpath("(.//td)[1]/a/text()").get()
            median_age = country.xpath("(.//td)[2]/text()").get()
            pop_under_20 = country.xpath("(.//td)[3]/text()").get()
            life = country.xpath("(.//td)[4]/text()").get()
            yield {
                'name': name,
                'median_age': median_age,
                'pop_under_20': pop_under_20,
                'life': life,
            }

