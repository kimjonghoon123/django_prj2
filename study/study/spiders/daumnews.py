import scrapy
import re
from study.items import newsitem

class DaumnewsSpider(scrapy.Spider):
    name = 'daumnews'

    start_urls = ['https://www.daum.net/']
    custom_settings = {
         'DOWNLOADER_MIDDLEWARES': {
             'study.middlewares.SeleniumMiddleware3': 100
         },
        'ITEM_PIPELINES': {
            "study.pipelines.annMySQLPipeline": 400,
        }
    }
    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         'study.middlewares.SeleniumMiddleware2': 100
    #     }
    # }

    def parse(self, response):
        title1 = response.xpath("/html/body/article/article/div/article/div/div[2]/div[1]/div[1]/ul/li[1]/div[2]/a//text()").getall()
        title2 = response.xpath("/html/body/article/article/div/article/div/div[2]/div[1]/div[1]/ul/li[2]/div[2]/a//text()").getall()
        title3 = response.xpath("/html/body/article/article/div/article/div/div[2]/div[1]/div[1]/ul/li[3]/div[2]/a//text()").getall()
        title4 = response.xpath("/html/body/article/article/div/article/div/div[2]/div[1]/div[1]/ul/li[4]/div[2]/a//text()").getall()
        link = response.xpath("/html/body/article/article/div/article/div/div[2]/div[1]/div[1]/ul/li/div[2]/a/@href").getall()[:4]

        doc = newsitem()
        doc['title'] = "".join(title1)
        doc['link'] = link[0]
        yield doc
        doc['title'] = "".join(title2)
        doc['link'] = link[1]
        yield doc
        doc['title'] = "".join(title3)
        doc['link'] = link[2]
        yield doc
        doc['title'] = "".join(title4)
        doc['link'] = link[3]
        yield doc










    #     yield scrapy.Request(url=newslink, callback=self.parse_item)
    #
    # def parse_item(self, response):
    #     # body = response.xpath("body").getall()
    #     # print(body)
    #     a = response.xpath("/html/body/article/article/div/article/div/div[2]/div[1]/div[1]/ul/li//text()").getall()
    #     b = response.xpath("/html/body/article/article/div/article/div/div[2]/div[1]/div[1]/ul/li//@href").getall()
    #     setb = set(b)
    #     blist = list(setb)
    #     print(blist)
    #     for num, i in enumerate(blist):
    #         print(num, i)
    #         yield scrapy.Request(url=i, callback=self.post_item)

    # noinspection PyMethodMayBeStatic
    # def post_item(self, response):
    #     doc = newsitem()
    #     hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    #     text = response.text
    #     result = hangul.sub('', text)
    #     m = result.replace("  ", '')
    #     print("1", m)
    #     doc["data"] = m
    #     # print(doc["data"])
    #     yield doc


        #asd = response.xpath("")
        #print(asd)
    #     setlink = set(link)
    #     links = list(setlink)
    #     for num, i in enumerate(links):
    #         print(num, i)
    #         yield scrapy.Request(url=i, callback=self.parse_item)
    #
    # def parse_item(self, response):
    #     body = response.xpath('body').getall()
    #     print(body)
