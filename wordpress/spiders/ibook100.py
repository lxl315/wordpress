# -*- coding: utf-8 -*-
import scrapy
from  scrapy import Request
from wordpress.items import WordpressItem

class Ibook100Spider(scrapy.Spider):
    name = 'ibook100'
    allowed_domains = ['kgbook.com']

    def start_requests(self):
        pages = []
        for i in range(2, 81):
            url = 'https://kgbook.com/list/index_%s.html' % i
            page = scrapy.Request(url)
            pages.append(page)
        return pages

    def parse(self, response):
        """
        解析每一首页列表
        :param response:
        :return:
        """
        for url in response.css('.list-title>a::attr(href)').extract():
            yield Request(url, self.parse_html)



    def parse_html(self, response):
        """
        解析每一篇文章详细页面
        :param response:
        :return:
        """

        item = WordpressItem()
        item['title'] =  response.xpath('//*[@id="content"]/h1/text()').extract_first()
        item['img'] = 'https://kgbook.com'+response.xpath('//*[@id="news_picture"]/img/@src').extract_first()
        item['content'] = response.css('#introduction > p::text').extract_first()
        list=[]
        tag = response.xpath('//*[@id="location"]/a/text()').extract()[-1]
        list.append(tag)
        item['tag']=list
        item['header'] = response.css('#news_details').extract_first()
        down = response.xpath('//*[@id="introduction"]/a').extract()[0:-1]
        item['download']=''.join(down)
        yield item
