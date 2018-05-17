# coding:utf-8


import requests

from bs4 import BeautifulSoup
import time
import json

from echarts import Echart, Bar, Axis

TEMPER_LIST = []
CITY_LIST = []
MIN_LIST = []


# 获取当前的数据 ，并且存入字典
def get_temperature(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"
    }
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'lxml')

    conMidtabtab = soup.find('div', class_='conMidtab')

    conMidtab2_lists = conMidtabtab.find_all('div', class_='conMidtab2')

    for conMidtab2_list in conMidtab2_lists:
        tr_list = conMidtab2_list.find_all('tr')[2:]  # 从第二个元素之后开始

        for index, tr in enumerate(tr_list):
            if index == 0:
                td_list = tr.find_all('td')
                province = td_list[0].text.replace('\n', ' ')
                city = td_list[1].text.replace('\n', '')
                min = td_list[7].text.replace('\n', '')
            else:
                td_list = tr.find_all('td')
                city = td_list[0].text.replace('\n', '')
                min = td_list[6].text.replace('\n', '')

            TEMPER_LIST.append({
                'city': city,
                'min': min
            })


# 获取所有城市的最低温度
def get_temperature_result(urls):
    for url in urls:
        get_temperature(url)
        time.sleep(2)


# 将获取到的所有城市数据存入json
def save_temperature_json():
    line = json.dumps(TEMPER_LIST, ensure_ascii=False)
    with open('temperature.json', 'w') as fp:
        fp.write(line.encode('utf-8'))


# 从json文件获得所有的城市数据
def get_temperature_json():
    with open('temperature.json', 'r') as fp:
        return json.load(fp, encoding='utf-8')


# 将数据进行处理，获取到最低温度的前20名 进行展示
def data_visualization(temperature_list):
    top20_temperature_list = sorted(temperature_list, lambda x, y: cmp(int(x['min']), int(y['min'])))[0:20]
    city20_list = []
    min20_list = []
    for city_min in top20_temperature_list:
        city20_list.append(city_min['city'])
        min20_list.append(city_min['min'])

    echart_show = Echart(u'全国最低温度排名', u'小白打酱油提供', u'这是气温排名')
    bar = Bar(u'最低温度', min20_list)
    axis = Axis('category', 'bottom', data=city20_list)
    echart_show.use(bar)
    echart_show.use(axis)
    echart_show.plot()


def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml'
    ]
    # 通过爬虫获取相关的数据
    # get_temperature_result(urls)
    # 将爬虫获取到的数据放入到json
    # save_temperature_json()
    # 从json文件中获取到爬虫数据
    temperature_list = get_temperature_json()
    # 进行数据展示
    data_visualization(temperature_list)


# 设置默认启动为main函数
if __name__ == '__main__':
    main()
