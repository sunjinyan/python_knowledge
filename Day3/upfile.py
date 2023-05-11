
# ascii 占8位  Unicode 2个字节 16位   utf-8 变长  中文3个字节  数字 英文占1个字节8位
# 也就是说所有的字符集之间的转换都要经过 与unicode 字符集的相互转换后才能转换成对应的字符集数据
# s.encode("gbk")
# utf8  decode-> unicode    gbk  decode-> unicode
# unicode encode-> utf8     unicode encode-> gbk


f1 = open("yesterday.txt","r",encoding="utf-8")
f2 = open("yesterday","w",encoding="utf-8")

for line in f1:

    if "aa" in line:
        line =  line.replace("old","new")
    f2.write(line)

f1.close()
f2.close()


#可以自动关闭文件，不用怕忘记 close
with open("yesterday.txt","r",encoding="utf-8") as f3,open("yesterday","w",encoding="utf-8") as f5:
    for ln in f3:
        print(ln)