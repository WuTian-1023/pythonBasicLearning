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
    # 豆瓣电影 //*[@id="screening"]/div[2]/ul/li[6]/ul/li[1]/a
    element = webdriver.find_element("xpath", "//div[@class='nav-items']/ul/li[4]/a") # 电影
    print(element.get_attribute("href"))  # https://movie.douban.com/
    element.click()
    # 回退
    webdriver.back()
#     前进
    webdriver.forward()

