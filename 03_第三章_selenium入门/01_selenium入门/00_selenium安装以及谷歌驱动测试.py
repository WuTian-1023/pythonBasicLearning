"""
    python爬虫4小分队（scrapy、beautifulsoup、selenium以及pyppeteer）之一的Selenium库，
主要用于模拟浏览器运行，是一个用于web应用测试的工具。Selenium直接运行在浏览器中，
看起来就像人在操作一样（也可无窗口模式运行）。支持的浏览器包括IE、Firefox、Safari、Chrome、Opera和Edge等。

selenium 英 /səˈliːniəm/ 美 /səˈliniəm/
selenium安装以及谷歌驱动测试
    1.安装selenium pip install selenium
    2.下载谷歌驱动 https://npm.taobao.org/mirrors/chromedriver/ 或者 https://googlechromelabs.github.io/chrome-for-testing/
        我的版本比较高 用的后面的地址 Chrome 已是最新版本
                                        版本 121.0.6167.86（正式版本） （64 位）
    3.将谷歌驱动放到python安装目录下

"""
import time
# 导入selenium包
from selenium import webdriver
# 打开谷歌浏览器
browser = webdriver.Chrome()
# 停留三秒
time.sleep(3)
# 关闭浏览器
browser.quit()