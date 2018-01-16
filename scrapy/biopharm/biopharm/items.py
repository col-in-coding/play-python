# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiopharmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ticker = scrapy.Field()
    price = scrapy.Field()
    drug = scrapy.Field()
    stage = scrapy.Field()
    date_text = scrapy.Field()
    end_date = scrapy.Field()
    
