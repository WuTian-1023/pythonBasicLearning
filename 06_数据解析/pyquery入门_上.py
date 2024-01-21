from pyquery import PyQuery

html = """
    <ul>
    <li class="aaa"><a href="http://www.baidu.com" title="百度">百度</a></li>
    <li class="bbb"><a href="http://www.taobao.com" title="淘宝">淘宝</a></li>
    <li class="bbb" id="jd"><a href="http://www.jd.com" title="京东">京东</a></li>
    <li class="bbb"><a href="http://www.hao123.com" title="hao123">hao123</a></li>
    <li class="aaa"><a href="http://www.360.com" title="360">360</a></li>
    </ul>
"""
# PyQuery 对象直接传入html
# 加载html
query  = PyQuery(html)
# a = query("a")
# print(a)
# print(type(a))

a = query("li")("a") # 链式操作
# print(a)

# 通过class获取
p = query(".aaa")
# print(p)

# 通过class获取
p = query(".aaa a")
# print(p)

# 通过id获取
p = query("#jd a")
# print(p)

# 获取属性
href = query("#jd a").attr("href") # 获取属性
text = query("#jd a").text() # 获取文本
print(href, text) # http://www.jd.com

# 多个元素获取属性
lis = query("li a").items()
for item in lis:
    href = item.attr("href") # 获取属性
    text = item.text() # 获取文本
    print(href, text)

# 快速总结
# 1. PyQuery 对象直接传入html
# 2. 通过class获取
# 3. 通过id获取
# 4. 获取属性 attr()
# 5. 多个元素获取属性
# 6. 获取文本 text()