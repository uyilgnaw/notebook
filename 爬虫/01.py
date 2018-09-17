from urllib import request

'''
使用urllib，request请求一个网页内容，并把内容打印出来
'''

if __name__ == '__main__':
    url='http://fanyi.baidu.com/sug'
    # 打开相应url并把相应页面作为返回

    rsp=request.urlopen(url)
    # 把返回结果读取出来
    # 都取出来内容类型为bytes

    html=rsp.read()
    print(type(html))
    # 使用decode方法将其进行解码
    html=html.decode()
    print(html)
