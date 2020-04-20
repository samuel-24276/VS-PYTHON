# -*- coding:utf-8 -*-

import requests
import pandas as pd
import os


# 实时全部道路拥堵排名
def now_allway_info():
    data = []
    url = 'https://report.amap.com/ajax/roadRank.do?roadType=0&timeType=0&cityCode=370200'
    info = requests.get(url)  # 获取网址包含的信息
    roads_info = info.json()  # 将获得信息格式化
    roads = roads_info['tableData']  # 以数组形式存储获取的需要信息，将多余信息排除在外

    for road in roads:
        name = road['name']
        index = road['index']
        speed = road['speed']
        length = road['length']
        travelTime = road['travelTime']
        delayTime = road['delayTime']
        road_info = {
            'a_name': name,
            'b_index': index,
            'c_speed': speed,
            'd_travelTime': travelTime,
            'e_delayTime': delayTime,
            'f_length': length
        }
        data.append(road_info)
    # 将数据存储到本地
    os.chdir(r'D:\CODE\VS-Python\WebCrawler\GaodeMap')
    road_data = pd.DataFrame(data)
    road_data.to_csv('now_highway_data.csv', encoding='utf_8_sig')
    print('实时道路数据已保存到本地')


# 近七天所有道路拥堵排名
def allway_info():
    data = []
    url = 'https://report.amap.com/ajax/roadRank.do?roadType=0&timeType=2&cityCode=370200'
    info = requests.get(url)  # 获取网址包含的信息
    roads_info = info.json()  # 将获得信息格式化
    roads = roads_info['tableData']  # 以数组形式存储获取的需要信息，将多余信息排除在外

    for road in roads:
        name = road['name']
        index = road['index']
        speed = road['speed']
        length = road['length']
        travelTime = road['travelTime']
        delayTime = road['delayTime']
        road_info = {
            'a_name': name,
            'b_index': index,
            'c_speed': speed,
            'd_travelTime': travelTime,
            'e_delayTime': delayTime,
            'f_length': length
        }
        data.append(road_info)
    # 将数据存储到本地
    os.chdir(r'D:\CODE\VS-Python\WebCrawler\GaodeMap')
    road_data = pd.DataFrame(data)
    road_data.to_csv('allway_data.csv', encoding='utf_8_sig')
    print('近七天所有道路数据已保存到本地')


# 近七天高速公路拥堵排名
def highway_info():
    data = []
    url = 'https://report.amap.com/ajax/roadRank.do?roadType=1&timeType=2&cityCode=370200'
    info = requests.get(url)  # 获取网址包含的信息
    roads_info = info.json()  # 将获得信息格式化
    roads = roads_info['tableData']  # 以数组形式存储获取的需要信息，将多余信息排除在外

    for road in roads:
        name = road['name']
        index = road['index']
        speed = road['speed']
        length = road['length']
        travelTime = road['travelTime']
        delayTime = road['delayTime']
        road_info = {
            'a_name': name,
            'b_index': index,
            'c_speed': speed,
            'd_travelTime': travelTime,
            'e_delayTime': delayTime,
            'f_length': length
        }
        data.append(road_info)
    # 将数据存储到本地
    os.chdir(r'D:\CODE\VS-Python\WebCrawler\GaodeMap')
    road_data = pd.DataFrame(data)
    road_data.to_csv('highway_data.csv', encoding='utf_8_sig')
    print('近七天高速道路数据已保存到本地')


# 交通健康指数
def index_info():
    url1 = 'https://report.amap.com/ajax/cityDaily.do?cityCode=370200&dataType=1'  # 拥堵延时指数（%）
    info1 = requests.get(url1)  # 获取网址包含的信息
    cdi = info1.json()  # 将获得信息格式化

    url2 = 'https://report.amap.com/ajax/cityDaily.do?cityCode=370200&dataType=2'  # 高延时运行时间占比（%）
    info2 = requests.get(url2)  # 获取网址包含的信息
    hlrr = info2.json()  # 将获得信息格式化

    url3 = 'https://report.amap.com/ajax/cityDaily.do?cityCode=370200&dataType=3'  # 拥堵路段里程比（%）
    info3 = requests.get(url3)  # 获取网址包含的信息
    mrcr = info3.json()  # 将获得信息格式化

    url4 = 'https://report.amap.com/ajax/cityDaily.do?cityCode=370200&dataType=4'  # 平均车速（km/h)
    info4 = requests.get(url4)  # 获取网址包含的信息
    a_s = info4.json()  # 将获得信息格式化

    # 将来自不同网址的数据存储到一个数组中
    DATA = []
    for i in range(7):
        data = {
            'a_cdi': cdi[i][1],
            'b_hlrr': hlrr[i][1],
            'c_mrcr': mrcr[i][1],
            'd_as': a_s[i][1]
        }
        DATA.append(data)
    # 将数据存储到本地
    os.chdir(r'D:\CODE\VS-Python\WebCrawler\GaodeMap')
    index = pd.DataFrame(DATA)
    index.to_csv('index_data.csv', encoding='utf_8_sig')
    print('近七天指数数据已保存到本地')
    os.chdir(r'C:\Users\DEll\Desktop\paper\data')
    sum_hlrr = sum_mrcr = sum_as = 0
    for data in DATA:
        sum_hlrr += data['b_hlrr']
        sum_mrcr += data['c_mrcr']
        sum_as += data['d_as']
    filename = 'index_info.txt'
    with open(filename, 'a') as f:  # 如果filename不存在会自动创建
        f.write(str(sum_hlrr/7)+'\n')
        f.write(str(sum_mrcr/7)+'\n')
        f.write(str(sum_as/7)+'\n')
    f.close()


# 道路运行速度偏差率
def rrsdr_info():
    url = 'https://report.amap.com/ajax/cityDaily.do?cityCode=370200&dataType=5'
    info5 = requests.get(url)  # 获取网址包含的信息
    rrsdr = info5.json()  # 将获得信息格式化
    DATA = []
    for i in range(5):
        data = {'name': rrsdr[i][0], 'rrsdr': rrsdr[i][1]}
        DATA.append(data)
    # 将数据存储到本地
    os.chdir(r'D:\CODE\VS-Python\WebCrawler\GaodeMap')
    index = pd.DataFrame(DATA)
    index.to_csv('rrsdr_data.csv', encoding='utf_8_sig')
    print('道路运行速度偏差率数据已保存到本地')
    os.chdir(r'C:\Users\DEll\Desktop\paper\data')
    filename = 'index_info.txt'
    sum_rrsdr = 0
    for info in DATA:
        sum_rrsdr += info['rrsdr']
    avg_rrsdr = sum_rrsdr / 5
    with open(filename, 'a') as f:  # 如果filename不存在会自动创建
        f.write(str(avg_rrsdr)+'\n')
    f.close()


# 全国主要城市拥堵指数均值
def avg_index_info():
    DATA = []
    url = 'https://report.amap.com/diagnosis/ajax/countryindicators.do'
    info = requests.get(url)  # 获取网址包含的信息
    index_info = info.json()  # 将获得信息格式化

    for index in index_info:
        data = {
            'a_indicator': index['indicator'],
            'b_avg': index['avg'],
            'c_maxValue': index['maxValue'],
            'd_topCityName': index['topCityName'],
            'e_numGTAvg': index['numGTAvg']
        }
        DATA.append(data)
    # 将数据存储到本地
    os.chdir(r'D:\CODE\VS-Python\WebCrawler\GaodeMap')
    avg_index = pd.DataFrame(DATA)
    avg_index.to_csv('avg_index_data.csv', encoding='utf_8_sig')
    print('全国主要城市拥堵指数均值已保存到本地')
    os.chdir(r'C:\Users\DEll\Desktop\paper\data')
    filename = 'avg_index_info.txt'
    for info in DATA:
        with open(filename, 'a') as f:  # 如果filename不存在会自动创建
            f.write(str(info['a_indicator'])+'\t')
            f.write(str(info['b_avg'])+'\t')
            f.write(str(info['c_maxValue'])+'\t')
            f.write(str(info['d_topCityName'])+'\t')
            f.write(str(info['e_numGTAvg'])+'\n')
        f.close()


if __name__ == '__main__':
    now_allway_info()  # 实时全部道路拥堵排名
    allway_info()  # 近七天所有道路拥堵排名
    highway_info()  # 近七天高速公路拥堵排名
    index_info()  # 交通健康指数
    rrsdr_info()  # 道路运行速度偏差率
    avg_index_info()  # 全国主要城市拥堵指数均值
