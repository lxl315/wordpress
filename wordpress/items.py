# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WordpressItem(scrapy.Item):
    """
    bookset爬虫对应的 item
    定义要保存的字段
    """
    title = scrapy.Field()
    content = scrapy.Field()
    tag = scrapy.Field()
    img = scrapy.Field()
    header = scrapy.Field()
    download = scrapy.Field()

class MeBookItem(scrapy.Item):
    """
    mebook爬虫对应的 item
    定义要保存的字段
    """
    title = scrapy.Field()
    content = scrapy.Field()
    tag = scrapy.Field()
    img = scrapy.Field()
    download = scrapy.Field()