#!/usr/bin/env python3
import scrapy


class ShiYanLouCodeSpider(scrapy.Spider):

    name = 'ShiYanLouCodeSpider'

    @property
    def start_urls(self):
        stat_urls = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (stat_urls.format(i) for i in range(1, 5))

    def parse(self, response):
        for url in response.css('li.col-12'):
            yield {
#                    'name': url.css('div.d-inline-block.mb-1 a::text').re_first('[^\s]+[\w]*'),
                    'name': url.xpath('.//a[contains(@itemprop, "name")]/text()').extract_first().strip(),
                    'update_time': url.xpath('.//relative-time/@datetime').extract_first()
                    }
