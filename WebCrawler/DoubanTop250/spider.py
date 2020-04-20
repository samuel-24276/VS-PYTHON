# -*- coding:utf-8 -*-

import requests
import pandas as pd
import os
import lxml.html
etree = lxml.html.etree


def get_html(url):
    headers = {'User-Agent' :
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    try:
        html = requests.get(url, headers=headers)
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            print('成功获取源代码')
            # print(html.text)
    except Exception as e:
        print('获取源代码失败:%s' % e)

    return  html.text


def parse_html(html):
    h = etree.HTML(html)
    lis = h.xpath("//ol[@class='grid_view']/li")
    movies = []
    imgurls = []
    for li in lis:
        name = li.xpath(".//a/span[@class='title']/text()")[0].strip()
        director = li.xpath(".//div[@class='bd']/p/text()")[0].strip()
        factor = li.xpath(".//div[@class='bd']/p/text()")[1].strip()
        score = li.xpath(".//div[@class='star']/span/text()")[0].strip()
        cwd = li.xpath(".//div[@class='star']/span/text()")[1].strip()
        img = li.xpath(".//img/@src")[0]
        imgurls.append(img)

        movie = {'name': name, 'director': director, 'factor': factor, 'score': score, 'cwd': cwd}
        movies.append(movie)
    return movies, imgurls


def downloading(url, movie):
    if 'moviepost' in os.listdir(r'D:\CODE\VS-Python\Web Crawler\DoubanTop250'):
        pass
    else:
        os.mkdir('moviepost')
    os.chdir(r'D:\CODE\VS-Python\Web Crawler\DoubanTop250\moviepost')

    img = requests.get(url).content
    # print(movie['name'])
    with open(movie['name'] + '.jpg', 'wb+') as f:
        #print('正在下载: %s' % url)
        f.write(img)


if __name__ == '__main__':
    MOVIES = []
    IMGURLS = []
    for i in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(i*25) + '&filter='
        html = get_html(url)
        
        movies = parse_html(html)[0]
        imgurls = parse_html(html)[1]
        '''
        for movie in movies:
            print(movie)
        '''
        MOVIES.extend(movies)
        IMGURLS.extend(imgurls)

    # for m in movies:
        # print(m)


    for i in range(250):
        downloading(IMGURLS[i], MOVIES[i])
    os.chdir(r'D:\CODE\VS-Python\Web Crawler\DoubanTop250')

    moviedata = pd.DataFrame(MOVIES)
    # print(MOVIES)
    moviedata.to_csv('movie.csv', encoding='utf_8_sig')
    print('已保存到本地')
