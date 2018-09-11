
from urllib import error , request

if __name__ == '__main__':
    url = "http://www.baidu.com"

    # 使用代理的步骤
    # 1.设置代理地址
    proxy = {'http':'61.133.222.69:80'}
    # 2.创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = request.build_opener(proxy_handler)
    # 4.安装Opener
    request.install_opener(opener)
    #

    try:
        rsp = request.urlopen(url)

        html=rsp.read().decode()

        print(html)
    except Exception as e:
        print(e)