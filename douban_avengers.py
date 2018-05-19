# coding:utf-8

import requests
from bs4 import BeautifulSoup
import re
import time
import random


def get_comments(url):
    headers = {
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/subject/24773958/?from=showing',
        # 'cookie':'bid=PUAVtyeRokg; gr_user_id=e651981e-a242-4a77-a4a8-a666484f07c3; _vwo_uuid_v2=D4F884D7D16E433229170670A6B8D9E8B|ffaed606c945efaa0eb95e666090bc3e; ll="108288"; __utmc=30149280; __utmc=223695111; ap=1; __utmz=30149280.1526732644.8.3.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/qq_34777600/article/details/77460380; __utmz=223695111.1526732644.5.3.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/qq_34777600/article/details/77460380; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1526737656%2C%22https%3A%2F%2Fblog.csdn.net%2Fqq_34777600%2Farticle%2Fdetails%2F77460380%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.2139543112.1523975327.1526732644.1526737656.9; __utma=223695111.1993260330.1523980482.1526732644.1526737656.6; ct=y; __utmt=1; ps=y; __utmb=30149280.4.10.1526737656; dbcl2="141994285:7kA3vJmal8Q"; ck=vyr9; push_noty_num=0; push_doumail_num=0; __utmb=223695111.14.10.1526737656; _pk_id.100001.4cf6=a11a022059bbd602.1523980482.6.1526740633.1526733250.',
        'Upgrade-Insecure-Requests': 1,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    return requests.get(url, headers)

# 保存当前评论的数据到txt中
def save_comments(result):
    soup = BeautifulSoup(result.content, 'lxml')
    all_comments = soup.findAll('div', class_='comment')
    with open('avengers.txt', 'a') as fp:
        for comments in all_comments:
            # print comments.p.get_text()
            fp.write((comments.p.get_text().strip() + '\r\n').encode('utf-8'))


# 获取当前的评论总数
def get_count_comment():
    url = 'https://movie.douban.com/subject/24773958/comments?status=P'
    result = get_comments(url)
    soup = BeautifulSoup(result.content, 'lxml')
    count = soup.find('ul', class_='fleft CommentTabs')
    return (count.li.get_text())[4:-2] #截取字符串


def main():
    count = get_count_comment()
    print '总共有{}页数据'.format(count)
    # page = int(count) / 20
    for num in range(20, count, 20):
        url = 'https://movie.douban.com/subject/24773958/comments?start=' + str(num) + '&limit=20'
        result = get_comments(url)
        save_comments(result)
        print('第{}页评论爬取结束...'.format(num/20))
        time.sleep(2 + float(random.randint(1, 100)) / 20)


if __name__ == '__main__':
    main()
