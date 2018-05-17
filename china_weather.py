# coding:utf-8


import requests

from bs4 import BeautifulSoup
import time
import json

from echarts import Echart, Bar, Axis

TEMPER_LIST = []
CITY_LIST = []
MIN_LIST = []


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
        province = ''

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
            # CITY_LIST.append(province + city)
            # MIN_LIST.append(min)

            # print '%s|%s' % (province + city, min)


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

    for url in urls:
        get_temperature(url)
        time.sleep(2)

    TOP20_TEMPERATURE_LIST = sorted(TEMPER_LIST, lambda x, y: cmp(int(x['min']), int(y['min'])))[0:20]

    # CITY20_LIST = CITY_LIST[0:20]
    # MIN20_LIST = MIN_LIST[0:20]

    CITY20_LIST = []
    MIN20_LIST = []

    for city_min in TOP20_TEMPERATURE_LIST:
        CITY20_LIST.append(city_min['city'])
        MIN20_LIST.append(city_min['min'])
    line = json.dumps(TEMPER_LIST, ensure_ascii=False)
    with open('temperatu.json', 'w') as fp:
        fp.write(line.encode('utf-8'))

    echart = Echart(u'全国最低温度排名', u'提供')
    bar = Bar(u'最低温度', MIN20_LIST)
    axis = Axis('category', 'bottom', data=CITY20_LIST)
    echart.use(bar)
    echart.use(axis)
    echart.plot()


if __name__ == '__main__':
    main()
