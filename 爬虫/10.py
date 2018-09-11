from urllib import request

if __name__ == '__main__':
    url = 'http://www.renren.com/2347295/profile'

    headers = {
        "Cookie":"自己浏览器上的cookie地址"

    }
    req = request.Request(url,headers= headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    with open("添加Cookie.html","w") as f:
        f.write(html)
