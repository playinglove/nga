# -*- coding: utf-8 -*-

# Scrapy settings for nga project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'nga'

SPIDER_MODULES = ['nga.spiders']
NEWSPIDER_MODULE = 'nga.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'nga (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
HTTPERROR_ALLOWED_CODES = [403]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Language': 'en',
    'User-Agent': "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "

}
COOKIES_ENABLES = False

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'nga.middlewares.NgaSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'nga.middlewares.NgaDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'nga.pipelines.NgaPipeline': 300,
# }
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


COOKIE = {'UM_distinctid': '1635d9d13c777b-03b66611879fa-3961430f-144000-1635d9d13c86fe',
          'taihe': 'bf3d77f557cb44a550bee5d21e74ef34', 'bbsmisccookies': '%7B%7D',
          'CNZZDATA1256638851': '674147559-1529645399-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529645399',
          'CNZZDATA1256638828': '1589233661-1526543616-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529648393',
          'CNZZDATA1256638919': '1525469300-1529648646-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529648646',
          'CNZZDATA1256638924': '312763242-1529646682-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529653575',
          'CNZZDATA1264400273': '1988147916-1529650361-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529650361',
          'CNZZDATA1256638887': '559896610-1529648818-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529648818',
          'CNZZDATA30043604': 'cnzz_eid%3D147715379-1526279102-http%253A%252F%252Fbbs.ngacn.cc%252F%26ntime%3D1529979443',
          'CNZZDATA30039253': 'cnzz_eid%3D1037247114-1526283838-http%253A%252F%252Fbbs.ngacn.cc%252F%26ntime%3D1529977786',
          'CNZZDATA1256638820': '1787913993-1526280324-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529976113',
          'guestJs': '1529980732', 'PHPSESSID': '2u02d1bip6oguslklb5bhv0vt4',
          'ngacn0comUserInfo': 'spring%25B0%25A1%25B0%25A1%25B0%25A1%09spring%25E5%2595%258A%25E5%2595%258A%25E5%2595%258A%0939%0939%09%0910%091200%094%090%090%0961_12',
          'ngacn0comUserInfoCheck': '3325213a7ec86ffb6cee44228238fd99', 'ngacn0comInfoCheckTime': '1529981284',
          'ngaPassportUid': '40755489', 'ngaPassportUrlencodedUname': 'spring%25B0%25A1%25B0%25A1%25B0%25A1',
          'ngaPassportCid': 'Xkc2bbakvmldcuj8u5bdali9p4pbk0h2ns4upk7q', 'lastvisit': '1529981482',
          'lastpath': '/read.php?tid',
          'Hm_lvt_5adc78329e14807f050ce131992ae69b': '1529647469,1529909758,1529980014,1529981483',
          'Hm_lpvt_5adc78329e14807f050ce131992ae69b': '1529981483',
          'CNZZDATA1256638858': '1208637985-1526546744-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529978881'}
