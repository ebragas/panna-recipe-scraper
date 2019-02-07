from scrapy.cmdline import execute

try:
    execute(["scrapy", "crawl", "recipes", "-o", "out.json"])
except SystemExit:
    pass
