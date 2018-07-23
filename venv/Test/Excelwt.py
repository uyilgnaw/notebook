# -*- coding=utf-8 -*-
import xlwt #导入xlwt模块
#  创建一个workbook对象，就相当于创建了一个excel文件
book=xlwt.Workbook(encoding='utf-8',style_compression=0)
'''
workbook类初始化时有encoding和style_compression参数
encoding：设置字符编码。设置了encoding='utf—8'，就可以输入中文
style_compression：表示是否压缩，不常用

'''
# 创建一个sheet对象，一个sheet对象对应一个excel文件表格

sheet=book.add_sheet('test',cell_overwrite_ok=True)
# test为工作表的名字，cell_overwrite_ok，表示是否可以覆盖单元格。
# 注意大小写敏感

print('姓名')
sheet.write(0,0,'姓名') #python3中不需要将中文字符串解码，直接使用即可
sheet.write(0,1,'age')
sheet.write(0,2,'hobby')
# 最后，将文件保存，r代表声明为raw字符串，这样就不会处理其中的转移字符。
book.save(r'C:\Users\meridian\Desktop\Test1.xls')





