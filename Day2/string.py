


name="my \tname is alex"

#首字母大写
print(name.capitalize())

# count  出现次数
print(name.count("a"))

#center 把内容放中间，使用给定字母充填其余部分
print(name.center(50,"-"))

# endswith 判断是否以某一个字符结尾
print(name.endswith("ex"))


# expandtabs 把字符串里的tab  转换成多少个空格
print(name.expandtabs(tabsize=30))

# find 查找字符的子字符首次出现的位置
print(name.find("name"))
# print(name.format("name"))

# name.format_map({"name":"ddd","ddd":"mmm"})

print(name.index("a"))

# 阿拉伯数字+阿拉伯字符
print(name.isalnum())
# 是否为数字
print(name.isdigit())
# 纯英文字符  大小
print(name.isalpha())
# 浮点
print(name.isdecimal())

# 是不是合法标识符
print(name.isidentifier())

# 是否小写
print(name.islower())

# 是否是整数
print(name.isnumeric())
# 是否是空格
print(name.isspace())
# 是否每个字母都大写
print(name.istitle())
#是否是可以打印 除了tty设备文件
print(name.isprintable())

# 是否大写
print(name.isupper())

#数组变成字符串  数字在3中不能被join
print(' '.join(['1','2','3']))

# 保证长50 不足的用后边的补充
print(name.ljust(50,"*"))
# 保证长50 不足的用后边的补充
print(name.rjust(50,"*"))

#把大写变成小写
print(name.lower())
print(name.upper())

#去掉空行等字符
print(name.lstrip())
print(name.rstrip())
print(name.strip())

#maketrans
p = name.maketrans('abcdef','123456') #a=1 b=2 c=3 d=4 e=5 f=6 必须保证数据一样多
print('alix li'.translate(p)) #1l5x li 用上边的与该字符里的数字做对应转换

#把 a 替换成 b
print(name.replace('a','b',1))

#r find 找到最右边的下标返回
print(name.rfind('l'))

#按照给定的分隔符 变数组 默认空格
name.split(' ')

#按换行来分数组 linux和win不一样 \n  \r\n
name.splitlines()

#大写变小写 小写变大写
name.swapcase()

#自动补位
name.zfill(50)