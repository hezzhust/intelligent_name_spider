# -*- coding: utf-8 -*-
import scrapy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from name_spider.items import NameSpiderItem


class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["sohu.com"]
    start_urls = [
        "http://www.sohu.com/"
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        # title = response.xpath("/html/head/title/text()").extract();
        # print "response end", title
        for sel in response.xpath('//ul/li'):
            title = ""
            desc = ""
            link = ""
            item = NameSpiderItem()
            # if sel.xpath('a/text()').extract():
            title = sel.xpath('a/text()').extract_first()
            if title:
                title = title.replace('\n', '').replace(' ','')
            # if title and self.is_chinese(title):
            #     title = title.decode('unicode_escape')
            # if sel.xpath('a/@href').extract():
            link = sel.xpath('a/@href').extract_first()
                # if self.is_chinese(link):
                #     link = desc.decode('unicode_escape')
            # if sel.xpath('text()').extract():
            desc = sel.xpath('text()').extract_first()
            if desc:
                desc = desc.replace('\n', '').replace(' ','')
            # if desc and self.is_chinese(desc):
            #     desc = desc.decode('unicode_escape')

            item['title'] = title
            item['link'] = link
            item['desc'] = desc
            yield item
            print '标题：',title,'，链接：', link, '，描述：',desc

    def is_chinese(self, uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
            return True
        else:
            return False