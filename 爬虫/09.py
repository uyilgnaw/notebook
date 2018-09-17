from urllib import request

if __name__ == '__main__':
    url = 'http://www.renren.com/965187997/profile'

    rsp = request.urlopen(url)

    html = rsp.read()

    html = html.decode()

    # print(html)
    with open ("rsp.html","w",encoding = 'utf -8') as f:
        f.write(html)

