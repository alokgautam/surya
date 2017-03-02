# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector 
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy import log
from scrapy import Spider
from scrapy.selector import Selector
from alok.items import AlokItem



class AbcSpider(CrawlSpider):
    name = "abc"
    allowed_domains = ["adbagency.com"]
    start_urls = (
        [l.strip() for l in open('/apps/alok/scrapy/alok/websites.txt').readlines()]
    )

    def parse(self, response):
        item =AlokItem()
        item['description'] = response.xpath('//meta[@name=\'description\']/@content').extract();
        yield item
