import shelve

# shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，可读可写;key必须为字符串，而值可以是python所支持的数据类型



f=shelve.open(r'sheve.txt')
# 存储
# f['stu1_info']={'name':'egon','age':18,'hobby':['piao','smoking','drinking']}
# f['stu2_info']={'name':'gangdan','age':53}
# f['school_info']={'website':'http://www.pypy.org','city':'beijing'}

print(f['stu1_info']['hobby'])
f.close()


f=shelve.open(r'sheve.txt')

# 获取
# f.get("name")

f.close()
