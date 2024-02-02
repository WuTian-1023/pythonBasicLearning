from pyquery import PyQuery

html = """
<HTML>
<div class="aaa">哒哒哒</div>
<div class="bbb">嘟嘟嘟</div>
</HTML>
"""

# PyQuery 对象直接传入html
# 加载html
query = PyQuery(html)

# 插入
query("div.aaa").after("<div class='ccc'>我是ccc</div>")
# print(query)

query("div.aaa").append("<span>我是span</span>")
# print(query)

# 修改bbb 成 aaa
query("div.bbb").removeClass("bbb").addClass("aaa") # removeClass 删除类名 addClass 添加类名
# print(query)

# ccc添加id
query("div.ccc").attr("id", "ccc") # attr 添加属性
print(query)