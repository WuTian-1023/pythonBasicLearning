# --*-- conding:utf-8 --*--
# @Time : 2024-01-31 031 下午 02:59
# @Author : CoderTLL
# @Email : javacoder1023@gmail.com
# @File : 04_selenium拉勾网.py
# @Software : PyCharm
# 代码不规范 同事两行泪
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
search_input = WebDriverWait(self.driver, 10).until( EC.presence_of_element_located((By.ID, "search_input")) )

这段代码是使用Selenium库在Python中进行网页自动化的一部分。这里的`WebDriverWait`和`expected_conditions`（别名为`EC`）是Selenium的显式等待功能。

`WebDriverWait(self.driver, 10)`创建了一个WebDriverWait实例，它将等待最多10秒，直到某个条件满足。

`.until(EC.presence_of_element_located((By.ID, "search_input")))`是等待的条件。`EC.presence_of_element_located`是一个预设的条件，表示等待某个元素出现在DOM中。`By.ID, "search_input"`指定了要等待的元素，即ID为"search_input"的元素。

所以，整段代码的意思是：等待最多10秒，直到ID为"search_input"的元素出现在DOM中。如果在10秒内该元素出现，`WebDriverWait.until`方法将返回该元素；如果10秒后该元素仍未出现，将抛出`TimeoutException`异常。
"""


class LagouSpider:
    def __init__(self):
        self.url = "https://www.lagou.com/wn/"
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()  # 最大化窗口

    def run(self):
        self.driver.get(self.url)
        try:
            # 使用显式等待来等待搜索框的出现
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "search_input"))
            )
            search_input.click()  # 点击确保输入框可以输入
            time.sleep(1)  # 稍作等待
            search_input.send_keys("python")

            # 点击搜索按钮
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "search_button"))
            )
            # search_button.click()
            self.driver.execute_script("arguments[0].click();", search_button)  # 使用js点击
            # 等待并切换到新窗口
            WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])

            # 获取列表数据
            driver__until = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='p-top__1F7CL']")))
            for item in driver__until:
                print(item.text)


        except Exception as e:
            print(f"发生错误: {e}")
        # self.driver.quit()


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
