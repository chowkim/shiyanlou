# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class ShiyanlougithubSpider(scrapy.Spider):
    name = 'shiyanlougithub'
    allow_domains = ['https://github.com/']
    
    @property
    def start_urls(self):
        stat_urls = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (stat_urls.format(i) for i in range(1, 5))

    def parse(self, response):
        for url in response.css('li.col-12'):
            item = ShiyanlouItem()
            item['name'] = url.css('div.d-inline-block.mb-1 a::text').re_first('[^\s]+[\w]*')
            item['update_time'] = url.xpath('.//relative-time/@datetime').extract_first()
            git_url = response.urljoin(url.xpath('//*[@id="user-repositories-list"]/ul/li/div/h3/a/@href').extract_first())
            request = scrapy.Request(git_url, callback=self.parse_info)
            request.meta['item'] = item
            yield request

    @staticmethod
    def parse_info(self, response):
        item = response.meta['item']
        for number in response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[3]/div/div/ul/li'):
            type_text = number.xpath('.//a/text()').re_first('\n\s*(.*)\n')
            number_text = number.xpath('.//span[@class="num text-emphasized"]/text()').re_first('\n\s*(.*)\n')
            if type_text and number_text:
                number_text = number_text.replace(',', '')
                if type_text in ('commit', 'commits'):
                    item['commits'] = int(number_text)
                elif type_text in ('branch', 'branches'):
                    item['branches'] = int(number_text)
                elif type_text in ('release', 'releases'):
                    item['releases'] = int(number_text)
        yield item
