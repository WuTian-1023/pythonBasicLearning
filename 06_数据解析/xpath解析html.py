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
            <span id="one">one</span>
            <span id="two">two</span>
            <span id="three">three</span>
        </div>
        <div class="bottom">
            <span id="four">four</span>
            <span id="five">five</span>
            <span id="six">six</span>
        </div>
    </body>
    </html>
"""
etree_html = etree.HTML(html)
xpath = etree_html.xpath("/html/body/div/span/text()")
print(xpath)
