import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class StringencyIdxSpiderSelenium(scrapy.Spider):
    name = 'stringency_idx_selenium'
    allowed_domains = ['ourworldindata.org/grapher/covid-stringency-index']
    start_urls = ['https://ourworldindata.org/grapher/covid-stringency-index']

    def __init__(self):
        s = Service("../crawler/crawler/spiders/chromedriver.exe")

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options, service=s)
        driver.get("https://ourworldindata.org/grapher/covid-stringency-index")

        table_tab = driver.find_element(By.XPATH, "//nav/ul/li[3]/a")
        table_tab.click()

        self.html = driver.page_source

    def parse(self, response):
        resp = Selector(text=self.html)
        print(type(resp))
        for country in resp.xpath("//tbody/tr"):
            yield {
                'name': country.xpath(".//td[@class='entity sorted']/text()").get(),
                'stringency_index': country.xpath(".//td[3]/text()").get(),
                # 'stringency_index': country.xpath(".//td[3]/text()").get(),
            }


