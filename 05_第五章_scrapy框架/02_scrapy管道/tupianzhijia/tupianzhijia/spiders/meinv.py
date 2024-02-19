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
        "t": "d2f08dc16b55757689da08f387a1351d",
        "r": "2454",
        "Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273": "1708331981",
        "Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273": "1708341100",
        "arp_scroll_position": "0",
    }

    def start_requests(self):  # 重构start_requests函数
        """
        重构start_requests函数，用于发送带有cookie的请求，模仿浏览器行为
        """
        yield scrapy.Request("https://www.tupianzj.com/meinv/siwa/", callback=self.parse, cookies=self.cookie)

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
