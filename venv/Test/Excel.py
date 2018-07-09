#-*- coding:utf-8 -*-
import xlrd

xlsfile=r"C:\Users\meridian\Desktop\Test.xlsx"  #打开指定路径中的xlsx文件，r代表\\。可以不加r，但是路径要用/来表示。

book=xlrd.open_workbook(xlsfile)        #得到excel文件的book对象，并实例化对象。如果不需要获取表格名称的话，后续操作可以一直用这个对象来调用

sheet0=book.sheet_by_index(0)   #通过sheet索引获得sheet对象

print("1",sheet0)
sheet_name=book.sheet_names()[0]        #获得指定索引的sheet表名字

print("2",sheet_name)

sheet_names=book.sheet_names()  #将所有工作表放入list中
print(type(sheet_names))

for j in sheet_names:   #遍历集合，得到所有工作表的名称
        print(j)

sheet1=book.sheet_by_name(sheet_name)   #通过sheet名字来获取，如果知道sheet名字可以直接指定

nrows=sheet0.nrows      #或取总行数
print("3",nrows)

for i in range(nrows):  #循环遍历每一行的值
        print(sheet0.row_values(i))

ncols=sheet0.ncols      #获取总列数
print("4",ncols)

row_data=sheet0.row_values(0)   #通过索引获取索引号的行值
print("5",row_data)

col_data=sheet0.col_values(0)   #通过索引获取索引号的列值
print("6",col_data)

cell_value1=sheet0.cell_value(0,0)      #通过坐标读取单元格的值
print("7",cell_value1)
cell_value2=sheet0.cell_value(0,1)
print("8",cell_value2)


