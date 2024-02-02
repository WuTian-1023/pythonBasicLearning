# --*-- conding:utf-8 --*--
# @Time : 2024-02-02 002 下午 10:02
# @Author : CoderTLL
# @Email : javacoder1023@gmail.com
# @File : TwoCaptcha.py
# @Software : PyCharm
# 代码不规范 同事两行泪

# 验证码识别

from twocaptcha import TwoCaptcha

solver = TwoCaptcha('你的apikay')

# 解决普通验证码的包装(图片
normal = solver.normal('./img.png')
print(normal) # {'captchaId': '75625184432', 'code': '7'}
