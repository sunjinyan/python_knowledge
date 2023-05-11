# _*_ encoding="utf-8" _*_

# a append w write  r read  r+ 读写模式 读和追加写的模式
# w+ 写读模式 创建文件后再写也是追加写，如果原来有文件，则被覆盖
# rb 读取2进制文件  网络传输只能用2进制
# wb 写入2进制文件  网络传输只能用2进制  需要写btye
f = open("yesterday","r+",encoding="utf-8")

c = f.read() #光标最后  f.read(10)

rl = f.readline() #读取单行
rls = f.readlines() #读取多行，返回数组

count = 0
for ln in f:
    print(ln)
    count += 1
    if  count >=9 :
        break
''' low loop
for idx,li in enumerate(rls):
    print(li.strip())
'''

#获取文件指针位置
ft = f.tell()

#将光标移动到指定位置
f.seek(0)

print(f.encoding)
print(f.buffer)

# 获取文件自身的 inode 句柄编号
print(f.fileno())


f.readable()
f.writable()

#刷新缓存到磁盘
f.flush()

f.close()

#print(c)

f = open("yesterday","w",encoding="utf-8")

#截断  从0位置开始截断
f.truncate(10)

f.write("dsadsvvv") #创建一个文件 并写在一行

f.close()