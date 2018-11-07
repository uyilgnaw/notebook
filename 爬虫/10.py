from urllib import request

import time
if __name__ == '__main__':
    for i in range(10):
        url = 'https://www.douban.com/group/beijingzufang/discussion?start=10'

        headers = {

            'User-Agent': 'Mozilla/5.0',

            "Cookie":'bid=Ezp0VC8HwBU; douban-fav-remind=1; __yadk_uid=dtbo8DAT2fsUHy55FV3Vge6Qp0ab2fPj; viewed="10590856"; gr_user_id=5773bd7d-33ec-46ce-b1a9-8009dc974113; __utmz=30149280.1536644764.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _vwo_uuid_v2=DD4F2971BFEA8D11166ABD3925631FB2E|524e0a9b2391067c755c043f8deaaa95; ll="108288"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1537237124%2C%22https%3A%2F%2Fwoyaozufang.live%2FHome%2FHouseList%3Fcityname%3D%25E5%258C%2597%25E4%25BA%25AC%26source%3Ddouban%26intervalDay%3D7%26houseCount%3D500%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.101589859.1535523826.1537173649.1537237124.5; ps=y; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18176; __utmc=30149280; dbcl2="181760503:iQDztkVBQhw"; ck=J3GY; __utmt=1; _pk_id.100001.8cb4=b21844d0c359c64d.1535523825.2.1537239563.1535525845.; __utmb=30149280.63.5.1537239563462'

        }
        req = request.Request(url,headers= headers)

        rsp = request.urlopen(req)

        html = rsp.read().decode()

        print('已经爬取了一次')
        time.sleep(3)
        # with open("添加Cookie.html","w",encoding='utf - 8') as f:
        #
        #     f.write(html)
