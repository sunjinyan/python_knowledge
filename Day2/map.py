#!/usr/bin/env Python
#_*_ coding:utf-8 _*_


info = {
    'stu001':"a",
    'stu002':"b",
    'stu003':"v",
}

#无序的 通过key
info["stu001"]="122"

#删除列表、字典的数据
del info["stu001"]
info.pop("stu002")
info.popitem() #随即删除
info.get("stu001") #获取指定key  也可以用来作为判断条件
print(info)

#判断是不是在一个字典里的另一个判断方式
print("stu001" in info)

#打印所有值

print(info.values())
print(info.keys())

#先取ddd  取到了把值返回 取不到设置默认值vvv
print(info.setdefault("ddd","vvv"))

#合并两个数组，存在 覆盖前面的，不存在就新增
print(info.update({"vvv":"das","stu001":"dasd"}))

#把字段按照[key,val]的形式变成数组
info.items()

#通过一个列表 初始化一个字典，并付初始值  如果是多层关系的初始值，则会出现浅copy的问题
c = dict.fromkeys([7,8,9],"ddd") # ddd 或 [1,{"cxz":"dsa"}]
print(c)

#元组
a = ("d","c")

#高效  通过索引的形式去遍历
for i in info:
    print(i,info[i])
#相对上边的低效，因为需要转换成列表（里边是元组）有开销
for k,v in info.items():
    print(k,v)