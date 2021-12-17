import scrapy
from average_rainfall.items import AverageRainfallItem
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class AvgRainfallSpider(scrapy.Spider):
    name = 'avg_rainfall'
    allowed_domains = ['data.worldbank.org/indicator/AG.LND.PRCP.MM']
    start_urls = ['http://data.worldbank.org/indicator/AG.LND.PRCP.MM']

    def __init__(self):
        s = Service("../average_rainfall/chromedriver.exe")

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options, service=s)
        driver.get("http://data.worldbank.org/indicator/AG.LND.PRCP.MM")

        self.html = driver.page_source

    def parse(self, response):
        resp = Selector(text=self.html)
        # countries = response.xpath("//*[@class='item']")

        for country in resp.xpath("//*[@class='item']"):
            item = AverageRainfallItem()
            item['country_name'] = country.xpath(".//div[1]/a/text()").get()
            item['avg_rainfall'] = country.xpath(".//div[3]/text()").get()
            yield item
