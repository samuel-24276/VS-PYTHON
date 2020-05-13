# -*- coding: utf-8 -*-
import scrapy
# import requests
import re


class QingdaoSpider(scrapy.Spider):
    name = 'qingdao'
    start_urls = ['https://report.amap.com/ajax/getCityRank.do']

    def parse(self, response):
        content = response.text
        pattern = r'[{|}}]'
        cont = re.split(pattern, content)
        
        DATA = []
        for r in cont:
            city_name = re.sub("[A-Z|a-z|0-9|\[|\]|\,|\'|\"|\:|\.|\-]", "", r)
            # print(city)
            number = re.sub('[\u4e00-\u9fa5:a-zA-Z\"-]', '', r)
            # print(number)
            
            label = re.search('\\d{6}', number)
            if label:
                city = {'name': city_name, 'label': label.group()}
                DATA.append(city)
                # print(label.group())  
            else:
                pass
            
        for data in DATA:
            print(data)
            
        """
        for city in city_list:
            
            item = {}
            item['name'] = city.xpath('./a/text()')
            index = city.xpath('./a/@href')
            link = 'https://report.amap.com/ajax/cityDaily.do?cityCode=' + re.sub("\D", "", index) + '&dataType='
            for i in range(1, 5):
                link = link + str(i)
                print('*'*100)
                print(link)
        """
    """
    def parse(self, response):
        url = 'https://report.amap.com/ajax/cityDaily.do?cityCode=370200&dataType='
        info1 = requests.get(url+'1')  # 获取网址包含的信息:拥堵延时指数（%）
        info2 = requests.get(url+'2')  # 获取网址包含的信息:高延时运行时间占比（%）
        info3 = requests.get(url+'3')  # 获取网址包含的信息:拥堵路段里程比（%）
        info4 = requests.get(url+'4')  # 获取网址包含的信息:平均车速（km/h) 
        # 将来自不同网址的数据存储到一个数组中
        cdi = info1.json()  # 将获得信息格式化
        hlrr = info2.json()  # 将获得信息格式化
        mrcr = info3.json()  # 将获得信息格式化
        a_s = info4.json()  # 将获得信息格式化
        item = response.meta.get('map')
        for i in range(7):
            item = {
                'a_cdi': cdi[i][1],
                'b_hlrr': hlrr[i][1],
                'c_mrcr': mrcr[i][1],
                'd_as': a_s[i][1]
            }            
            yield item
    """
