# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AverageTemperatureItem(scrapy.Item):
    country_name = scrapy.Field()
    avg_temp = scrapy.Field()
