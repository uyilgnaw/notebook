import urllib
import chardet
if __name__ == '__main__':
    url='http://stock.eastmoney.com/news/1407,20170807763593890.html'
    rsp=urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))
    html=rsp.read()

    # cs=chardet.detect(html)
    # print(type(cs))
    #
    # print(cs)

    # html=html.decode(cs.get("encoding","utf-8"))
    # print(html)