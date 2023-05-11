import copy



'''
sys模块是内置的c的模块

浅copy  第二个内置列表是第一个内置列表的引用
联合账号的应用
'''

name = ["1","2","3"]

name.append("5")
name.insert(1,"5")
name[2] = "7"

print(name.index("5"))
print(name.count("5"))

name.remove("7")
del name[1]
name.pop(1)

name.sort()

name1 = ["7","8","9"]
name.extend(name1)
del  name1

# 1、copy确实会复制浅层的数据
# 不会完全复制一份子列表 而是都指向了指针  浅COPY 只复制第一层
# name2 = name 直接都是指向的同一内存块
name2 = name.copy()
name3 = copy.copy(name)#和上面的一样
name5 = copy.deepcopy(name)
# name.clear()
name.reverse() #反转
print(name[0:2]) #切片
print(len(name)) #元素长度
name6 = list(name)
print(name[0:-1:2])#步长 2 0 和1 可以省略
for n in name:
    print(n)