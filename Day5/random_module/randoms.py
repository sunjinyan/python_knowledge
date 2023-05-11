import random

# 随机小数
print(random.random())

# 可以指定区间的所及浮点数
print(random.uniform(1,10))

#随机整数  包括 0 10
print(random.randint(0,10))

#不包含5
print(random.randrange(0,5))

# 在一个序列化的数据中随机拿出一个 可以是字符串、列表
# random.choice([1,2,3])

# 随机选取指定个数的列表  也是序列类型
print(random.sample([0,1,2,3,5],3))

# 打乱顺序
item = [1,2,3]
random.shuffle(item)
print(item)