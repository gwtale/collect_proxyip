# -*- coding: utf-8 -*-
import scrapy
from ..items import CrawlipItem


class CrawlIpSpider(scrapy.Spider):
    name = 'collect_ip'
    allowed_domains = ['http://www.xicidaili.com/']
    start_urls = ['http://www.xicidaili.com/nn/']

    def parse(self, response):
        node_list = response.xpath(".//tr")
        node_list = node_list[1:]
        for node in node_list:
            item = CrawlipItem()
            item['ip'] = node.xpath("./td[2]/text()").extract()
            item['port'] = node.xpath("./td[3]/text()").extract()
            item['high_hide'] = node.xpath("./td[5]/text()").extract()
            item['type'] = node.xpath("./td[6]/text()").extract()
            yield item


