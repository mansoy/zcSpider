from scrapy.cmdline import execute

# -L WANING 不显示DEBUG信息
#execute(['scrapy', 'crawl', 'zcSpider', '-L', 'WARNING'])

execute(['scrapy', 'crawl', 'zcSpider'])
