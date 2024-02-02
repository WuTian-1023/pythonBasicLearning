import time

from selenium import webdriver

if __name__ == '__main__':
    # 创建浏览器对象
    browser = webdriver.Chrome()
    # 访问页面
    browser.get("https://www.baidu.com")
    browser.find_element("id", "kw").send_keys("python")  # 通过id找到输入框并输入python
    browser.find_element("id", "su").click()  # 通过id找到搜索按钮并点击

    time.sleep(3)  # 停留3秒
    browser.save_screenshot("baidu.png")  # 截图
    # 获取渲染后的数据
    # print(browser.page_source)
    # 获取cookie
    cookies = browser.get_cookies()
    print(cookies)
    # 查看当前url
    print(browser.current_url)
    # 关闭当前页面
    browser.close()
    # 关闭浏览器
    browser.quit()

    # 无限循环，阻止程序退出
    # while True:
    #     pass
