# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class ShiyanlougithubSpider(scrapy.Spider):
    name = 'shiyanlougithub'
    @property
    def start_urls(self):
        stat_urls = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (stat_urls.format(i) for i in range(1, 5))

    def parse(self, response):
        for url in response.css('li.col-12'):
            item = ShiyanlouItem({
                'name': url.css('div.d-inline-block.mb-1 a::text').re_first('[^\s]+[\w]*'),
                'update_time': url.xpath('.//relative-time/@datetime').extract_first()
                })
            yield item
