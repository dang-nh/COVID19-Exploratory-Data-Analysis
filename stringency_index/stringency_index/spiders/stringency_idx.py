import scrapy
from stringency_index.items import StringencyIndexItem
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class StringencyIdxSpider(scrapy.Spider):
    name = 'stringency_idx'
    allowed_domains = ['ourworldindata.org/grapher/covid-stringency-index']
    start_urls = ['http://ourworldindata.org/grapher/covid-stringency-index/']

    def __init__(self):
        s = Service("../stringency_index/chromedriver.exe")

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options, service=s)
        driver.get("https://ourworldindata.org/grapher/covid-stringency-index")

        table_tab = driver.find_element(By.XPATH, "//nav/ul/li[3]/a")
        table_tab.click()

        self.html = driver.page_source

    def parse(self, response):
        resp = Selector(text=self.html)

        for country in resp.xpath("//tbody/tr"):
            item = StringencyIndexItem()
            item['country_name'] = country.xpath(".//td[@class='entity sorted']/text()").get()
            item['stringency_index'] = country.xpath(".//td[3]/text()").get()
            yield item
