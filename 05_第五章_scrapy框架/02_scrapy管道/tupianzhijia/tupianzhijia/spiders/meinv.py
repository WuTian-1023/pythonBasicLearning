import scrapy

from tupianzhijia.items import TupianzhijiaItem

'''
 遇到反爬了 
    百度一下看看
    果然是需要 用cookie模拟浏览器行为
  scrapy crawl meinv
<script language="javascript" type="text/javascript">eval(function(p,a,c,k,e,d){e=function(c){return(c<a?"":e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,S
tring)){while(c--)d[e(c)]=k[c]||e(c);k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1;};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p;}('p b(j){1 7=j+"=";1 a=
3.4.o(\';\');u(1 i=0;i<a.9;i++){1 c=a[i].s();f(c.q(7)==0)g c.v(7.9,c.9)}g""}1 6=b("6");1 5=B(b("5"));f(6==""||5==""){D("8=8; ",C)}x{1 k=5-y;3.4="6=; d=e, m l n 2:2:2 h;";3.4="5=; d=e, m l n 2:2:2 h;";3
.4="t="+6+";";3.4="r="+k+";";A.8.z(w)}',40,40,'|var|00|document|cookie|secret|token|name|location|length|ca|getCookie||expires|Thu|if|return|UTC||cname|random|Jan|01|1970|split|function|indexOf||trim||for|substring|true|else|100|reload|window|parseInt|3000|setTimeout'.split('|'),0,{}))
</script>
'''


class MeinvSpider(scrapy.Spider):
    name = "meinv"
    allowed_domains = ["tupianzj.com"]
    start_urls = ["https://www.tupianzj.com/meinv/siwa/"]

    # cookie用于模仿浏览器行为
    cookie = {
        "t": "173d9d44f3cb8f7029f8e1c7a6ef0ebd",
        "r": "6653",
        "Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273": "1708331981,1708391997",
        "arp_scroll_position": "900",
        "Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273": "1708394631",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": "https://www.tupianzj.com/meinv/",
    }

    def start_requests(self):  # 重构start_requests函数
        """
        重构start_requests函数，用于发送带有cookie的请求，模仿浏览器行为
        """
        yield scrapy.Request("https://www.tupianzj.com/meinv/siwa/", callback=self.parse, cookies=self.cookie,
                             headers=self.headers)

    def parse(self, response, **kwargs):
        print(response.text)
        li_list = response.xpath("//ul[@class='list_con_box_ul']/li")
        for li in li_list:
            href = li.xpath("./a/@href").extract_first()  # 提取链接
            yield scrapy.Request(
                url=response.urljoin(href),
                callback=self.parse_detail,  # 将parse_detail作为回调函数
                cookies=self.cookie
            )
        # 翻页
        # 获取下一页的链接
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        # 判断是否有下一页 如果有就继续爬取 如果没有就结束  next_url = javascript:dPlayNext(); 就代表没有了
        if next_url != "javascript:dPlayNext();":
            # 如果有下一页
            # 拼接下一页的链接
            next_url = response.urljoin(next_url)
            # 发送请求
            yield scrapy.Request(
                url=next_url,
                callback=self.parse,
                cookies=self.cookie
            )

    def parse_detail(self, response, **kwargs):
        # 拿到图片的名称
        name = response.xpath("//*[@id='container']/div/div/div[2]/h1/text()").extract_first()
        '''
        # 拿到图片的链接 有坑需要注意
        # 需要判断是一张还是多张图片
        # 如果是一张图片，直接提取图片链接
        # 如果是多张图片，需要提取每张图片的链接
        # id bigpicimg 这个不存在的时候，就是单张
        '''
        img = response.xpath("//*[@id='bigpicimg']").extract_first()
        # 如果是None
        if img is None:
            # 单张图片
            img = response.xpath("//div[@class='rrt']/div/img/@src").extract_first()
            # 需要处理
            img_src = 'https://www.tupianzj.com' + img
            print(img_src)
            tupianzhijia_item = TupianzhijiaItem(name=name, img_src=img_src)
            yield tupianzhijia_item
        else:
            # 多张图片
            img_list = response.xpath("//*[@id='bigpicimg']/@src").extract()
            for img in img_list:
                tupianzhijia_item = TupianzhijiaItem(name=name, img_src=img)
                yield tupianzhijia_item
