# coding:utf-8


import requests

from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"
}
url = 'http://www.weather.com.cn/textFC/hb.shtml'
r = requests.get(url, headers)
soup = BeautifulSoup(r.content, 'lxml')

conMidtabtab = soup.find('div', class_='conMidtab')

conMidtab2_lists = conMidtabtab.find_all('div', class_='conMidtab2')

for conMidtab2_list in conMidtab2_lists:
    tr_list = conMidtab2_list.find_all('tr')
    province_tr = tr_list[2]
    td_list = province_tr.find_all('td')
    province_td = td_list[0]
    print province_td.text.replace('\n', '')
