import openpyxl

class A:
    def read(self):
        e1=openpyxl.load_workbook("C:/Users/meridian/Desktop/提取练习/提取.xlsx")

        w1=e1["Sheet1"]
        print(w1['A1'].value)

        #最大行数和列数
        Maxr=w1.max_row
        Maxc=w1.max_column
        print(Maxc,Maxr)

        # 此列表用来存所有行中的数据
        l1=list()
        for i in w1['A']:
            #print(i.value,end="\n")
            l1.append(i.value)

        #print(len(l1))
        # 此列表用来存拆分后的数据
        l2=list()
        for j in l1:
            l3=j.split('。')
            for i in l3:
                if i=="":
                    l3.remove(i)
                # if i[0].isalpha():
                #     l3.remove(i)
            l2.append(l3)

        # 此列表用来存甲开头的数据
        l4=list()
        for m in l2:
            for n in m:
                #print(n)
                if n!="":
                    if len(n) >2:
                        if n[0] =='甲':
                            l4.append(n)

        # 开始写入

        tq=openpyxl.Workbook()
        Sheet1=tq.active
        Sheet1.title="已提取"
        #l5=list()
        print("开始写入")

        Sheet1.append(l4)


        print("写入完成")

        tq.save('C:/Users/meridian/Desktop/提取练习/已提取.xlsx')



if __name__ == '__main__':
    a1=A()
    a1.read()