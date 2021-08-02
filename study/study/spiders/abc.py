import scrapy
from study.items import abcitem
custom_settings ={

}

class AbcSpider(scrapy.Spider):
    name = 'abc'

    def start_requests(self):
        urls = ['https://www.searates.com/kr/port/pyungtaek_kr.htm',
                'https://www.searates.com/kr/port/seoul_kr.htm',
                'https://www.searates.com/kr/port/incheon_kr.htm',
                'https://www.searates.com/kr/port/daesan_kr.htm',
                'https://www.searates.com/kr/port/pyungtaek_kr.htm',
                'https://www.searates.com/kr/port/ko_jung_kr.htm',
                'https://www.searates.com/kr/port/kunsan_kr.htm',
                'https://www.searates.com/kr/port/mogpo_kr.htm',
                'https://www.searates.com/kr/port/sokcho_kr.htm',
                'https://www.searates.com/kr/port/daepori_kr.htm',
                'https://www.searates.com/kr/port/okkye_kr.htm',
                'https://www.searates.com/kr/port/mukho_kr.htm',
                'https://www.searates.com/kr/port/tonghae_kr.htm',
                'https://www.searates.com/kr/port/samchok_kr.htm',
                'https://www.searates.com/kr/port/donghae_kr.htm',
                'https://www.searates.com/kr/port/pohang_kr.htm',
                'https://www.searates.com/kr/port/ulsan_kr.htm',
                'https://www.searates.com/kr/port/onsan_kr.htm',
                'https://www.searates.com/kr/port/masan_kr.htm',
                'https://www.searates.com/kr/port/pusan_kr.htm',
                'https://www.searates.com/kr/port/kwangyang_kr.htm',
                'https://www.searates.com/kr/port/gwangyang_kr.htm',
                'https://www.searates.com/kr/port/yosu_kr.htm',
                'https://www.searates.com/kr/port/yeosu_kr.htm',
                'https://www.searates.com/kr/port/samcheon_po_kr.htm',
                'https://www.searates.com/kr/port/okpo_kr.htm',
                'https://www.searates.com/kr/port/koje_kr.htm',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        doc = abcitem()
        doc['xt'] = response.xpath("/html/body/div[1]/div/div[1]/div[2]/table[1]//tr[8]/td[1]/text()").getall()
        doc['x'] = response.xpath("/html/body/div[1]/div/div[1]/div[2]/table[1]//tr[8]/td[2]/text()").getall()
        doc['yt'] = response.xpath("/html/body/div[1]/div/div[1]/div[2]/table[1]//tr[9]/td[1]/text()").getall()
        doc['y'] = response.xpath("/html/body/div[1]/div/div[1]/div[2]/table[1]//tr[9]/td[2]/text()").getall()
        doc['name']= response.xpath("/html/body/div[1]/div/div[1]/div[1]/div/text()").getall()
        print(doc['name'])
        print(doc['x'], doc['xt'])
        print(doc['y'], doc['yt'])
        yield doc
