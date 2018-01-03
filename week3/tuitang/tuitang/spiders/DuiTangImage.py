# -*- coding: utf-8 -*-
import scrapy
import json
from tuitang.items import ImageItem


class DuitangimageSpider(scrapy.Spider):
	name = 'DuiTangImage'
	allowed_domains = ['https://www.duitang.com/']
	
	@property
	def start_urls(self):
		start_urls = 'https://www.duitang.com/napi/blog/list/by_filter_id/?include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Csender%2Calbum&filter_id=%E5%A4%B4%E5%83%8F&start={}'
		# stat_urls = (stat_url.format(i) for i in range(24, 48, 24))
		# for url in stat_urls:
		# 	print(url)
		return (start_urls.format(i) for i in range(0, 48, 24))
	
	def parse(self, response):
		# self.logger.info('hello world!')
		# self.logger.info(response)
		# self.logger.info(response.url)
		# yield response.url
		data = json.loads(response.text)
		# print(data)
		item = ImageItem()
		image_urls = []
		for d in data['data']['object_list']:
			image_urls.append(d['photo']['path'])
		item['image_urls'] = image_urls
		return item
