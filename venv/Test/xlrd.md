# xlrd的使用
    - xlrd中的类：
        ·sheet  工作表
        ·workbook   工作簿
        ·cell   单元格
        ·slice  切片
    - 基本操作1：打开工作簿
        ·workbook=xlrd.open_workbook(filename)
        ·filename为xls文件的完整路径
    - workbook类方法：
        ·book.sheet_names()  返回excel中所有sheets的名字，list类型
        ·book.sheet_by_index(sheet_index)   excel中的sheet索引从0开始，获取索引为sheet_index处的工作表对象
        ·book.sheet_by_name(sheet_name) 返回名字为sheet_name的对象
        ·book.sheets()  返回excel中所有的sheets对象，list类型
        ·book.sheet_loaded(sheet_name_or_index='sheet1')    如果加载了sheets为'sheet1'的单元，则返回true，否则返回false，如果excel中不存在名为sheet1的单元则抛出XLRDError
        ·book.unload_sheet(self,sheet_name_or_index)    索引为index或者表名为name的工作表不能再使用
    - 基本操作2：打开工作表
        ·sheet=workbook.sheet_by_index(sheet_index)
        ·sheet_index处填入0开始的工作表编号
        ·book.sheet_by_name(sheet_name)
        ·sheet_name处填入工作表的名称（字符串）
    -sheet类方法：
        ·sheet.name str,sheet名字 获取工作表名称
        ·sheet.nrows    int,行数  获取工作表行数
        ·sheet.ncols    int,列数  获取工作表列数
        ·sheet.row(row) list,xlrd,sheet,cell    获取rowx行的所有单元对象
        ·sheet.row_values(num)  list,第num行的值    获取工作表中第num行的内容
        ·sheet.row_slice(rowx,start_colx=0,end_colx=None)   获取rowx行中，start_colx->end_colx内的单元
        ·sheet.row_types(rowx,start_colx=0,end_colx=None)   获取rowx行中，start_colx->end_colx内的单元类型
        ·sheet.get_rows()   generator   所有行的生成器
        ·sheet.col(colx)    list,xlrd,sheet,cell    获取colx列的所有单元对象
        ·sheet.col_values(num) list,第num列的值 获取工作表中第num列的内容
        ·sheet.col_slice(colx,start_rowx=0,end_rowx=None)   list,xlrd,sheet,cell    获取colx中，start_rowx->end_rowx内的单元
        ·sheet.col_types(colx,start_rowx=0,end_rowx=None)   list    获取colx列中，start_row->end_rowx内的单元类型
        ·sheet.cell(rowx,colx) xlrd.sheet.cell  获取rowx行，colx列的单元对象
        ·sheet.cell_value(rowx,colx) rowx行，colx列的值
        ·sheet.celltype(rowx,colx)  返回单元的类型 获取（row，col）处的类型
        ·sheet.put_cell(row,col,ctype,value,xf=0)   None    修改（row，col）处的值，ctype为单元类型（只是修改程序中此处的值，不会影响源文件）
    - cell类主要属性：value和ctype
        ·value为单元格的值
        ·ctype为单元格的类型，以数字表示
        0：empty,1: string,2：number,3: date,4: boolean，5：error
    -使用技巧：
        ·