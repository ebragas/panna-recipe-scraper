from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from panna_recipe_scraper.spiders.recipe_spider import RecipeSpider

process = CrawlerProcess(get_project_settings())
process.crawl(RecipeSpider)
process.start()
