# 什么是sql？
    - sql是指结构化查询语言
    - sql使我们有能力访问数据库
    - sql使一种ANSI的标准计算机语言
# sql能做什么？
    - sql面向数据库进行查询
    - sql可从数据库取回数据
    - sql可在数据库中插入新的纪录
    - sql可更新数据库中的纪录
    - sql可从数据库删除纪录
    - sql可创建新的数据库
    - sql可在数据库中创建新表
    - sql可在数据库中创建存储过程
    - sql可在数据库中创建视图
    - sql可以设置表、存储过程和视图的权限

- sql对大小写不敏感
- distinct代表去重
- 可以把sql分为两个部分：数据操作语言（DML）和数据定义语言（DDL）
    - 查询和更新指令构成了sql的dml部分：（增删改查）
        - select - 从数据库表中获得数据
        - update - 更新数据库表中的数据
        - delete - 从数据库表中删除数据
        - insert into - 向数据库表中插入数据
    - sql的数据定义语言
        - create database - 创建数据库
        - alter database - 修改数据库
        - create table - 创建新表
        - alter table - 变更（改变）数据库表
        - drop table - 删除表
        - create index - 创建索引（搜索键）
        - drop index - 删除索引


- where 子句用于规定选择的标准
    - where 子句
        - select 列名称 from 表名称 where 列 运算符 值
            = ：等于
            <>: 不等于
            >:大于
            <:小于
            >=:大于等于
            <=:小于等于
            between:在某个范围内
            like:搜索某种模式
            在某些版本中的sql中，操作符<>可以写为！=

    - 在条件值周围使用的是单引号
    - sql使用单引号来环绕文本值。如果是数值则不需要加任何引号

- and和or运算符用于基于一个以上的条件纪录进行过滤
    - and和or运算符
        - and和or可在where子语句中把两个或多个条件结合起来
        - 如果第一个条件和第二个条件都成立，则and运算符显示一条记录
        - 如果第一个条件和第二个条件中只要有一个成立，则or运算符显示一个条纪录

    - order by语句用于对结果集进行排序
        - order by语句用于根据指定的列对结果进行排序
        - order by语句默认按照升序对纪录进行排序
        - 降序用desc 升序asc
- insert into 语句用于向表格中插入新的行
    - 语法
        - insert into 表名称 values （值1，值2，。。。）
        - insert into 表名称（列1，列2，。。） values（值1，值2，。。。）

- update语句用于修改表中的数据
    - 语法
        - update 表名称 set 列名称 = 新值 where 列名称 = 某值
        - 可以更新某一行中的若干列

- delete语句
    - 语法
        - delete from 表名称 where 列名称 = 值
    - 删除所有行
        - 可以在不删除表的情况下删除所有的行。这意味着表的结构，属性和索引都是完整的
            - delete from table_name
            - delete * from table_name

- top子句用于规定要返回的纪录的数目
    - 并非所有的数据库都支持top子句。
        - sql server的语法：

            - select top number|percent column_name from table_name
            - select top 2 * from table_name(从表中选取2条纪录)
            - select top 50 percent * from table_name(从表中选取50%的纪录)

        - mysql和oracle中的sql
            - select column_name from table_name limit number

        - oracle中的语法
            - select column_name from table_name where rownum <=number
- like 操作符用于在where 子句中搜索列中的指定模式
    - 相当于模糊查询
        - %为通配符
        - like 和 not like
- sql中的通配符
    - 在搜索数据库中的数据时，sql通配符可以替代一个或多个字符
    - sql通配符必须于like运算符一起使用
    - 在sql中，可使用一下通配符：
        - % ：替代一个或者多个字符
        - _ : 进代替一个字符
        - [charlist] : 字符列中的任何单一字符
        - [^charlist] 或者 [!charlist] 不在字符列中的任何单一字符
            - select * from person where city like '[ALN]%'(从person表中选取居住的城市以'A'、'L'或'N'开头的人)
            - [!ALN]% 表示不以这些字母开头


- in操作符允许我们在where子句中规定多个值
    - select column_name from table_name where column_name in (value1,value2...)

- between 操作符在where子句中使用，作用是选取介于两个值之间的数据范围
    - 操作符between ... and 会选取介于两个值之间的数据范围。这些值可以是数值，文本或者日期
    - 显示范围之外用not between

- as 可以为列名和表名称指定别名
    - 使用别名更易阅读和书写，但不会改变原始表】


- join 用于根据两个或多个表中列之间的关系，从这些表中查询数据
    - 数据库中的表可通过键将彼此联系起来。主键是一个列，在这个列中的每一行的值都是唯一的。
      在表中每个主键的值都是唯一的。这样做的目的是在不重复每个表中的所有数据的情况下，把表间的数据交叉捆绑在一起
    - 不同的join
        - join：如果表中有至少一个匹配，则返回行（返回两个表中同时满足的元组对，不满足将被丢弃）
        - left join：即使右表中没有匹配，也从左表返回所有的行（返回左表所有行以及右表满足条件的行，左表有值右表无值填充为null）
        - right join：即使左表中没有匹配，也从右表返回所有的行（返回右表所有行以及左表满足条件的行，右表有值左表无值填充为null）
        - full join：只要其中一个表中存在匹配，就返回行（返回所有表的所有行，在满足条件的行之外，两表不满足的均填充为null）

- union操作符用于合并两个或多个select语句的结果集
    - union内部的select语句必须用手相同数量的列。列也必须拥有相似的数据类型。同时，每条select语句中的列的顺序必须相同
    - 默认的union操作符选取不同的值。如果允许重复的值，请使用union all

- select into 语句从一个表中选取数据，然后把数据插入另一个表中
- 常用于创建表的备份文件或者用于对纪录进行存档

- create database语句
    - 用于创建一个新的数据库中的表

