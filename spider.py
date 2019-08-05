import scrapy
import logging
import json

logging.getLogger('scrapy').setLevel(logging.WARNING)


class spider(scrapy.Spider):

    name = 'Spider'

    try:
        with open('data.json') as json_file:
            data = json.load(json_file)
    finally:
        json_file.close()

    start_urls = data

    def start_requests(self):
        index = 0
        for url in self.start_urls:
            index += 1
            yield scrapy.Request(url, callback=self.parse,
                                 cb_kwargs=dict(index=index))

    def parse(self, response, index):
        yield {
            'Index': index,
            'Title': response.xpath(
                '//div[@class="title"]/h1/text()').get(),
            'Description': response.xpath(
                '//div[@class="description"]/p/text()').get(),
            'URL': response.request.url,
            'ImageURL': response.xpath(
                '//img[@id="image"]/@src').get()
        }
