

import html_downloader, html_parser, html_outputer
import time
import random

class BOSS_Main(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def start(self,keyword, baseURL, page_count):

        all_coms = []

        for i in range(1, page_count+1):
            # 添加延迟
            time.sleep(random.uniform(1, 5))
            # 获取网页内容
            content = self.downloader.get_page(baseURL, i, keyword)
            # 解析数据
            com_results = self.parser.parse(content)

            print("正在抓取第 %d 页数据, 有 %d 条数据" % (i, len(com_results)))
            # 保存数据到列表
            for com in com_results:
                all_coms.append(com)

        print(len(all_coms))
        print(all_coms)

        tag_name = ['公司名称', '职位名称', '工资', '所需学历', '公司介绍']
        # self.outputer.save_to_excel(all_coms, tag_name, "test")
        # 输出
        self.outputer.save_to_excel_other_way(all_coms, tag_name, "boss1")

# 程序的入口
if __name__ == "__main__":

    keyword = input('请输入抓取的关键词：\n')
    page_counts = input("请输入抓取总页数：\n")

    baseURL = "http://www.zhipin.com/job_detail/"
    bosszp = BOSS_Main()
    bosszp.start(keyword, baseURL, int(page_counts))
