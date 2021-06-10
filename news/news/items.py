# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):

    title = scrapy.Field()
    sub_title = scrapy.Field()
    abstract = scrapy.Field()
    download_time = scrapy.Field()
