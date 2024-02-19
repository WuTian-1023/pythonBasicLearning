import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class TupianzhijiaPipeline:
    def process_item(self, item, spider):
        return item

class meinvPipeline(ImagesPipeline):
    # 重写get_media_requests方法，发送图片链接的请求
    def get_media_requests(self, item, info):
        adapter = ItemAdapter(item)
        if adapter.get('img_src'):
            yield scrapy.Request(adapter['img_src'])
        else:
            raise DropItem(f"Missing img_src in {item}")

    # 重写file_path方法，指定图片的保存路径和文件名
    def file_path(self, request, response=None, info=None, *, item=None):
        adapter = ItemAdapter(item)
        # 根据item中的信息生成文件名
        image_guid = request.url.split('/')[-1]
        name = adapter.get('name', 'unknown')  # 使用 'unknown' 如果没有提供名称
        return f"img/{name}/{image_guid}"

    # 重写item_completed方法，处理下载后的事务
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem(f"Item contains no images {item}")
        item['image_paths'] = image_paths
        return item
