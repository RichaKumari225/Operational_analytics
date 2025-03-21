# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ConsumeraffairsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user = scrapy.Field()
    rating = scrapy.Field()
    verified_reviewer = scrapy.Field()
    verified_buyer = scrapy.Field()
    review_date = scrapy.Field()
    text = scrapy.Field()
    helpful = scrapy.Field()
    site = scrapy.Field()
   
