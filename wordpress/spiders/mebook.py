# -*- coding: utf-8 -*-
from  scrapy import Request
import scrapy,re
from wordpress.items import MeBookItem
"""
爬 mebook 网站
"""

class MebookSpider(scrapy.Spider):
    name = 'mebook'
    allowed_domains = ['mebook.cc']

    def start_requests(self):
        pages = []
        for i in range(501, 768):
            url = 'http://mebook.cc/page/%s' % i
            page = scrapy.Request(url)
            pages.append(page)
        return pages

    def parse(self, response):
        """
        解析首页列表
        :param response:
        :return:
        """
        for url in response.css('h2 a::attr(href)').extract():
            yield Request(url,self.parse_html,dont_filter=True)

        # nextpage = response.css('.next-page a::attr(href)').extract_first()
        # if nextpage:
        #     yield Request(nextpage,self.parse)

    def parse_html(self,response):
        """
        解析每一篇文章详细页面
        :param response:
        :return:
        """

        item = MeBookItem()
        item['title'] = title =response.css('h1::text').extract_first()
        item['img'] = response.xpath('//*[@id="content"]/p/img/@src').extract_first()
        result= response.xpath('//*[@id="content"]').extract_first()
        if result:
            item['content']= re.findall('内容简介(.*?)<div class="xydown_down_link">',result,re.S)[0]
        item['tag'] = response.xpath('//*[@id="primary"]/div/span/a/text()').extract()
        yield item

        downUrl = response.xpath('//*[@id="content"]/div/p/strong/a/@href').extract_first()
        yield Request(downUrl,meta={'item':item},callback=self.parse_down)


    def parse_down(self,response):
        item = response.meta['item']
        item['download'] = response.xpath('/html/body/div/p[6]').extract_first()+response.css('.list').extract_first()

        yield item

