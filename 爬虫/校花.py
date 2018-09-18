

'''
http://www.xiaohuar.com/list-1-0.html 第一页
http://www.xiaohuar.com/list-1-1.html 第二页
'''
# 需要先创建需保存文件的文件夹
import requests
import re
import time
from bs4 import BeautifulSoup
import random

# 以上作为基本引用
user_agent_list = [
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
  "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
  "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
  "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
  "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
  "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
  "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
  "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
  "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
 ]


def getGirls(girl_url):
    # 此处会报一个error11001异常，要抓住他
    UA = random.choice(user_agent_list)

    time.sleep(1)
    main_url = 'http://www.xiaohuar.com'
    header = {'User-Agent': UA,
                  'Connection':'close'}
    res = requests.get(girl_url, headers=header)
    res.encoding = 'gb2312'
    soup = BeautifulSoup(res.text, 'html.parser')
    for images in soup.select('.item'):
           try:
            #time.sleep(2)
            img_url = main_url + images.select('.item_t .img a img')[0]['src']
            houzhui = img_url[-4:]
            img_alt = images.select('.item_t .img a img')[0]['alt'] + houzhui
            print(img_alt)
            img = requests.get(img_url)
            with open('xiaohua/' + img_alt, "wb") as code:
                code.write(img.content)

           except Exception as e:
                print(e)
                print(res.status_code)



def url_change():
    iput = input('你想爬取多少页？')
    for i in range(int(iput)):
        url = 'http://www.xiaohuar.com/list-1-' + str(i) + '.html'
        getGirls(url)
        print('---------------->第{0}页爬取完毕'.format(i+1))


if __name__ == '__main__':
    url_change()
