from scrapy.cmdline import execute

# -L WANING 不显示DEBUG信息
# execute(['scrapy', 'crawl', 'zcSpider', '-L', 'WARNING'])

# execute(['scrapy', 'crawl', 'zcSpider', '-s', 'JOBDIR=.remain/002'])
# execute(['scrapy', 'crawl', 'zcSpider'])

# execute(['scrapy', 'crawl', 'zcSpider', '-a', 'params={"startDate":"2010-08-01", "endDate":"2010-08-02"}', '-L', 'WARNING'])
execute(['scrapy', 'crawl', 'zcSpider', '-a', 'params={"startDate":"2018-01-31", "endDate":"2018-02-02"}'])
