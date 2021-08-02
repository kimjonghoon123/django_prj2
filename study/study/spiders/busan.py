import scrapy
from study.items import newsitem


class BusanSpider(scrapy.Spider):
    name = 'busan'
    start_urls = ['https://www.busanpa.com/kor/Board.do?mCode=MN0793']
    custom_settings = {
        'ITEM_PIPELINES': {
            "study.pipelines.busanMySQLPipeline": 400,
        }
    }
    def parse(self, response):
        start_urls = ['https://www.busanpa.com/kor/Board.do']
        titles = response.xpath('//*[@id="board-wrap"]/table/tbody/tr/td[3]/a/text()').getall()
        hrefs = response.xpath('//*[@id="board-wrap"]/table/tbody/tr/td[3]/a/@href').getall()

        for num, href in enumerate(hrefs):
            if num == 5:
                break
            doc = newsitem()
            a = start_urls[0] + href
            c = titles[num]
            doc['title'] = c
            doc['link'] = a
            yield doc