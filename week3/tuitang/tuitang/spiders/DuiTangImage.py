# -*- coding: utf-8 -*-
import scrapy
import json
from tuitang.items import ImageItem


class DuitangimageSpider(scrapy.Spider):
	name = 'DuiTangImage'
	#allowed_domains = ['https://www.duitang.com/']
	
	@property
	def start_url(self):
		stat_url = 'https://www.duitang.com/napi/blog/list/by_filter_id/?include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Csender%2Calbum&filter_id=%E5%A4%B4%E5%83%8F&start={}'
		# stat_urls = (stat_url.format(i) for i in range(24, 48, 24))
		# for url in stat_urls:
		# 	print(url)
		return (stat_url.format(i) for i in range(0, 48, 24))
	
	def parse(self, response):
		self.logger.info(response.url)
		# for data in json.loads(response.text):
		# 	print(data)
		# data = json.loads(response.text)
		# print(data)
		# item = ImageItem()
		# for i in range(0, len(data['data']['object_list'])):
		# 	print(data['data']['object_list'][i]['photo']['path'])
		# 	item['image_url'] = data['data']['object_list'][i]['photo']['path']
		# 	yield item
