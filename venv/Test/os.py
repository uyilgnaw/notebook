# python 中os模块的笔记

import os

'''
os 模块的方法：
===========================================
1.文件操作：
remove()/unlink()           删除文件
rename()/ renames()         重命名文件
stat()                      返回文件信息
symlink()                   创建符号链接
utime()                     更新时间戳
tmpfile()                   创建并打开（‘w+b’）一个临时文件
walk()                      生成一个目录树下的所有文件名

2.目录/文件夹操作：
chdir()/fchdir()            改变当前工作目录/通过文件描述符改变
chroot()                    改变当前进程的根目录
listdir()                   列出指定目录下的文件
getcwd()/getcwdu()          返回当前工作目录/unicode模式的返回值
mkdir()/makedirs()          创建目录/创建多层目录
rmdir()/removedirs()        删除目录/删除多层目录

3.访问/权限：
access()                    检验权限模式
chmod()                     更改权限
chown()/lchown()            更改文件所有者，GroupID/同功能，不追踪lnk
umask()                     设置默认权限

4.文件描述符操作：
open()                      打开一个文件
read()/write()              读或写一个文件
dup()/dup2()                复制文件描述符/将一个文件描述符复制到另一个
**********************************
os.path路径名访问方法：
**********************************
1.分割：
basename()                  去掉目录名，返回文件名
dirname()                   去掉文件名，返回目录名
join()                      将分离的各部分重新组合成路径名
split()                     返回（dirname（），basename()）元组
splitdrive()                返回（dirvename，pathname）元组
splittext()                 返回（文件名，扩展名）元组

2.信息：
getatime()                  返回最近访问的时间
getctime()                  返回创建的时间
getmtime()                  返回修改的时间
getsieze()                  返回文件的大小

3.查询判断：
exists()                    指定路径（文件或目录）是否存在
isbas()                     指定路径是否是绝对路径
isdir()                     判断是否未文件夹
isfile()                    判断是否是文件
islink()                    判断是否是连接
ismount()                   判断是否是挂载点
samefile()                  判断两个路径是否指向同一文件
===============================================
'''

'''
os.access(path,mode)主要是测试文件是否存在（调用os.F_OK属性）
文件有没有可读性（调用os.R_OK）
文件能不能写入（调用os.W_OK）
文件能不能执行(调用os.X_OK)方法返回的是布尔值

'''

path = os.getcwd()
#path1 = "C:/Users/meridian/Desktop/"
# 查看当前所在路径
#print(path)

# 列举目录下的所有文件(隐藏文件也能显示)。返回的是列表类型
print(os.listdir(path))

# os.path.split(path):将路径分解为（文件夹，文件名）。返回的是元组类型。
print(os.path.split(path))

# os.path.abspath(path):返回path的绝对路径
print(os.path.abspath(path))

# os.path.dirname(path):返回path中的文件夹部分，结果不包含'\'
print(os.path.dirname(path))

# os.path.basename(path):返回path中的文件名
print(os.path.basename(path))

# os.path.getmtime(path):文件或文件夹的最后修改时间，秒数
print(os.path.getmtime(path))

# os.path.getatime(path):最后访问时间
print(os.path.getatime(path))

# os.path.getctime(path):创建时间
print(os.path.getctime(path))

# os.path.getsize(path):文件或文件夹的大小，若是文件夹返回0
print(os.path.getsize(path))

# os.path.exists(path):文件或文件夹是否存在，返回True或False.不区分大小写
print(os.path.exists(path))

print(os.sep)
print(os.extsep)
print(os.pathsep)
print(os.linesep)