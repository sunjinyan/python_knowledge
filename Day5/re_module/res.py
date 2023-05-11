import re

#re.match就是从开头进行匹配 不能匹配从中间开始的位置  ^没什么用

# ree = re.match("^ls\d","ls123add") 只会匹配到一个数字
# ree = re.match("^.+","ls123add") .匹配除了\n之外的任意字符  如果flags = re.DOTALL 则就是所有
ree = re.match("^ls\d+","ls123add")  #如果想匹配多个数字，则需要使用+号
print(ree.group())

#re.search 才是从整个文本中去搜索

re.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE)  #$指的是整个字符串以$之前的字符结尾
re.search("aal?","aaxsaaa",flags=re.MULTILINE)  #l 可以匹配不到  表示匹配问号之前的所有字符
re.search("[0-9]{3}","dsadas3112aa",flags=re.MULTILINE)  #匹配数字个数



# re.findall()  匹配所有符合正则表达式的结果，返回多个结果的列表
#findall没有group方法


#分组匹配 (?P<name>)  ?P 表示的是给分组定义个名字 名字就是后边<中的名字，唯一不可重复>  可以使用groupdict来获取
re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371271199206123111").groupdict("city")


# 将字符串分割成列表
# re.split("[0-9]","abc123de31DS")
re.split("[0-9]+","abc123de31DS")


# 将匹配到的字符替换成指定的字符
re.sub("[0-9]+","*","abc123de31DS",count=2)


#几种模式
#re.I(re.IGNORECASE) 忽略大小写 （括号内是完整写法，下同）
#M(MULTILINE) 多行模式，改变^ 和 $ 的行为
#S(DOTALL) 点任意匹配模式，改变"."的行为