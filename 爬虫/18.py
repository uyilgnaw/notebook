# 爬取豆瓣电影排行版进阶版

from urllib import request

import json

'''
这段url中：
    limit代表了一次性刷新多少元素
    start代表了从第几个电影开始刷新
    interval_id代表了好评度
    
    下面可以动态修改这些值，来达到爬取整个排行版的目的

'''

sta = 0
l1 = list()
for j in range(100):


    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={0}&limit=20".format(sta)

    rsp = request.urlopen(url)

    data = rsp.read().decode()


    data = json.loads(data)

    if len(data) > 0:
        #print('一共有{0}个元素'.format(len(data)))
        for i in data:
            #print(i['title'] +'-------' +  i['url'])
            l1.append(i['title'] +'-------' +  i['url'])


        sta = sta + 20
    else:
        break

# 添加到列表中后开始写入文件

file = open('排行榜.txt','a')

for i in l1:
    file.write(i + '\n')

file.close()

print('一共有{0}条电影数据'.format(len(l1)))
print('写入完毕')
