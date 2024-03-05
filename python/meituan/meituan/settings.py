# Scrapy settings for meituan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "meituan"

SPIDER_MODULES = ["meituan.spiders"]
NEWSPIDER_MODULE = "meituan.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "meituan (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
    'Cookie': '_lxsdk_cuid=18a8d26aab5c8-05eb1d1a0c5011-19525634-13c680-18a8d26aab5c6; WEBDFPID=653629w0044851z107vuy568v7431w7y81z1w73y3v897958u0yy856y-2009945240344-1694585237637IUEEIMG75613c134b6a252faa6802015be905516892; _hc.v=be61828e-7424-ecd6-0600-adbd08fdd53a.1694585248; _gid=GA1.2.315039336.1709511959; zgwww=ec96e200-d9c5-11ee-b1e2-554576b05e95; uuid=737AD5AA843EC6B2CF5BE92E56A3CF1636C616692CDDB0482F15276FE8D97C62; iuuid=737AD5AA843EC6B2CF5BE92E56A3CF1636C616692CDDB0482F15276FE8D97C62; _lxsdk=737AD5AA843EC6B2CF5BE92E56A3CF1636C616692CDDB0482F15276FE8D97C62; zg.userid.untrusted=465229356; token2=AgHtI4uDBpDwo45C9HKX2VwHrafhKdLxgtTHq7uvDbAA8nhLKhicz8EShLxHZJ2PuGxz9P3ghsrVdAAAAABgHgAAkT4FsCnXJpfS1ZUha24p4Odi3_47frM_r8spA2mR3gcWwyE2cgxx8frQoqsdGWZ_; userid=2583015098; _ga=GA1.2.2044757989.1694585236; _lxsdk_s=18e094cc37d-28e-811-732%7C%7C65; XSRF-TOKEN=6J1cPwUh-tJr9TiF1qC_019SxF9g3V5TE8aQ; _ga_14F924BYNN=GS1.1.1709553024.3.1.1709553637.60.0.0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3928.4 Safari/537.36',

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "meituan.middlewares.MeituanSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "meituan.middlewares.MeituanDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "meituan.pipelines.MeituanPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
