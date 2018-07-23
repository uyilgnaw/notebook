# openPyxl的基本用法
    ·openpyxl有三个不同层次的类，Workbook是对工作簿的抽象，Worksheet是对表格的抽象,Cell是对单元格的抽象，每一个类都包含许多属性和方法
    ·在操作excel之前，都应该创建一个Workbook对象，对于创建新的excel文档，直接进行workbook类的调用即可，对于已经存在的excel文档，可以使用openpyxl模块的load_workbook函数进行读取，该函数包含多个参数，但只有filename参数为必传参数
        - import openpyxl
            # 创建新文档
        - excel = openpyxl.Workbook('文件名')
            # 加载已存在文档
        - excel1 =openpyxl.load_workbook('文件名')
        - PS：workbook和load_workbook相同，返回的都是同一个work book对象
              workbook对象提供了很多属性方法，其中大部分方法都与sheet有关，部分属性如下：
                ·active：获取当前活跃的worksheet
                ·worksheet：以列表的形式返回所有的worksheet（表格）
                ·read_only:判断是否以read_only模式打开excel文档
                ·encoding:获取文档的字符集编码
                ·properties：获取文档的元数据，如标题，创建者，创建日期等
                ·sheetnames：获取工作簿中的表（列表）
              workbook提供的方法如下：
                ·get_sheet_names:获取所有表格的名称
                ·get_sheet_by_name:通过表格名称获取Worksheet对象，不建议使用。worksheet['表名']更合适
                ·get_active_sheet:获取活跃的表格
                ·remove_sheet:删除一个表格
                ·create_sheet:创建一个表格
                ·copy_worksheet:在workbook内拷贝表格
              worksheet对象：
                ·可以通过worksheet对象获取表格属性，得到单元格数据，修改表格中的内容。
                ·常用的worksheet属性如下
                 ·title:表格的标题
                 ·dimensions：表格的大小，即usedrange（含有数据的表格的大小）
                 ·max_row:表格里的最大行
                 ·min_row:表格里的最小行
                 ·max_column:表格里的最大列
                 ·min_column:表格里的最小列
                 ·rows:按行获取单元格（cell对象）-生成器
                 ·columns：按列获取单元格对象（cell对象）-生成器
                 ·freeze_panes:冻结窗格
                 ·values:按行获取表格的内容（数据）-生成器
                ·常用的worksheet方法如下：
                    ·iter_rows:按行获取所有单元格，内置属性有（min_row,max_row,min_col,max_col）
                    ·iter_columns:按列获取所有单元格
                    ·append：在表格末尾添加数据
                    ·merged_cells:合并多个单元格
                    ·unmerged_cells:移除合并的单元格


