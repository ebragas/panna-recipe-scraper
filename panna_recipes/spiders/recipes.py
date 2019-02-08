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
            yield scrapy.Request(url=url, callback=self.parse_api_page)

    def parse_api_page(self, response):
        page_data = json.loads(response.text)
        
        for recipe in page_data['_embedded']['recipes']:
            # callback parse_recipe_page
            yield scrapy.Request(f"https://www.pannacooking.com/recipes/{recipe['slug']}/", callback=self.parse_recipe_page)

        for link in page_data['_links'].values():
            yield scrapy.Request(url=link['href'], callback=self.parse_api_page)

    def parse_recipe_page(self, response):
        data = response.css("script[type='application/ld+json']::text").get()
        item = json.loads(data)
        item['image_urls'] = [item['thumbnailUrl']]
        item['file_urls'] = [item['video']['contentURL']]
        yield item
