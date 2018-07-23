# import openpyxl
#
# filename='C:/Users/meridian/Desktop/Test2.xlsx'
# filename2='C:/Users/meridian/Desktop/新文件.xlsx'
#
# def replace_xls(sheetname):
#     wb=openpyxl.load_workbook(filename)
#     wb2=openpyxl.load_workbook(filename2)
#
#     ws=wb[sheetname]
#     ws2=wb2[sheetname]
#
#     #两个for循环遍历整个excel单元格的内容
#     for i,row in enumerate(ws.iter_rows()):
#         for j,cell in enumerate(row):
#                 ws2.cell(row=i+1,column=j+1,value=cell.value)
#     wb2.save(filename2)
# replace_xls("Sheet1")

import calendar
#自带三个参数，调整各个数之间的间隔。
cal = calendar.calendar(2018)
print(cal)
#isleap:判断某一年是否闰年
calendar.isleap(2001)

#leapdays:获取指定年份之间的闰年个数
calendar.leapdays(2001,2011)

import openpyxl

excel=openpyxl.load_workbook()
