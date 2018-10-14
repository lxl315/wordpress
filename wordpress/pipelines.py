# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from wordpress import post
class WordpressPipeline(object):



    def process_item(self, item, spider):
        # line =[item['title'],item['img'],item['header'],item['content']]
        # self.ws.append(line)
        # self.wb.save('wordperss.xlsx')
        if not item['title']:
            raise DropItem("Duplicate item found: %s" % item)
        elif not item['content']:
            raise DropItem("Duplicate item found: %s" % item)
        else :
            post.autoPost(item['img'],item['title'],item['header'],item['tag'],item['content'],item['download'])
            return item

