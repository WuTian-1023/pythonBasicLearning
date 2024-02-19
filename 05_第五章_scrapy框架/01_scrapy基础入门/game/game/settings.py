# Scrapy settings for game project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
'''
    爬虫配置文件
    作用：配置爬虫的一些参数
    1. 请求头
    2. 代理
    3. IP
    4. 爬取速度
    5. 爬取深度
    6. 爬取范围
'''
BOT_NAME = "game" # 爬虫名

SPIDER_MODULES = ["game.spiders"] # 爬虫模块
NEWSPIDER_MODULE = "game.spiders" # 新爬虫模块

LOG_LEVEL = "WARNING"
# 日志的级别：CRITICAL、ERROR、WARNING、INFO、DEBUG


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "game (+http://www.yourdomain.com)" # 用户代理

# Obey robots.txt rules
ROBOTSTXT_OBEY = True # 是否遵守robots协议

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32 # 并发请求数

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3  # 下载延迟
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16 # 同一个域名的并发请求数
#CONCURRENT_REQUESTS_PER_IP = 16 # 同一个IP的并发请求数

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False # 是否开启cookie

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False # 是否开启telnet控制台

# Override the default request headers: # 请求头
#DEFAULT_REQUEST_HEADERS = { # 请求头
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", # 接受的数据类型
#    "Accept-Language": "en", # 接受的语言
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = { # 爬虫中间件
#    "game.middlewares.GameSpiderMiddleware": 543, # 默认开启
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = { # 下载中间件
#    "game.middlewares.GameDownloaderMiddleware": 543, # 默认开启
#}

# Enable or disable extensions # 扩展文件
# See https://docs.scrapy.org/en/latest/topics/extensions.html # 扩展文件
#EXTENSIONS = { # 扩展文件
#    "scrapy.extensions.telnet.TelnetConsole": None, # 默认开启
#}

# Configure item pipelines # 管道文件
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html # 管道文件


ITEM_PIPELINES = { # 管道文件
    # key 是管道的优先级 0-1000 之间 数字越小 优先级越高
    # 值是管道的路径
   "game.pipelines.GamePipeline": 300,
   "game.pipelines.NewPipeline": 299,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True # 自动限速
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5 # 初始下载延迟
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60 # 在高延迟的情况下，设置的最大下载延迟
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0 # 平均每秒并发请求数
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False # 是否开启自动限速的debug模式

# Enable and configure HTTP caching (disabled by default) # 是否开启缓存
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True # 是否开启缓存
#HTTPCACHE_EXPIRATION_SECS = 0 # 缓存过期时间
#HTTPCACHE_DIR = "httpcache"  # 缓存目录
#HTTPCACHE_IGNORE_HTTP_CODES = [] # 忽略的HTTP状态码
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7" # default: 'scrapy.utils.request_fingerprint.request_fingerprint'
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor" # default: 'twisted.internet.selectreactor.SelectReactor'
FEED_EXPORT_ENCODING = "utf-8" # default: 'utf-8'
