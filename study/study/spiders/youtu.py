import urllib.request

import scrapy
from selenium import webdriver
from time import sleep

import study.pipelines
from study.items import youtuMysqlItem
import urllib.request
import wget

class YoutuSpider(scrapy.Spider):
    name = 'youtu'
    start_urls = ['https://www.youtube.com/results?search_query=%ED%95%AD%EB%A7%8C%EB%89%B4%EC%8A%A4']
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'study.middlewares.SeleniumMiddleware': 100
        },
        'ITEM_PIPELINES': {
            "study.pipelines.youtuMySQLPipeline": 400,
        }
    }

    def parse(self, response):
        baseurl = ['https://www.youtube.com']
        href = response.xpath('//div[@id="contents"]/ytd-video-renderer/div//h3/a/@href').getall()
        titles = response.xpath('//div[@id="contents"]/ytd-video-renderer/div//h3/a/@title').getall()
        #imgsrc = response.xpath('//*[@id="thumbnail"]/yt-img-shadow/img/@src').getall()
        #print(imgsrc)
        for num, a in enumerate(titles):
            doc = youtuMysqlItem()
            titles = a
            #b = musics[num]
            c = baseurl[0] + href[num]
            doc["title"] = a
            doc["link"] = c
            #doc["imgsrcs"] = b
            #doc["num"] = num+1
            print("[", num + 1, "] 제목 : ", titles, "주소 : ", c)
            #print("[", num+1, "]이미지 소스 : ", b, "제목 : ", titles, "주소 : ", c)
            #filename = 'C:/Users/kjh19/OneDrive/바탕 화면/cmder/study/' + a[:4] + '.jpg'
            #print(filename)
            #wget.download(b, filename)
            yield doc