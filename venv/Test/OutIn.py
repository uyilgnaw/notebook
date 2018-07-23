# -*- coding=utf-8 -*-
# 此种方法不适用于数据量大的表格。
import xlrd

import xlwt

fileName="C:/Users/meridian/Desktop/Test.xlsx"

bk=xlrd.open_workbook(fileName)

st=bk.sheet_by_index(0)

nrows=st.nrows

bk1=xlwt.Workbook(encoding='utf-8')

st1=bk1.add_sheet('Test')

for i in range(0,nrows):
        row_data=st.row_values(i)

        st1_value=st.cell_value(i,2)

        print ("-------正在写入" + str(i)+"行")

        st1.write(i,1,st1_value)
bk1.save("C:/Users/meridian/Desktop/Test1.xls")
print("写入完成")









