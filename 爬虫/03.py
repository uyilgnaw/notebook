from urllib import request,parse

if __name__ == '__main__':
    url='http://www.baidu.com/s?'
    wd=input("Input your keyword")

    # 想要使用data,需要使用字典结构
    qs={"wd":wd}

    qs=parse.urlencode(qs)

    print(qs)

    fullurl=url+qs
    print(fullurl)

    # 如果直接使用可读的带参数的url，是不能访问的
    rsp=request.urlopen(fullurl)
    html=rsp.read()

    html=html.decode()
    print(html)