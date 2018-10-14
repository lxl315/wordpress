# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json
class WordpressPipeline(object):
    # wb = workbook.Workbook()
    # ws = wb.active
    # ws.append(['title','img','header','content'])
    def __init__(self):
        f=open('items.txt', 'w',encoding='utf-8')
        self.file =f


    def process_item(self, item, spider):
        # line =[item['title'],item['img'],item['header'],item['content']]
        # self.ws.append(line)
        # self.wb.save('wordperss.xlsx')
        if not item['title']:
            raise DropItem("Duplicate item found: %s" % item)
        elif not item['content']:
            raise DropItem("Duplicate item found: %s" % item)
        else :

            line = json.dumps(dict(item),indent=2,ensure_ascii=False)+'\n'
            self.file.write(line)
            return item

