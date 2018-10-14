# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WordpressItem(scrapy.Item):
    """
    定义要保存的字段
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    tag = scrapy.Field()
    img = scrapy.Field()
    header = scrapy.Field()
    download = scrapy.Field()
