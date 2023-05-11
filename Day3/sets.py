

list_1 = [1,2,3,5,2,1,6,7,6,8]

list_1 = set(list_1)

print(list_1,type(list_1))

list_2 = [22,5,8,1,2]

list_2 = set(list_2)

#求集合交集
list_1.intersection(list_2)
#求集合并集
list_1.union(list_2)
#求集合差集
list_1.difference(list_2)

#对称差集 把两个的交集去掉，留下互相都没有的
list_1.symmetric_difference(list_2)

#判断是否为子集
list_1.issubset(list_2)
list_1.issuperset(list_2)

#没有交集  返回true
list_1.isdisjoint(list_2)


# 符号 交集 并集  补集
#交集  &
print(list_1 & list_2)
#并集  |
print(list_1 | list_2)

#差集  -
print(list_1 - list_2)# in list 1  bout not in list 2

#对称差集
print(list_1 ^ list_2)



#集合的增删改查
list_1.add(999)
list_1.update([21,31,71])


#删除信息  天生就是去重的，不会出现重复
list_1.remove(999)

#x in  list_1  判断是否在里边 列表、字典、集合、字符串都用 xxx  in|not in  list、set、dict、string
print(3 in list_1)
print(3 not in list_1)

#删除任一一个元素并返回
print(list_1.pop())
#删除指定的元素  如果不存在 remove 会报错
print(list_1.remove(999))

#删掉一个元素  如果不存在 返回none 如果是remove 会报错
print(list_1.discard(999))