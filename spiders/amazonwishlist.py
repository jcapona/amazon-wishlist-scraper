import scrapy
import re


class AmazonWishlistSpider(scrapy.Spider):
    BASE_URL = 'https://www.amazon.com'
    name = 'amazonwishlist'
    allowed_domains = ['www.amazon.com']

    def __init__(self, uri, scraped_data, **kwargs):
        self.scraped_data = scraped_data
        self.start_urls = [uri]

        domain = re.sub(r'(http|https)?://', '', uri)
        self.allowed_domains.append(domain)

        super().__init__(**kwargs)

    def parse(self, response):
        page_items = response.css(".g-item-sortable")

        for item in page_items:
            id = item.css('li::attr(data-itemid)').extract_first()
            title = item.css('#itemName_'+id + "::text").extract_first()
            link = item.css('#itemName_'+id + "::attr(href)").extract_first()
            img = item.css('#itemImage_'+id).css('img::attr(src)').extract_first()

            obj = {
                'id': id,
                'title': title,
                'link': link,
                'img': img
            }

            self.scraped_data.append(obj)
            yield obj

        # manage "infinite scrolldown"
        has_next = response.css('#sort-by-price-next-batch-lek::attr(value)').extract_first()
        if has_next:
            lek_uri = response.css('#sort-by-price-load-more-items-url-next-batch::attr(value)').extract_first()
            next_page = self.BASE_URL + lek_uri
            yield scrapy.Request(next_page)

