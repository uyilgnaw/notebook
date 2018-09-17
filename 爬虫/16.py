# 爬取豆瓣电影排行榜基本版

from urllib import request

import json

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"

rsp = request.urlopen(url)

data = rsp.read().decode()
print(type(data))
#print(data)
data = json.loads(data)
#print(type(data))
print(data)
print('一共有{0}个元素'.format(len(data)))
for i in data:
    print(i['title'] +'-------' +  i['url'])
