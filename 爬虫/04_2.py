# 此案例可使用百度翻译翻译句子,中文翻译英文，User_Agent和url换成手机版的

from urllib import request,parse

import json


def fanyi():
    # 需要研究网页，查看基础url是什么
    url = 'https://fanyi.baidu.com/basetrans'
    sr=input('请输入你想翻译的句子')

    # 将数据传入服务器需要将数据转换成字典格式，翻译句子时会用formdata进行传输
    # 所以data要添加一些参数
    data = {
        "from":"zh",
        "to":"en",
        "query":sr,

    }
    # 并用parse进行编码,由于此时的data是str型，所以要将其编码为bytes的utf-8格式
    data=parse.urlencode(data).encode('utf-8')


    headers={

        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"

    }
  #  此处添加一个Request类实例来封装headers
    req=request.Request(url=url,data=data,headers=headers)

    #rsp=request.urlopen(baseurl,data=data)
    # 此处返回的值就为Request类的实例
    rsp=request.urlopen(req)

    html = rsp.read().decode('unicode-escape')
    print(html)



fanyi()


