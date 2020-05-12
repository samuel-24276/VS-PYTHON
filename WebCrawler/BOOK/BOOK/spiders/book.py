# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com']
    # 第一层，爬取所有图书-首页
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt[1]')
        # 遍历52个大分类
        for dt in dt_list:
            item = {}
            # 解析大分类名字
            item['category'] = dt.xpath('./a/text()').extract_first()
            # 根据大分类取小分类
            em_list = dt.xpath('./following-sibling:: *[1]/em')
            for em in em_list[:1]:
                item['small_category'] = em.xpath('./a/text()').extract_first()
                # 小分类链接需要拼接
                samll_link = 'http:' + em.xpath('./a/@href').extract_first()
                # print(item)
                
                # 发送请求获取小分类里的图书列表,调用parse_book()函数
                yield scrapy.Request(samll_link, callback=self.parse_book, meta={'book': item})

    def parse_book(self, response):
        # 取字典
        item = response.meta.get('book')
        url = response.
        print('*'*100)
        print(response)
        print('*'*100)
        # 解析所有数据
        list_book = response.xpath('//*[@id="J_goodsList"]/ul/li[@ware-type!="0"]/div')
        """
        # 遍历解析60本书的数据
        for book in list_book:
            # 书名，用相对路径./解析
            item['name'] = book.xpath('.//div[@class="p-name"]/a/em/text()').extract_first().strip()
            # 作者
            item['author'] = book.xpath('.//div[4]/span[1]/a/text()').extract_first().strip()
            # 出版社 有的书有两个出版社，取第一个
            item['store'] = book.xpath('.//div[4]/span[2]/a[1]/text()').extract_first().strip()
            # 价格
            item['price'] = book.xpath('.//div[@class="p-price"]/strong/i/text()').extract_first().strip()
            # 默认图片
            item['default_img'] = 'http:' + book.xpath('.//div[@class="p-img"]/a//img/@src').extract_first().strip()
            yield item
        """