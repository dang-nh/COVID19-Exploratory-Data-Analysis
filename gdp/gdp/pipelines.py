# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class GdpPipeline:
    sea_countries = ['Vietnam', 'Indonesia', 'Malaysia', 'Lao',
                     'Cambodia', 'Thailand', 'Singapore', 'Myanmar',
                     'Brunei', 'Timor','Philippines']

    def process_item(self, item, spider):
        for country in self.sea_countries:
            if country in item['country_name']:
                if country == 'Brunei':
                    item['country_name'] = 'Brunei'
                    return item
                elif country == 'Lao':
                    item['country_name'] = 'Laos'
                    return item
                elif country == 'Timor':
                    item['country_name'] = 'Timor Leste'
                    return item
                else:
                    return item
        raise DropItem("This country is not in Sout East Asia")
