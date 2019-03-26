# -*- coding: utf-8 -*-
from scrapy import Spider, Request
import pymongo
from crawlImages.items import CrawlimagesItem


class TaobaoSpider(Spider):
    name = 'taobao'
    allowed_domains = ['alicdn.com']

    def start_requests(self):
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        mydb = myclient['taobao']
        mycol = mydb['taobao']
        cursor = mycol.find({"sellerId": "833676353"})
        datas = []
        for item in cursor:
            datas.append(item['pics'])
        cursor.close()
        for data in datas:
            for path in data:
                yield Request(url=path['path'], callback=self.parse)


    def parse(self, response):
        item = CrawlimagesItem()
        item['path'] = response.url
        print(item)
        yield item
