# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from wordpress import post
import json,re
class WordpressPipeline(object):



    def process_item(self, item, spider):
        print('-------:'+spider.name)
        # line =[item['title'],item['img'],item['header'],item['content']]
        # self.ws.append(line)
        # self.wb.save('wordperss.xlsx')
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

            else :
                pat = re.compile('<[^>]+>', re.S)
                item['content'] = pat.sub('',item['content'])
                post.autoPost(item['img'],item['title'],item['tag'],item['content'],item['download'])
                # f = open('item.json','a',encoding='utf-8')
                # f.write(json.dumps(dict(item), ensure_ascii=False)+'\n')
                return item
