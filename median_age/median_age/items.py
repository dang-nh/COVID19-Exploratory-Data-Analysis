# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MedianAgeItem(scrapy.Item):
    country_name = scrapy.Field()
    median_age = scrapy.Field()
