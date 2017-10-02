# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .model.config import Session
from .model.proxyIP import proxyIP, BASE
from scrapy import log
import requests


class CrawlipPipeline(object):
    def open_spider(self, spider):
        self.session = Session()
    def process_item(self, item, spider):
        try:
            requests.get('http://wenshu.court.gov.cn/', proxies={"http":str(item['ip']).lstrip('[\'').rstrip('\']')})
        except:
            log.msg('*'*10,level=log.INFO)
            log.msg('*' * 10, level=log.INFO)
            log.msg('*' * 10, level=log.INFO)
            log.msg(str(item['ip'])+'is not useful', level=log.INFO)
            log.msg('*' * 10, level=log.INFO)
            log.msg('*' * 10, level=log.INFO)
            log.msg('*' * 10, level=log.INFO)
        else:
            log.msg('-'*10,level=log.INFO)
            log.msg('-' * 10, level=log.INFO)
            log.msg('-' * 10, level=log.INFO)
            log.msg('-' * 10, level=log.INFO)
            proxyip = proxyIP(ip=str(item['ip']).lstrip('[\'').rstrip('\']'),
                              port=str(item['port']).strip('[\'').rstrip('\']'),
                              high_hide=str(item['high_hide']).strip('[\'').rstrip('\']'),
                              type=str(item['type']).strip('[\'').rstrip('\']'))
            self.session.add(proxyip)
            self.session.commit()
        finally:
            return item
    def close_spider(self,spider):
        self.session.close()