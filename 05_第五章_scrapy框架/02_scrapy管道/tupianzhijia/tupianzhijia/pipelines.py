import os

import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class TupianzhijiaPipeline:
    def process_item(self, item, spider):
        return item

class meinvPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        adapter = ItemAdapter(item)
        if adapter.get('img_src'):
            # 支持img_src为单个URL或URL列表
            img_src_list = adapter['img_src'] if isinstance(adapter['img_src'], list) else [adapter['img_src']]
            for img_src in img_src_list:
                yield scrapy.Request(img_src, headers={'Referer': 'https://www.tupianzj.com/'})
        else:
            raise DropItem(f"Missing img_src in {item}")

    def file_path(self, request, response=None, info=None, *, item=None):
        adapter = ItemAdapter(item)
        name = adapter.get('name', 'unknown').replace(':', '').replace('/', '')
        image_guid = request.url.split('/')[-1]
        # 确保文件名有效，移除或替换不合法字符
        filename = f"{name}/{image_guid}"
        # 使用安全的文件名和目录名
        safe_filename = "".join([c for c in filename if c.isalnum() or c in [' ', '.', '_', '-']])
        return os.path.join('img', safe_filename)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem(f"Item contains no images {item}")
        item['image_paths'] = image_paths
        return item
