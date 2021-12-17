# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AverageRainfallItem(scrapy.Item):
    country_name = scrapy.Field()
    avg_rainfall = scrapy.Field()
