# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
class ImagePipeline(ImagesPipeline):
    #重写get_media_requests()方法
    def get_media_requests(self, item, info):
        yield scrapy.Request(
            url = item['img_url'],
            meta={'item':item['img_title']},
        )

    def file_path(self, request, response=None, info=None):
        #获取到图片url
        item = request.url
        # request.meta属性
        filename = request.meta['name'] + '.' + item.split('.')[-1]

        return filename