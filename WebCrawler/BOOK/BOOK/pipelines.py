# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from BOOK import settings
import pymysql

"""
# mysql数据库配置
MYSQL_HOST = 'localhost'
MYSQL_DB_NAME = 'book'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
"""


class BookPipeline(object):
    # 1.python和mysql服务建立关系
    def open_spider(self, spider):
        # 链接成功
        self.connc = pymysql.Connect(
            host=settings.MYSQL_HOST,
            database=settings.MYSQL_DB_NAME,
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PASSWORD,
            charset='utf8',
        )
    
        # 创建游标对象
        self.cur = self.connc.cursor()

    # 2.插入数据
    def process_item(self, item, spider):

        try:
            # 1.写 sql语句
            sql = 'insert into book_bookinfo values(%s,%s,%s,%s,%s,%s,%s,%s);'
            # [0, '小说', '中国当代小说', '王朔:动物凶猛（2015版）', '王朔', '北京十月文艺出版社',
            # 'http://img14.360buyimg.com22024/85445270/55406a1dNa44f2514.jpg', '35.00']

            # 格式处理，把字典类型变为列表
            items_list = list(item.values())
            # 主键占位
            items_list.insert(0, 0)
            print(items_list)

            # 2.让游标执行 Sql
            self.cur.execute(sql, items_list)
            # 事务提交
            self.connc.commit()
        except Exception as e:
            print(e)
            # 事务回滚
            self.connc.rollback()

        return item

    # 3.爬虫结束--断开和mysql的连接
    def close_spider(self, spider):
        self.cur.close()
        self.connc.close()