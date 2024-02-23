from bald_spider.spider import Spider
from bald_spider.http.request import Request
from tests.baidu_spider.items import BaiduItem


class BaiduSpider(Spider):

    start_urls = ['http://www.baidu.com', 'http://www.baidu.com']
    # start_url = 'http://www.baidu.com'

    # @classmethod
    # def create_instance(cls):
    #     # 实例化的逻辑
    #     return cls()

    custom_settings = {'CONCURRENCY': 8}

    def parse(self, response):
        # print('parse', response)
        for i in range(3):
            url = 'http://www.baidu.com'
            request = Request(url=url, callback=self.parse_page)
            yield request

    def parse_page(self, response):
        # print('parse_page', response)
        for i in range(3):
            url = 'http://www.baidu.com'
            request = Request(url=url, callback=self.parse_detail)
            yield request

    def parse_detail(self, response):
        # print('parse_detail', response)
        # print(response.text)
        item = BaiduItem()
        item['url'] = 'baidu.com'
        item['title'] = '百度首页'
        yield item