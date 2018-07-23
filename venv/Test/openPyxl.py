import openpyxl

excel=openpyxl.load_workbook(filename="C:/Users/meridian/Desktop/Test.xlsx",read_only=True)

#print(excel.active) #获取当前活跃的worksheet

#print(excel.read_only)  # 判断是否以只读方式打开文档

#print(excel.worksheets) # 以列表形式返回所有的worksheet表格

#print(excel.properties) # 获取文档的元数据，如标题，创建者，创建日期

#print(excel.sheetnames) # 获取工作簿中的表，返回形式为列表

#print(excel.encoding)   #   获取文档的字符集编码

#print(excel.get_sheet_names)    # 获取所有表格的名称

# print(excel.get_sheet_by_name('Sheet')) # 通过名称获取对象
#print(excel['Sheet1'])   # 建议使用这种方法

#e1=excel['Sheet1']
#excel.remove_sheet(e1)  # 删除一个表格，需要注意的是参数是对表格对象，而不是表格名称

#print(excel.sheetnames)

#print(excel.create_sheet('mrking')) #创建一个表格，参数直接用名称即可，如果表格已经存在，则忽略，不会报错。

#print(excel.sheetnames)

#for row in excel['Sheet'].iter_rows(min_row=1,max_row=5,min_col=1,max_col=9):

#    print(row)

e1=excel['Sheet1']
#print(e1['A1'].value)
#print(e1.rows[1])  #有networkx问题无法解决
#print(e1.columns[1].value)




#for row in e1.iter_rows(): #遍历表格所有数据
#    for x in range(len(row)):
#        print(row[x].value,end= " ")
#    print()

#for i in e1['A']:   # 该for循环遍历a列所有单元格并输出
#    print(i.value,end= "\n")
#print("完成功能")
#print("开始写入")

wb=openpyxl.Workbook()
sheet=wb.active
sheet.title="牛逼"
print("开始写入")
#max_row=e1.max_row
#max_column=e1.max_column

#n=int(input("输入一个大一点的数"))

#print(chr(n))

#for m in range(1,max_row+1):
#    for n in range(97,97+max_column):   #此种方法只适合不超过z列的表格。超过Z列就不满足条件
#        n=chr(n)
#        i='%s%d'%(n,m)
        #print(i)
#        cell1=e1[i].value
#        sheet[i].value=cell1
#wb.save("C:/Users/meridian/Desktop/新文件.xlsx")

a=0
for row in e1.iter_rows():  #这种是最合适的方法
    a=a+1
    #print(type(row))
    #print(type(list(row)))
    l=list(row)
    l1=[]
    for x in range (len(l)):
        m=row[x].value
        l1.append(m)
    sheet.append(l1)

    print(a)
    #gc.collect()

wb.save("C:/Users/meridian/Desktop/新文件.xlsx")


#a=0
#for row in e1.iter_rows():  #这种方法可以将一个工作簿中的所有数据循环遍历出来，但此方法运行速度过慢且占用资源严重
#    a=a+1
#    b=0
#    for x in range(len(row)):
#        b=b+1
#        m=row[x].value
#        sheet.cell(a,b).value=m
#   print("已经写入了{0}行数据".format(a))
#wb.save("C:/Users/meridian/Desktop/新文件.xlsx")

#print(type(sheet.columns))
#print(sheet.columns[1].value)
#for i in sheet.columns:

##a=0    #定义一个自变量
#for j in e1['A']:  #for循环遍历a列
#    a=a+1
#    sheet['A{0}'.format(a)].value=j.value  #将a列的值循环填入到新表中，只能循环一列数据
#    print("已经写入了{0}条数据！".format(a))
#wb.save("C:/Users/meridian/Desktop/新文件.xlsx")