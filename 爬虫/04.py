#  此种方法只是简单的进行翻译，不能伪装身份,不能中译英和句子翻译
from urllib import request,parse

import json


def fanyi():
    # 需要研究网页，查看基础url是什么
    url = 'https://fanyi.baidu.com/sug'
    sr=input('请输入你想翻译的词')

    # 将数据传入服务器需要将数据转换成字典格式
    data = {
        'kw':sr
    }
    # 并用parse进行编码,由于此时的data是str型，所以要将其编码为bytes的utf-8格式
    data=parse.urlencode(data).encode('utf-8')
    print(type(data))

    headers={
        'Content-Length':len(data)

    }
  #  此处添加一个Request类实例来封装headers
    req=request.Request(url=url,data=data,headers=headers)

    #rsp=request.urlopen(baseurl,data=data)
    # 此处返回的值就为Request类的实例
    rsp=request.urlopen(req)

    # html = rsp.read().decode('utf-8')
    # print(html)
    json_data=rsp.read().decode('utf-8')

    #print(type(json_data))

    #print(json_data)

    json_data=json.loads(json_data)

    #print(type(json_data))
    print(json_data)
    print('翻译结果为')
    for i in json_data['data']:

        print(i['k'],"-------",i['v'])

fanyi()
