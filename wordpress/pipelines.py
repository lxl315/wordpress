# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from wordpress import post
import re
class WordpressPipeline(object):
    def __init__(self):
        self.ids_seen = set()


    def process_item(self, item, spider):

        if spider.name == 'bookset':  #根据爬虫名判断 用那个pipliness
            if not item['title']:
                raise DropItem("Duplicate item found: %s" % item)
            elif not item['content']:
                raise DropItem("Duplicate item found: %s" % item)
            else :
                post.autoPost(item['img'],item['title'],item['tag'],item['content'],item['download'],header=item['header'])
                return item
        elif spider.name == 'mebook':
            if not item['title']:
                raise DropItem("Duplicate item found: %s" % item)

            elif item['title'] in self.ids_seen:
                raise DropItem("Duplicate item found: %s" % item)
            elif not item['download']:
                raise DropItem("Duplicate item found: %s" % item)
            else :
                self.ids_seen.add(item['title'])
                pat = re.compile('<[^>]+>', re.S)
                item['content'] = pat.sub('',item['content'])
                post.autoPost(item['img'],item['title'],item['tag'],item['content'],item['download'])

                return item
