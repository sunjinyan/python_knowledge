
#必须都为真才返回真非0就是真
print(all([0,-5,3]))

#有一个为真就返回真
print(any([0,-5,3]))


print(ascii(['卡','了']))

#将一个int转换成字节
bin(2)

#判断是否为真
bool(0)#[1,2]

#转换成字节
a = bytes("abcd","utf-8")
print(a)
b = bytearray("abcd","utf-8")
print(b[0])

# 数字转换成asicc
print(chr(97))
# asicc转换成数字
print(ord('b'))

# 编译用的
code = '''
def a():
    time.sleep(3)
    print("in the a")
    return "999"
'''
# py_obj =   compile(code,"err.log","exec")
#
# print(py_obj)

divmod(5,2)
#(2,1)2商 1是余数

# 把字符串变成字典
# eval()

#
#
#
#
#
#
#

#匿名函数
def sayhi(n):
    for i in range(5):
        if n == i :
            print(i)
sayhi(3)

calc = lambda n:sayhi(n)
calc(5)
# filter
# 按条件过滤  range列表里  只打印匿名函数中定义的大于5的
res = filter(lambda n:n>5,range(10))

# array_map
rea = map(lambda n:n*n,range(10))

re = [lambda i:i*2  for i in range(10)]

import functools
# 将结果付给x 累加  如果把 x+y 换成 x*y 就是阶乘
rf = functools.reduce(lambda x,y:x+y ,range(10))


a = set([1,2,3,9,1,55,15,3,6])
# a.add() a.pop

# 不能被修改  不可变集合 不可变列表
b = frozenset([1,2,3,9,1,55,15,3,6])

# 返回当前所运行的程序里所有变量的集合 这个文件额  返回的是一个字典
# globals()




# 散列

hash("ddd")

# 把数字转成16进制
hex(8)

# 返回内存地址

# id()

# 获取用户输入
# input()

# isinstance()

# issubclass() 是不是子类

# iter把列表、字典、集合变成迭代器
# print(iter([1,2,3,5,7]))

# 长度
# len()

# 获取局部的变量
# locals()
# array_map功能
# map
# 最大\小值
# print(max([1,2,3,51,7]))
# print(min([1,2,3,51,7]))


# 相当于迭代器的 __next()__
# next()

# 把数字变为八进制
# oct(5)

# 打开文件
# open()

# 返回 unicode对应的地址
# ord("c")

# 返回3 的5次方
pow(3,5)

# range(1,10,2) 从 1 开始生成列表到10  步长为2


#用字符串表示一个对象  也不能使用eval 或exec 转会代码
# repr()

# 反转
# reversed()


# 保留小数几位
# round(1.23333,2)

#集合
# set()


# b = [1,2,3,4,5,6]
# b[slice(2,3)]


# sorted
# a = sorted(b.items(),key = lambda x:x[1])
# a = sorted(b)

# 列表求和
# sum()

# 面向对象继承
# super()

# 所有数据类型的根
# type()

#返回对象的所有属性名
# vars()

a  = [1,2,3,5]
b  = ['a','b','c','d']
# 拉链
# zip(a,b)

# 
# __import__()