# coding:utf-8

import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"
}
url = 'http://www.qiushibaike.com'
r = requests.get(url, headers)

soup = BeautifulSoup(r.text, 'lxml')

# divs = soup.find_all(class_='author clearfix')
divs = soup.find_all('div', {'class': 'article block untagged mb15 typs_hot'})

for divTemp in divs:
    joke = divTemp.h2.get_text()
    contentSpan = divTemp.span.get_text()
    statsVote = divTemp.i.get_text()
    # print divTemp.div.get('articleGender manIcon')
    print 'author:' + joke
    print 'content:' + contentSpan
    print 'statsVote: ' + statsVote

    print divTemp.find(class_='articleGender manIcon')

    print '---------------------------'
