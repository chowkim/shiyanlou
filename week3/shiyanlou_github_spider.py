#!/usr/bin/env python3
import scrapy


class ShiYanLouCodeSpider(scrapy.Spider):

    name = 'ShiYanLouCodeSpider'

    @property
    def start_urls(self):
        start_urls = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return(start_urls.format(i) for i in range(1, 5))

    def parse(self, response):
        for url in response.css('li.col-12.d-block.width-full.py-4.border-bottom.public.source'):
            yield {
                    'name': url.css('div.d-inline-block.mb-1 a::text').re_first('[^\s]+[\w]*'),
                    'update_time': url.xpath('//*[@id="user-repositories-list"]/ul/li/div/relative-time/@datetime').extract_first()
                    }
