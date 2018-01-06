#!/usr/bin/env python3

import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen


browserPath = '/opt/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
homePage = 'https://mm.taobao.com/search_tstar_model.htm?'
outputDir = 'photo/'
parser = 'html5lib'


def main():
	driver = webdriver.PhantomJS(executable_path=browserPath)
	driver.get(homePage)
	bsObj = BeautifulSoup(driver.page_source, parser)
	
	girlsList = driver.find_element_by_id('J_GirlsList').text.split('\n')
	girlsNL  = girlsList[::3]
	girlsHW = girlsList[1::3]
	girlsUrl = bsObj.find_all("a",{"href": re.compile("\/\/.*\.htm\?(userId=)\d*")})
	girlsHURL = [('http:' + i['href']) for i in girlsUrl]
	imagesUrl = re.findall('\/\/gtd\.alicdn\.com\/sns_logo.*\.jpg',driver.page_source)
	girlsPhotoURL = [('https:' +i) for i in imagesUrl]
	girlsInfo = zip(girlsNL, girlsHW, girlsHURL, girlsPhotoURL)
	for girlNL, girlHW, girlHURL, girlPhotoURL in girlsInfo:
		print("[*]Girl:", girlNL, girlHW)
		mkdir(outputDir + girlNL)
		data = urlopen(girlPhotoURL).read()
		with open(outputDir + girlNL +'/cover.jpg', 'wb') as f:
			f.write(data)
			print("[+}Loading cover...")
			getImg(girlHURL, outputDir + girlNL)
	driver.close()
	
def mkdir(path):
	isExists = os.path.exists(path)
	if not isExists:
		print("[*]mkdir path", path)
		os.makedirs(path)
	else:
		print("[+]path",path, 'exists')


def getImg(url,path):
	driver = webdriver.PhantomJS(executable_path=browserPath)
	driver.get(url)
	bsObj = BeautifulSoup(driver.page_source, parser)

	imgs = bsObj.find_all("img", {"src": re.compile(".*\.jgp")})
	for i, img in enumerate(imgs[1:]):
		try:
			html = urlopen('https:' + img['src'])
			data = html.read()
			fileName = "{}/{}.jpg".format(path, i+1)
			print("[+]Loading...", fileName)
			with open(fileName, 'wb') as f:
				f.write(data)
		except Exception:
			print("[!]address Error!")
	driver.close()


if __name__ == "__main__":
	if not os.path.exists(outputDir):
		os.makedirs(outputDir)
	main()
