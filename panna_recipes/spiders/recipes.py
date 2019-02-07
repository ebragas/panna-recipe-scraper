# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json


class RecipesSpider(CrawlSpider):
    name = 'recipes'
    allowed_domains = ['pannacooking.com']
    start_urls = ['https://api.pannacooking.com/recipes']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        page_data = json.loads(response.text)
        
        for recipe in page_data['_embedded']['recipes']:
            yield recipe

        for link in page_data['_links'].values():
            yield scrapy.Request(url=link['href'], callback=self.parse_page)
