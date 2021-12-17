# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class PopulationPipeline:
    sea_countries = ['Vietnam', 'Indonesia', 'Malaysia', 'Laos',
                     'Cambodia', 'Thailand', 'Singapore', 'Myanmar',
                     'Brunei', 'Timor']

    def process_item(self, item, spider):
        if any(country in item['country_name'] for country in self.sea_countries):
            return item
        else:
            raise DropItem("This country is not in Sout East Asia")
