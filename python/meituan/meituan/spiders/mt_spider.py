import scrapy
from ..items import MeituanItem


class MtSpiderSpider(scrapy.Spider):
    name = 'mt_spider'
    allowed_domains = ['minsu.dianping.com']
    max_page = 17
    city = input("请输入您要入住的酒店城市：")
    # start_urls = [f'https://minsu.dianping.com/zhenjiang/pn{page}/'for page in range(1, max_page+1)]
    start_urls = [f'https://minsu.dianping.com/{city}']
    headers = {
        'Cookie': '_lxsdk_cuid=18a8d26aab5c8-05eb1d1a0c5011-19525634-13c680-18a8d26aab5c6; WEBDFPID=653629w0044851z107vuy568v7431w7y81z1w73y3v897958u0yy856y-2009945240344-1694585237637IUEEIMG75613c134b6a252faa6802015be905516892; _hc.v=be61828e-7424-ecd6-0600-adbd08fdd53a.1694585248; _gid=GA1.2.315039336.1709511959; zgwww=ec96e200-d9c5-11ee-b1e2-554576b05e95; uuid=737AD5AA843EC6B2CF5BE92E56A3CF1636C616692CDDB0482F15276FE8D97C62; iuuid=737AD5AA843EC6B2CF5BE92E56A3CF1636C616692CDDB0482F15276FE8D97C62; _lxsdk=737AD5AA843EC6B2CF5BE92E56A3CF1636C616692CDDB0482F15276FE8D97C62; zg.userid.untrusted=465229356; token2=AgHtI4uDBpDwo45C9HKX2VwHrafhKdLxgtTHq7uvDbAA8nhLKhicz8EShLxHZJ2PuGxz9P3ghsrVdAAAAABgHgAAkT4FsCnXJpfS1ZUha24p4Odi3_47frM_r8spA2mR3gcWwyE2cgxx8frQoqsdGWZ_; userid=2583015098; _ga=GA1.2.2044757989.1694585236; _lxsdk_s=18e094cc37d-28e-811-732%7C%7C65; XSRF-TOKEN=6J1cPwUh-tJr9TiF1qC_019SxF9g3V5TE8aQ; _ga_14F924BYNN=GS1.1.1709553024.3.1.1709553637.60.0.0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3928.4 Safari/537.36',
    }

    cookie={
    "_lxsdk_cuid": "18a8d26aab5c8-05eb1d1a0c5011-19525634-13c680-18a8d26aab5c6",
    "WEBDFPID": "653629w0044851z107vuy568v7431w7y81z1w73y3v897958u0yy856y-2009945240344-1694585237637IUEEIMG75613c134b6a252faa6802015be905516892",
    "_hc.v": "be61828e-7424-ecd6-0600-adbd08fdd53a.1694585248",
    "_gid": "GA1.2.315039336.1709511959",
    "zgwww": "ec96e200-d9c5-11ee-b1e2-554576b05e95",
    "uuid": "737AD5AA843EC6B2CF5BE92E56A3CF1636C616692CDDB0482F15276FE8D97C62",
    "iuuid": "737AD5AA843EC6B2CF5BE92E56A3CF1636C616692CDDB0482F15276FE8D97C62",
    "_lxsdk": "737AD5AA843EC6B2CF5BE92E56A3CF1636C616692CDDB0482F15276FE8D97C62",
    "zg.userid.untrusted": "465229356",
    "token2": "AgHtI4uDBpDwo45C9HKX2VwHrafhKdLxgtTHq7uvDbAA8nhLKhicz8EShLxHZJ2PuGxz9P3ghsrVdAAAAABgHgAAkT4FsCnXJpfS1ZUha24p4Odi3_47frM_r8spA2mR3gcWwyE2cgxx8frQoqsdGWZ_",
    "userid": "2583015098",
    "_ga": "GA1.2.2044757989.1694585236",
    "_lxsdk_s": "18e094cc37d-28e-811-732%7C%7C65",
    "XSRF-TOKEN": "6J1cPwUh-tJr9TiF1qC_019SxF9g3V5TE8aQ",
    "_ga_14F924BYNN": "GS1.1.1709553024.3.1.1709553637.60.0.0"
}

    def start_requests(self):
        for page in range(1, self.max_page + 1):
            base_url = 'https://minsu.dianping.com/{}/pn{}'.format(self.city, page)
            yield scrapy.Request(base_url,headers=self.headers,cookies=self.cookie, callback=self.parse)

    def parse(self, response):
        all = response.xpath('.//div[@class="r-card-list v-stretch h-stretch"]').xpath(
            './/div[@class="r-card-list__item shrink-in-sm"]')
        for i in all:
            hrefs = i.xpath('.//a[@class="product-card-container"]/@href').extract_first()
            item = MeituanItem()
            item['title'] = i.xpath('./div/a/figure/figcaption/div/text()').extract_first('')
            item['place'] = i.xpath('./div/a/figure/figcaption/div/div[@class="mt-2"]/text()').extract_first('')
            item['price'] = i.xpath('.//span[@class="product-card__price__latest"]/text()').extract_first('')
            item['room'] = i.xpath('./div/a/figure/figcaption/div/div[1]/text()').extract_first('').split(' · ')[0]
            item['bed_num'] = i.xpath('./div/a/figure/figcaption/div/div[1]/text()').extract_first('').split(' · ')[1]
            item['num'] = i.xpath('./div/a/figure/figcaption/div/div[1]/text()').extract_first('').split(' · ')[2]
            href = response.urljoin(hrefs)
            yield scrapy.Request(url=href, callback=self.new_parse, meta={'item': item})

        # # 翻页操作
        # next_page = response.xpath('.//ul[@class="phx-paginator-wrapper"]/li[10]/a/@href').extract_first()
        # print(response.urljoin(next_page))
        # yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def new_parse(self, response):
        item = response.meta['item']
        ul = response.xpath('.//div').extract_first()
        # print(ul)
        yield item