# --*-- conding:utf-8 --*--
# @Time : 2024-01-29 029 下午 10:33
# @Author : CoderTLL
# @Email : javacoder1023@gmail.com
# @File : 02_selenium标签定位.py
# @Software : PyCharm
# 代码不规范 同事两行泪
from selenium import webdriver

if __name__ == '__main__':
    webdriver = webdriver.Chrome()
    # 豆瓣
    webdriver.get("https://movie.douban.com/")

    # 1.通过class name定位
    element = webdriver.find_element("class name", "nav-logo")  # 通过class name定位，获得的是一个标签对象
    print(element.text)  # 豆瓣电影

    # 2.获取多个标签对象
    elements = webdriver.find_elements("class name", "nav-items")  # find_elements
    for element in elements:
        print(element.text)
    """
    element.get_attribute()
获取元素的给定属性或属性。
此方法将首先尝试返回具有给定名称的属性的值。如果具有该名称的属性不存在，它将返回具有相同名称的属性的值。如果没有具有该名称的属性，则返回None。
被认为是truthy的值，即等于“true”或“false”的值，将作为布尔值返回。所有其他非None值都作为字符串返回。对于不存在的属性或属性，将返回None。
要获得属性或属性的确切值，请分别使用~selenium.webdriver.mote.BaseWebElement.get_dom_attribute或~selenium_webdriver.Mote.BaseWebElement.get_property方法。
    """
    # 3.通过标签名定位
    element = webdriver.find_element("tag name", "input")
    print(element.get_attribute("placeholder"))  # 搜索电影、电视剧、综艺、影人 element.get_attribute()获取属性值

    # 4.通过xpath定位 //*[@id="inp-query"] /html/body/div[2]/div[1]/div/div[2]/form/fieldset/div[1]/input
    element = webdriver.find_element("xpath", "//div[@class='nav-search']/form/fieldset/div/input")
    print(element.get_attribute("placeholder"))  # 搜索电影、电视剧、综艺、影人 element.get_attribute()获取属性值

    # 5.通过css定位
    """
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="搜索电影、电视剧、综艺、影人" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1002" />
        </fieldset>
    """
    element = webdriver.find_element("css selector", "#inp-query")
    print(element.get_attribute("placeholder"))  # 搜索电影、电视剧、综艺、影人 element.get_attribute()获取属性值

    # 6.通过链接文本定位
    element = webdriver.find_element("link text", "FM")
    print(element.get_attribute("href"))  # https://www.douban.com/

    # 7.通过部分链接文本定位
    element = webdriver.find_element("partial link text", "读书")  # 通过部分链接文本定位
    print(element.get_attribute("href"))  # https://www.douban.com/

    # 8.模糊查询 包含豆瓣的所有标签
    elements = webdriver.find_elements("partial link text", "豆瓣")
    for element in elements:
        print(element.get_attribute("href"))  # https://www.douban.com/

    # 9.通过h2标签定位
    element = webdriver.find_element("tag name", "h2")
    print(element.text)  # 豆瓣电影

    # 10.通过id定位
    element = webdriver.find_element("id", "inp-query")
    print(element.get_attribute("placeholder"))  # 搜索电影、电视剧、综艺、影人 element.get_attribute()获取属性值


