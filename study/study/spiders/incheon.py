import nltk
import scrapy
from study.items import announcement
from nltk.tokenize import word_tokenize


class IncheonSpider(scrapy.Spider):
    name = 'incheon'
    start_urls = ['http://alio.go.kr/popSusi.do?apbaId=C0107&reportFormRootNo=B1030']
    custom_settings = {
         # 'DOWNLOADER_MIDDLEWARES': {
         #     'study.middlewares.SeleniumMiddleware3': 100
         # },
         'ITEM_PIPELINES': {
             "study.pipelines.incheonMySQLPipeline": 400,
        }
    }
    def parse(self, response):
        a = response.xpath("/html/body/div[1]/div[2]/div/table/tbody/tr/td[2]/a/@onclick").getall()
        print(a)
        b = response.xpath("/html/body/div[1]/div[2]/div/table/tbody/tr/td[2]/a/text()").getall()
        print(b)
        for num,i in enumerate(a):
            doc = announcement()
            # token = i[0]
            print(i[15:31])
            print(i[79:86])
            link = 'http://alio.go.kr/popSusiViewB1030.do?disclosure_no=' + i[15:31] + '&report_form_no=B1030&nowcode=B103' \
                                                                                       '0&apbaid=C0107&table_name=COMM_BOARD&idx_name=BOARD_NO&idx=' + i[79:86] + '&report_gbn=N&bid_type=1'
            title = b[num]
            print(link)
            print(title)
            doc['title'] = title
            doc['link'] = link
            yield doc
        # print("잘됨")
        # doc = announcement()
        # doc['title'] = response.meta['a']
        # doc['link'] = response.meta['b']
        # yield doc
