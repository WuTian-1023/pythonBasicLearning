# --*-- conding:utf-8 --*--
# @Time : 2024-01-30 030 下午 07:38
# @Author : CoderTLL
# @Email : javacoder1023@gmail.com
# @File : 03_selenium浏览器窗口切换.py
# @Software : PyCharm
# 代码不规范 同事两行泪

import random
import re  # 正则表达式匹配库
import time  # 事件库，用于硬性等待
import urllib  # 网络访问
import cv2  # opencv库

from selenium import webdriver  # 导入selenium的webdriver模块
from selenium.webdriver.common.by import By  # 引入By类选择器
from selenium.webdriver.support.wait import WebDriverWait  # 等待类
from selenium.webdriver.support import expected_conditions as EC  # 等待条件类
from selenium.webdriver.common.action_chains import ActionChains  # 动作类


# 封装的计算图片距离的算法
def get_pos(imageSrc):
    # 读取图像文件并返回一个image数组表示的图像对象
    image = cv2.imread(imageSrc)
    # GaussianBlur方法进行图像模糊化/降噪操作。
    # 它基于高斯函数（也称为正态分布）创建一个卷积核（或称为滤波器），该卷积核应用于图像上的每个像素点。
    blurred = cv2.GaussianBlur(image, (5, 5), 0, 0)
    # Canny方法进行图像边缘检测
    # image: 输入的单通道灰度图像。
    # threshold1: 第一个阈值，用于边缘链接。一般设置为较小的值。
    # threshold2: 第二个阈值，用于边缘链接和强边缘的筛选。一般设置为较大的值
    canny = cv2.Canny(blurred, 0, 100)  # 轮廓
    # findContours方法用于检测图像中的轮廓,并返回一个包含所有检测到轮廓的列表。
    # contours(可选): 输出的轮廓列表。每个轮廓都表示为一个点集。
    # hierarchy(可选): 输出的轮廓层次结构信息。它描述了轮廓之间的关系，例如父子关系等。
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 遍历检测到的所有轮廓的列表
    for contour in contours:
        # contourArea方法用于计算轮廓的面积
        area = cv2.contourArea(contour)
        # arcLength方法用于计算轮廓的周长或弧长
        length = cv2.arcLength(contour, True)
        # 如果检测区域面积在5025-7225之间，周长在300-380之间，则是目标区域
        if 5025 < area < 7225 and 300 < length < 380:
            # 计算轮廓的边界矩形，得到坐标和宽高
            # x, y: 边界矩形左上角点的坐标。
            # w, h: 边界矩形的宽度和高度。
            x, y, w, h = cv2.boundingRect(contour)
            print("计算出目标区域的坐标及宽高：", x, y, w, h)
            # 在目标区域上画一个红框看看效果
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imwrite("111.jpg", image)
            return x
    return 0

# 新增的 move_slider 函数，用于更精确地控制滑块移动
def move_slider(webdriver, slider_element, target_distance):
    action_chains = ActionChains(webdriver)
    action_chains.click_and_hold(slider_element).perform()
    time.sleep(0.2)  # 短暂暂停，模拟人类点击滑块后的停顿

    # 逐渐增加移动距离
    moved_distance = 0
    while moved_distance < target_distance:
        step = random.randint(5, 10)  # 每次移动5到10像素
        action_chains.move_by_offset(step, 0).perform()
        moved_distance += step
        time.sleep(0.1)  # 短暂暂停，模仿人类滑动滑块的行为

    # 如果移动过头，需要回退一点
    overshoot = moved_distance - target_distance
    if overshoot > 0:
        action_chains.move_by_offset(-overshoot, 0).perform()

    action_chains.release().perform()

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)  # 保持浏览器不关闭
    """ 切换窗口 """
    webdriver = webdriver.Chrome(options=options)
    # 豆瓣 https://accounts.douban.com/passport/login
    webdriver.get("https://www.douban.com/")
    # 获取frame
    webdriver.switch_to.frame(0)  # 切换到frame
    # 点击账号密码登录
    webdriver.find_element("xpath", "//ul[@class='tab-start']").click()
    # 设置账号密码 id="username" id="password"
    webdriver.find_element("id", "username").send_keys("17711743029")
    webdriver.find_element("id", "password").send_keys("mm123456")
    # 点击登录
    webdriver.find_element("class name", "btn-account").click()
    # 有滑条的页面，需要滑动滑条
    # 滑条验证处理文档：https://blog.csdn.net/qq_45774549/article/details/108626796
    webdriver.implicitly_wait(5)  # 使用浏览器隐式等待5秒
    # 此时需要切换到弹出的滑块区域，需要切换frame窗口
    webdriver.switch_to.frame("tcaptcha_iframe_dy")
    # 等待滑块验证图片加载后，再做后面的操作
    WebDriverWait(webdriver, 10).until(EC.visibility_of_element_located((By.ID, 'slideBg')))
    # 获取滑块验证图片下载路径，并下载到本地
    bigImage = webdriver.find_element(By.ID, "slideBg")
    s = bigImage.get_attribute("style")  # 获取图片的style属性
    # 设置能匹配出图片路径的正则表达式
    p = 'background-image: url\\(\"(.*?)\"\\);'
    # 进行正则表达式匹配，找出匹配的字符串并截取出来
    bigImageSrc = re.findall(p, s, re.S)[0]  # re.S表示点号匹配任意字符，包括换行符
    # print("滑块验证图片下载路径:", bigImageSrc)
    # 下载图片至本地
    urllib.request.urlretrieve(bigImageSrc, 'bigImage.png')
    # 计算缺口图像的x轴位置
    dis = get_pos('bigImage.png')
    print("缺口图像的x轴位置：", dis)
    # 获取小滑块元素，并移动它到上面的位置  //*[@id="tcOperation"]/div[6]
    smallImage = webdriver.find_element(By.XPATH, '//*[@id="tcOperation"]/div[6]')
    # 小滑块到目标区域的移动距离（缺口坐标的水平坐标距离小滑块的水平坐标相减的差）
    # 新缺口坐标=原缺口坐标*新画布宽度/原画布宽度
    x_ = smallImage.location['x']
    # width: 49.6429px; height: 49.6429px; left: 20.6845px;
    print("小滑块的初始x坐标：", x_)
    newDis = int(dis * 340 / 672)
    newDis = int((newDis - x_) / 1.22)  # 1.22是根据实际情况调整的
    print("小滑块的目标x坐标：", newDis)
    webdriver.implicitly_wait(5)  # 使用浏览器隐式等待5秒
    # 按下小滑块按钮不动
    ActionChains(webdriver).click_and_hold(smallImage).perform()

    # 使用新的 move_slider 函数移动滑块
    move_slider(webdriver, smallImage, newDis)
    # 移动小滑块，模拟人的操作，一次次移动一点点
    # i = 0
    # moved = 0
    # while moved < newDis:
    #     x = random.randint(3, 10)  # 每次移动3到10像素
    #     moved += x
    #     ActionChains(webdriver).move_by_offset(xoffset=x, yoffset=0).perform()
    #     print("第{}次移动后，位置为{}".format(i, smallImage.location['x']))
    #     i += 1
    #     if int(smallImage.location['x']) >= (newDis + x_): # 判断是否到达目标位置
    #         # 移动完之后，松开鼠标
    #         ActionChains(webdriver).release(smallImage).perform()
    #         break

    # 整体等待5秒看结果
    time.sleep(5)
