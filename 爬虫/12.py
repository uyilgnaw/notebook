from urllib import request, parse
from http import cookiejar


filename = 'cookie1.txt'
# 创建cookiejar实例
#cookie = cookiejar.CookieJar()
cookie = cookiejar.MozillaCookieJar(filename)



# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器

http_handler = request.HTTPHandler()
# 生成https管理器

https_handler = request.HTTPSHandler()

# 创建请求管理器

openr = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    '''
    负责初次登陆
    得到cookie凭证

    :return:
    '''
    # 此url需要从form的action属性中获取
    url = 'http://www.renren.com/PLogin.do'

    # 此键值需要从登陆form的两个对应input中提取name属性

    data = {
        "email": "18515199798",
        "password": "自己的密码"

    }

    # 需要将数据进行编码
    data = parse.urlencode(data)

    req = request.Request(url, data=data.encode())

    # 使用openr发起请求

    rsp = openr.open(req)

    # 保存cookie到文件

    # ignore_discard表示即使cookie将要被丢弃也要保存下来
    # ignore_expires表示如果该文件中cookie即使已经过期，也会保存

    cookie.save(ignore_discard=True,ignore_expires=True)



if __name__ == '__main__':
    login()

    print('已经获取了cookie凭证')


    print('已经成功添加并完成')
    print('运行结果生成一个html文件，点击直接就是登陆状态无需添加密码')