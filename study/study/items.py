# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class abcitem(scrapy.Item):
    x = scrapy.Field()
    xt = scrapy.Field()
    y = scrapy.Field()
    yt = scrapy.Field()
    name = scrapy.Field()


class newsitem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()

class announcement(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()



class youtuMysqlItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
