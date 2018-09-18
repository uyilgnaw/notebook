import time# 时间函数库，包含休眠函数sleep()
import random
import requests ##导入requests
import csv
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
ip_list=[
  '180.27.98.245:8080', '37.143.161.4:41258', '151.106.25.2:1080']
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
csv_file=open("C:/Users/meridian/Desktop/租房信息/成都女生租房.CSV", 'w',newline='')#你想保存的位置
csv_writer = csv.writer(csv_file)
for i in range(50):#页码 爬取前50页信息
 #需要爬取的网址，用同样的形式替换，复制的网址start=后面的数字掉即可
 url = 'https://www.douban.com/group/chengduhezu/discussion?start='+str(i*25)
 UA = random.choice(user_agent_list)
 headers = {'User-Agent': UA,
            "Cookie": 'bid=Ezp0VC8HwBU; douban-fav-remind=1; __yadk_uid=dtbo8DAT2fsUHy55FV3Vge6Qp0ab2fPj; viewed="10590856"; gr_user_id=5773bd7d-33ec-46ce-b1a9-8009dc974113; __utmz=30149280.1536644764.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _vwo_uuid_v2=DD4F2971BFEA8D11166ABD3925631FB2E|524e0a9b2391067c755c043f8deaaa95; ll="108288"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1537237124%2C%22https%3A%2F%2Fwoyaozufang.live%2FHome%2FHouseList%3Fcityname%3D%25E5%258C%2597%25E4%25BA%25AC%26source%3Ddouban%26intervalDay%3D7%26houseCount%3D500%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.101589859.1535523826.1537173649.1537237124.5; ps=y; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18176; __utmc=30149280; dbcl2="181760503:iQDztkVBQhw"; ck=J3GY; __utmt=1; _pk_id.100001.8cb4=b21844d0c359c64d.1535523825.2.1537239563.1535525845.; __utmb=30149280.63.5.1537239563462'
            }
 random_ip = random.choice(ip_list)
 proxy = {'https': random_ip,}
 try:
        #rec = requests.get(url, headers=headers)
        rec = requests.get(url, headers=headers,proxies=proxy)#需要ip的话打开这个
        Soup = BeautifulSoup(rec.text, 'lxml')
        a_list = Soup.find_all('a',class_="",title=True)
        for a in range(len(a_list)):#
            title = a_list[a]['title']# 取出a标签的href 属性
            href = a_list[a]['href']
            print(title,"第%d页第%d个"%(i+1,a+1))
            title_1=[]
            title_1.append(title+"第"+str(i+1)+"页第"+str(a+1)+"个")
            title_1.append(href)
            csv_writer.writerows([title_1])
            title_1=[]
            time.sleep(5)#休息0.8s 如果出现链接失败，可以把间隔时间加长
 except:
        print ('connect failed',random_ip)
        random_ip = random.choice(ip_list)
 time.sleep(3)
csv_file.close()
