# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NgaItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 帖子id
    tid = scrapy.Field()
    # 用户id
    uid = scrapy.Field()
    # 回帖数
    reply_num = scrapy.Field()
    # 帖子链接
    url = scrapy.Field()
