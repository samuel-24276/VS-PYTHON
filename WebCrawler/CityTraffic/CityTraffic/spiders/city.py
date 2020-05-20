# -*- coding: utf-8 -*-
import scrapy
import requests
import re


class CitySpider(scrapy.Spider):
    name = 'city'
    allowed_domains = ['report.amap.com']
    start_urls = ['https://report.amap.com/ajax/getCityRank.do']

    def parse(self, response):
        content = response.text
        pattern = r'[{|}}]'
        # 以{}为分隔符将文本切割为列表
        cont = re.split(pattern, content)
        for r in cont:
            city_name = re.sub(r'[A-Z|a-z|0-9|\[|\]|\,|\'|\"|\:|\.|\-]', '', r)  # 获得城市名字
            # re.sub('[\u4e00-\u9fa5]')正则表达式提取中文
            city = {}
            number = re.sub('[\u4e00-\u9fa5:a-zA-Z\"-]', '', r)
            # print(number)
            label = re.search('\\d{6}', number)  # 搜索城市编号
            if label:
                city['label'] = label.group()
                city['name'] = city_name
                dym = 'https://report.amap.com/ajax/cityDaily.do?cityCode='
                index = '&dataType='
                url = dym + city['label'] + index
                # 发送请求获取这个城市的详细信息,调用parse_map()函数
                yield scrapy.Request(url, callback=self.parse_map, meta={'map': city})
            else:
                pass

    def parse_map(self, response):
        # 取字典
        city = response.meta.get('map')
        # 从reponse提取要解析的地址
        # url1 = response.url + '1'
        url2 = response.url + '2'
        url3 = response.url + '3'
        url4 = response.url + '4'
        url5 = response.url + '5'
        # 将解析网页的内容格式化
        # arr_cdi = requests.get(url1).json()
        arr_hlrr = requests.get(url2).json()
        arr_mrcr = requests.get(url3).json()
        arr_speed = requests.get(url4).json()
        arr_rrsdr = requests.get(url5).json()
        # cdi = 
        hlrr = mrcr = speed = rrsdr = 0
        # 不同城市的rrsdr的道路数量不同，用size记录
        size = len(arr_rrsdr)
        for i in range(7):
            # cdi += arr_cdi[i][1]  # cdi有的城市有问题，为爬取所有城市的数据，暂时注释掉
            hlrr += arr_hlrr[i][1]
            mrcr += arr_mrcr[i][1]
            speed += arr_speed[i][1]      
        for i in range(size):
            rrsdr += arr_rrsdr[i][1]
        # 将double转为str，否则无法存入数据库
        # city['cdi'] = str(cdi/7)
        city['hlrr'] = str(hlrr/7)
        city['mrcr'] = str(mrcr/7)
        city['speed'] = str(speed/7)
        city['rrsdr'] = str(rrsdr/size)
        yield city
