import os

# os模块是用来调用操作系统的接口

# os.chdir(r"C:\Users")
# os.chdir("C:\\Users")
print(os.getcwd())
# os.makedirs()  递归创建目录
# os.mkdir()  不能递归

# os.removedirs(r"C:\a\b\c\d\e") 递归删除

# os.rmdir()  不能递归的删除  给了多级也只删除最后一级

# os.listdir('.')

# 删除一个文件
# os.remove()

# os.renames() 重命名文件

#查看文件 信息
# os.stat(r"a.txt")

# 输出操作系统特定的路径分隔符，win下为"\\" linux下为"\"
print(os.sep)

# 操作系统的行末结束符  win\r\n  linux \n
print(os.linesep)

#
print(os.pathsep)


# win nt  linux posix
print(os.name)

#环境变量
print(os.environ)

# os.system()  执行给定的系统命令



# os.path.abspath() 绝对路径

# os.path.split() 把文件分为两部分的元组  第一部分是路径 第二部分是文件名

# os.path.dirname() 只取目录名

# os.path.basename() 只取文件名

# os.path.exists() 判断是来否存在目录

# os.path.isabs() 是不是绝对路径

# os.path.isfile()  是不是文件

# os.path.isdir() 是不是文件夹

# os.path.join() 将多个路径组合返回 ，第一个绝对路径之前的参数将被忽略

# os.path.getsize()
# os.path.getatime()
# os.path.getctime()
# os.path.getmtime()