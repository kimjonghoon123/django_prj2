import scrapy
from study.items import announcement

class UlsanSpider(scrapy.Spider):
    name = 'ulsan'

    start_urls = ['https://www.upa.or.kr/bbs/list.do?bbsId=BBS_0000000000000039&mId=001003012001000000']
    custom_settings = {
        'ITEM_PIPELINES': {
            "study.pipelines.ulsanMySQLPipeline": 400,
        }
    }
    def parse(self, response):
        baseurl = 'https://www.upa.or.kr/bbs'
        a = response.xpath('/html/body/div/div[4]/div/div[2]/div[2]/div[1]/form/table/tbody/tr/td[2]/a/text()').getall()
        b = response.xpath('/html/body/div/div[4]/div/div[2]/div[2]/div[1]/form/table/tbody/tr/td[2]/a/@href').getall()
        for num, link in enumerate(b):
            if num ==5:
                break
            doc = announcement()
            f = link[1:]
            c= a[num]
            d= baseurl + f
            c.replace('\t','').replace('\n',"").replace('\n',"").replace("'","").replace("\r","").rstrip().lstrip()
            doc['title'] = c
            doc['link'] = d
            yield doc

