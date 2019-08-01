from scrapy.crawler import CrawlerProcess
from spiders.amazonwishlist import AmazonWishlistSpider


def get_data(url):
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'LOG_LEVEL': 'INFO'
    })

    scraped_data = []
    process.crawl(AmazonWishlistSpider, url, scraped_data)
    process.start()
    return scraped_data

