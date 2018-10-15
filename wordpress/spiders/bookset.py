# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from wordpress.items import WordpressItem


class BaiduSpider(scrapy.Spider):
    name = 'bookset'
    allowed_domains = ['bookset.me']
    start_urls = ['https://bookset.me/page/120']

    def parse(self, response):
        """
        解析每一首页列表
        :param response:
        :return:
        """
        for url in response.xpath('//*[@id="cardslist"]/div/div/h3/a/@href').extract():
            yield Request(url,self.parse_html)

        nextpage = response.css('.next-page a::attr(href)').extract_first()
        if nextpage:
            yield Request(nextpage,self.parse)

    def parse_html(self,response):
        """
        解析每一篇文章详细页面
        :param response:
        :return:
        """

        item = WordpressItem()
        item['title'] = response.css('h1 a::text').extract_first()
        item['img'] = response.xpath('//*[@id="mbm-book-page"]/span/img/@src').extract_first()
        result= response.xpath('//*[@id="mbm-book-page"]')
        if result:
            item['content']= result.re('<span class="mbm-book-excerpt-label">(.*?)</div>')[0]
        item['tag'] = response.css('.mbm-book-tag-text::text').extract()
        bookInfo = response.css('.mbm-book-details-outer div').extract_first()
        if bookInfo:
            item['header'] = bookInfo.replace('https://bookset.me','http://booksduo.com').replace('\\ax0','')
        item['download'] = response.xpath('//*[@id="mbm-book-links1"]/div/ul').extract_first()
        yield item