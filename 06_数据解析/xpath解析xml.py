from lxml import etree

xml ="""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周至柔</nick>
        <nick class="jay">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>周大强</nick>
            <nick>周至柔</nick>
            <nick>周杰伦</nick>
            <nick>蔡依林</nick>
        </div>
    </author>
    <partner>
         <nick id="ppc">周大强</nick>
         <nick id="ppbc">周至柔</nick>
    </partner>    
</book>
"""
etree_xml  = etree.XML(xml)
# ret = etree_xml.xpath("/book") # / 从根节点开始查找
ret = etree_xml.xpath("/book/name/text()")[0] # / 从根节点开始查找 text() 获取文本
print(ret)

ret = etree_xml.xpath("/book/*/nick/text()") # * 代表任意节点
print(ret)

ret = etree_xml.xpath("/book//nick") # // 代表多个节点
print(ret)

ret = etree_xml.xpath("/book/author/nick[@class='jay']/text()") # @class='jay' 表示属性
print(ret)

ret = etree_xml.xpath("/book/partner/nick/@id") # @id 表示属性
print(ret)

# 取ppc的值
ret = etree_xml.xpath("/book/partner/nick[@id='ppc']/text()") # @id 表示属性
print(ret)
