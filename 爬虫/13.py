'''
由于12306的证书是自己制作的，所以用https进行访问时会出现警告界面
所以要使用ssl模块进行忽略


'''

from urllib import request

# 导入python 中的ssl模块

import ssl

# 利用非认证上下文换进去替换认证的上下文环境
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.12306.cn"

rsp = request.urlopen(url)

html = rsp.read().decode()

print(html)