# --*-- conding:utf-8 --*--
# @Time : 2024-01-30 030 下午 07:38
# @Author : CoderTLL
# @Email : javacoder1023@gmail.com
# @File : 03_selenium浏览器窗口切换.py
# @Software : PyCharm
# 代码不规范 同事两行泪
from selenium import webdriver

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)  # 保持浏览器不关闭
    """ 切换窗口 """
    webdriver = webdriver.Chrome(options=options)
    # 豆瓣
    webdriver.get("https://movie.douban.com/")
    # 豆瓣电影
    element = webdriver.find_element("xpath", "//div[@class='global-nav-items']/ul/li[5]/a") # 同城
    print(element.get_attribute("href"))  # https://www.douban.com/location/
    element.click()
    # 获取当前所有窗口
    windows = webdriver.window_handles
    print(windows)
    # 切换窗口
    webdriver.switch_to.window(windows[-1]) # 切换到最后一个窗口 也就是切换到同城
