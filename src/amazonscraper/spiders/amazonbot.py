import scrapy
import re


class AmazonbotSpider(scrapy.Spider):
    name = 'amazonbot'

    def __init__(self, url, *args, **kwargs):
        super(AmazonbotSpider, self).__init__(*args, **kwargs)
        self.url = self.fixUrl(url)

    allowed_domains = ['www.amazon.ca']

    def fixUrl(self, url):
        id = re.search("B0.{8}", url).group(0)
        return f"https://www.amazon.ca/product-reviews/{id}/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&filterByStar=all_stars&reviewerType=all_reviews&pageNumber="

    def start_requests(self):
        for i in range(1, 10):
            yield scrapy.Request(self.url+str(i), self.parse)

    def parse(self, response):

        data = response.css('#cm_cr-review_list')
        comments = data.css('.review-text')
        for review in comments:
            yield {
                'comment':
                ''.join(review.xpath(".//text()").extract())
            }
