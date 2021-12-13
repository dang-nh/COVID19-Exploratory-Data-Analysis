import scrapy


class StringencyIdxSpider(scrapy.Spider):
    name = 'stringency_idx'
    allowed_domains = ['https://ourworldindata.org/grapher/covid-stringency-index?tab=table']
    start_urls = ['https://ourworldindata.org/grapher/covid-stringency-index?tab=table/']

    def parse(self, response):
        countries = response.xpath("/tr")

        for country in countries:
            name = country.xpath("(.//td)[1]/text()").get()
            stringency_idx = country.xpath("(./td)[3]/text()").get()
            abs_change = country.xpath("(./td)[4]/text()").get()
            relative_change = country.xpath("(./td)[5]/text()").get()
            yield {
                'name': name,
                'stringency_idx': stringency_idx,
                'abs_change': abs_change,
                'relative_change': relative_change
            }
