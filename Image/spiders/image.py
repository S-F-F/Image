# -*- coding: utf-8 -*-
import json

import scrapy
from ..items import ImageItem

class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['image.so.com']
    url = 'http://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'

    def start_requests(self):
        for sn in range(0,91,30):
            full_url = self.url.format(sn)
            # 扔给调度器入队列
            yield scrapy.Request(
                url=full_url,
                callback=self.parse_image
            )

    def parse_image(self,response):
        html = json.loads(response.text)
        item = ImageItem()
        for img_dict in html['list']:
            item['img_url'] = img_dict['qhimg_url']
            item['img_title'] = img_dict['title']

            yield item