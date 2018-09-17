# 1.爬虫简介
- 爬虫特征：
    - 能按照作者要求下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤：
    - 下载网页
    - 提取正确的信息
    - 根据一定的规则自动跳到另外的网页上执行上两部内容
- 爬虫分类：
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）

- python爬虫需要用到的包：
    - python3：urllib，requests，
    - 案例01

# 2.urllib
- 包含模块
    - urllib.request:打开和读取urls
    - urllib.error:包含urllib.request产生的常见的错误，使用try捕捉
    - urllib.parse：包含即系url的方法
    - urllib.robotparse:解析tobots.txt文件
- 网页编码问题解决
    - 案例02
    - urlopen的返回对象
         - geturl:返回请求对象的url
         - info：请求返反馈对象的meta信息
         - getcode：返回的http code
- request.date的使用
    - 访问网络的两种方法
        - get：
            - 利用参数给服务器传递信息
            - 参数为dict，然后用parse编码
            - 案例03
        - post：
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 我们如果想使用post信息，需要用到data参数
            - 使用post，意味着http的请求可能需要更改
                - Context-Type：application/x-www.form-urlencode
                - Context-Length:数据长度
                - 一旦更改请求方法，请注意其它请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的格式
            - 案例04
            - 为了更多的设置请求信息，单纯的通过urlopen函数已经不够
            - 需要利用request.Request类
            - 案例在04的注释中
- urllib.error
    - URLError产生的原因：
        - 没网
        - 服务器连接失败
        - 案例05
    - HTTPError是URLError的一个子类
        - 案例06

    - 两者的区别在于：
        - HTTPError是对应的HTTP请求的返回码错误，如果返回错误码是400以上，则引发HTTPError
        - URLError对应的一般是网络出现问题，包括url问题
        - 关系区别：OSError-URLError—HTTPError

- UserAgent
    - UserAgent: 用户代理，简称UA，属于heads的一部分，服务器通过UA来判断访问者身份
    - 常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包


      1.Android

      Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
      Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
      Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1

      2.Firefox

      Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0
      Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0

      3.Google Chrome

      Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36
      Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19

      4.iOS

      Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3
      Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3



- 设置UA可以通过两种方式
    - heads
    - add_header
    - 案例07

- ProxyHandler处理（代理服务器）

    - 使用代理IP，是爬虫的常用手段
    - 获取代理服务器的地址：
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问IP，代理也不允许频繁访问某一个固定的网站，所以代理要很多
    - 基本使用步骤：
        - 设置代理地址
        - 创建ProxyHandler
        - 创建Opener
        - 安装Opener
    - 案例08

- cookie 和 session

    -  由于http协议的无记忆性，所以有了一个补充协议
    - cookie是给用户的（即http浏览器）的一段信息，session是保存在服务器上的对应的另一半的信息，用来纪录用户详细信息
- cookie和session的区别
    - 存放位置不同
    - cookie不安全
    - session会保存在服务器上一定时间，会过期
    - 单个cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个cookie（不是所有浏览器都限制）

- session的存放位置
    - 存放在服务器上
    - 一般情况下，session是放在内存中或者数据库中的
- 没有cookie登陆 案例09。没使用cookie反馈结果为未登录状态

- 使用cookie登陆
    - 直接把cookie复制下来，然后手动放入请求头，案例10
    - http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie
        - CookieJar
            - 管理存储Cookie，向传出的http请求添加cookie
            - cookie存在于内存中，CookieJar实例回收后cookie将消失
        - FileCookieJar(filename,delayload=None,policy=None):
            - 使用文件管理cookie
            - filename为保存cookie的文件
        - MozillaCookieJar(filename,delaylocad=None,policy=None)：
            - 创建与mocilla浏览器cookie.txt兼容的FileCookieJar实例
        - LwpCookieJar(filename,delayload=None,policy=None):
            - 创建与libwww-perl标准兼容的Set-Cookie3格式的filecookiejar实例
        - 他们的关系是：CookieJar-->FileCookieJar-->MozillaCookieJar&LwpCookieJar
    - 利用cookiejar访问人人网
        - 案例11
        - 1.自动使用cookie进行登陆，
        - 2.打开登陆界面后自动通过用户名密码登陆
        - 3.自动提取反馈回来的cookie
        - 4.利用提取的cookie登陆隐私界面

    - handler是Handler的实例，
    - 将cookie作为一个变量，打印出来
        - 案例12
- SSL
    - ssl证书就是指遵守SSL安全套接层协议的服务器数字证书（SercureSocketLayer）
    - CA是数字证书认证中心，是发放、管理和废除数字证书的收信人的第三方机构
    - 遇到不信任的SSl证书，需要单独进行处理
        - 案例13

- js加密
    - 反爬虫策略会采用js对需要传输的数据进行加密（md5）
    - 经过加密，传输的就是密文
    - 但是加密函数或者过程一般都在浏览器中完成，也就是一定会把用来加密的js代码暴露给使用者
    - 通过阅读加密算法，就可以模拟出加密过程，进而破解
    - 案例14
    - 案例15

- ajax
    - 异步请求
    - 在发起请求时一定会有url和请求方法，以及数据
    - 返回的数据一般都是json格式
    - 案例16
    - 案例18

