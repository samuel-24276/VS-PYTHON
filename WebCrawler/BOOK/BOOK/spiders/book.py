# -*- coding: utf-8 -*-
import scrapy
import re
import requests


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com']
    # 第一层，爬取所有图书-首页
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt')  # 52个大分类
        # 遍历52个大分类
        for dt in dt_list:
            item = {}
            # 解析大分类名字
            item['category'] = dt.xpath('./a/text()').extract_first()
            # 根据大分类取小分类
            em_list = dt.xpath('./following-sibling:: *[1]/em')
            for em in em_list[:2]:  # 每个大分类取两个小分类
                item['small_category'] = em.xpath('./a/text()').extract_first()
                print('*'*100)
                print(item)
                # 小分类链接需要拼接
                content = em.xpath('./a/@href').extract_first()
                cont = re.sub(r"[a-z|\:|\.|/]", "", content)
                index = 'https://list.jd.com/list.html?cat=' + cont + '&page='                
                small_link = re.sub(r'-', '%2C', index)
                # temp = requests.get(small_link)
                # page = int(temp.xpath('//*[@id="J_bottomPage"]/span[2]/em[1]/b'))
                s = -26
                for i in range(1):
                    s = s * 1 + 26
                    link = small_link + str(i) + '&s=' + str(s) + '&click=0'
                    print(link)
                    # 发送请求获取小分类里的图书列表,调用parse_book()函数
                    yield scrapy.Request(link, callback=self.parse_book, meta={'book': item})

    def parse_book(self, response):
        # 取字典
        item = response.meta.get('book')
        list_book = response.xpath('//*[@id="J_goodsList"]/ul/li[@ware-type!="0"]/div')
        # print(list_book)
        # 遍历解析52本书的数据,书的数量在不同的日期是变化的，为了反爬
        for book in list_book:
            # 书名，用相对路径./解析
            item['name'] = book.xpath('.//div[@class="p-name"]/a/em/text()').extract_first().strip()
            # 作者
            item['author'] = book.xpath('.//div[4]/span[1]/a/text()').extract_first()
            # 出版社 有的书有两个出版社，取第一个，有的没写作者，只有一个span
            item['store'] = book.xpath('.//div[4]/span[2]/a[1]/text()').extract_first()
            # 价格
            item['price'] = book.xpath('.//div[@class="p-price"]/strong/i/text()').extract_first()
            # 默认图片
            item['default_img'] = 'http:' + book.xpath('.//div[@class="p-img"]/a//img/@src').extract_first()
            yield item