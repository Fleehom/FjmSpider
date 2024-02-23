from bald_spider.spider import Spider
from bald_spider.http.request import Request


class BaiduSpider2(Spider):

    start_urls = ['https://www.baidu.com', 'https://www.baidu.com']
    # start_url = 'https://www.baidu.com'

    # @classmethod
    # def create_instance(cls):
    #     # 实例化的逻辑
    #     return cls()

    def parse(self, response):
        print('parse2', response)
        for i in range(3):
            url = 'https://www.baidu.com'
            request = Request(url=url, callback=self.parse_page)
            yield request

    def parse_page(self, response):
        print('parse_page2', response)
        for i in range(3):
            url = 'https://www.baidu.com'
            request = Request(url=url, callback=self.parse_detail)
            yield request

    def parse_detail(self, response):
        print('parse_detail2', response)