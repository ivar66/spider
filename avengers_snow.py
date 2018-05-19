# coding:utf-8
# SnowNLP是python中用来处理文本内容的，
# 可以用来分词、标注、文本情感分析等，情感分析是简单的将文本分为两类，
# 积极和消极，返回值为情绪的概率，越接近1为积极，接近0为消极。代码如下：


import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt

f = open('avengers.txt', 'r')
list = f.readlines()
sentimentslist = []
for i in list:
    s = SnowNLP(i)
    # print s.sentiments
    sentimentslist.append(s.sentiments)
plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
plt.xlabel('Sentiments Probability')
plt.ylabel('Quantity')
plt.title('Analysis of Sentiments')
plt.show()
