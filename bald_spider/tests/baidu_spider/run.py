import asyncio
import time
from loguru import logger
from bald_spider.utils.project import get_settings
from bald_spider.crawler import CrawlerProcess
from tests.baidu_spider.spiders.baidu import BaiduSpider
from bald_spider.utils import system as _  # 针对windows端 使用aio方式下载器情况下使用代理出现的问题 进行了解决


async def run():
    settings = get_settings()
    process = CrawlerProcess(settings)
    await process.crawl(BaiduSpider)
    await process.start()


if __name__ == '__main__':
    start_time = round(time.time())
    logger.info(f'<---爬虫开始时间：{start_time}--->')
    asyncio.run(run())
    end_time = round(time.time())
    logger.info(f'<---爬虫结束时间：{end_time}--->')
    use_time = end_time - start_time
    logger.info(f'<---爬虫总用时：{use_time}秒--->')
