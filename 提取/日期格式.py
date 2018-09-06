import openpyxl

def read():
    e1=openpyxl.load_workbook("C:/Users/meridian/Desktop/提取练习/待添加.xlsx")
    w1=e1.active
    l1=[]
    for i in w1['A']:
        #print(i.value)
        l1.append(i.value)

    print(len(l1))
    l2=[]
    for j in l1:
        #print(type(j))
        #print(j.split("-"))
        l2.append(j.split("-"))

    for i in l2:
        if len(i)>1:
            if len(i[1])==1:
                i[1]="0" + i[1]
            #print(i[1])


    l4=[]
    str="-"
    for i in l2:
        l3 = []
        #print(str.join(i))
        l3.append(str.join(i))
        l4.append(l3)
    # for i in l4:
    #     print(i)

    #开始写入
    e2=openpyxl.Workbook()
    w2=e2.active
    p=0
    for i in l4:
        p=p+1
        w2.append(i)
        print("已经完成了{0}行".format(p))
    e2.save("C:/Users/meridian/Desktop/提取练习/已添加.xlsx")

read()