from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from panna_recipes.spiders.recipes import RecipesSpider

process = CrawlerProcess(get_project_settings())
process.crawl(RecipesSpider)
process.start()
