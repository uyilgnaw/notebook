'''
案例14的代码只是举例，不能翻译其他的内容

通过查找网页的页面我们找到js代码中的操作代码


'''

import json

import time,random

# md5需要hashlib库
import hashlib

from urllib import request,parse

def getSalt():
    '''
    将盐的公式用python表示出来
    :return:
    '''
    # time.time是以秒为单位的时间，而salt是以毫秒为单位的时间
    # 所以要将time.time乘以1000，加上一个随机数
    salt = int (time.time()* 1000) + random.randint(0,10)

    return salt

def getMD5(v):
    md5 = hashlib.md5()

    md5.update(v.encode("utf-8"))

    sign = md5.hexdigest()

    return sign

def getSign(key,salt):
    sign = 'fanyideskweb' + key + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"


    sign = getMD5(sign)

    return sign

def read(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
     # 得到一把盐，要保证 此处得到盐和下面的盐相同，否则不会成功
    salt = getSalt()
    # key为你想要查找的词
    data = {
        "i": key,
        "from":"AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt) ,
        "sign": getSign(key, salt),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult": "false"
    }

   # print(data)

    # 参数data需要是bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        #"Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1548144101@10.168.8.76;JSESSIONID=aaaTLWzfvp5Hfg9mAhFkw;OUTFOX_SEARCH_USER_ID_NCOO=1999296830.4784973;___rl__test__cookies=1523100789517",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0( X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36 X-Requested-With: XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    json_data = rsp.read().decode('utf-8')
    #html = rsp.read().decode()
    #print(html)
    jsondata = json.loads(json_data)
    # print("翻译结果为：")
    #print(jsondata)
    # for i in jsondata:
    #print(list(jsondata))


    if len(jsondata) > 3:

        for i in jsondata[list(jsondata)[0]]:

            #print(i)
            for j in i:
                print(j[list(j)[0]])

        n =jsondata[list(jsondata)[len(jsondata)-1]]
        #print(n)
        print("其它解释为：")
        for i in n[list(n)[0]]:

            print(i)
    else:
        for i in jsondata[list(jsondata)[0]]:
            #print(i)
            i=i[0]
            #print(i)
            print("你翻译的结果可能是句子：")
            print(i[list(i)[0]])
if __name__ == '__main__':
    shuru = input('请输入你想翻译的词：')
    print("翻译结果为：")
    read(shuru)