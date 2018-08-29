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


