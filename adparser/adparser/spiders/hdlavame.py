# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class HdlavameSpider(scrapy.Spider):
    name = 'hdlavame'
    allowed_domains = ['hdlava.me']
    start_urls = ['https://hdlava.me/film/zheleznyy-chelovek.html']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        for ad in response.css('a[href*="recreativ.ru"]'):
            ad_img = ad.css('div img::attr(src)').extract_first()
            ad_texts = ad.css('div span::text').extract()
            if ad_img and len(ad_texts) == 2:
                yield {
                    'img': response.urljoin(ad_img),
                    'title': ad_texts[0],
                    'text': ad_texts[1]
                }
