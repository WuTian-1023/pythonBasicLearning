from lxml import etree

"""
xml = """""""
"""
# xpath 处理HTML
html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>测试</title>
    </head>
    <body>
        <div class="top">
            <span id="one">1</span>
            <span id="two">2</span>
            <span id="three">3</span>
        </div>
        <div class="bottom">
            <span id="four">4</span>
            <span id="five">5</span>
            <span id="six">6</span>
        </div>
    </body>
    </html>
"""
etree_html = etree.HTML(html)
xpath = etree_html.xpath("/html/body/div[@class='top']/span[2]/text()")
print(xpath)

html_xpath = etree_html.xpath("//span")  # // 表示多个节点
for item in html_xpath:
    print(item.xpath("./text()")[0])
    print(item.xpath("./@id")[0])
