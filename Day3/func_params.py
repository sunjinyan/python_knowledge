

def test(x,y): #不是位置关系
    print(x,y)

def default_param(x,y=1):
    print(x,y)
    pass
test(1,y=2)#不明确写形参的时候需要按照位置参数来给定

default_param(1)

def params(*args): #不定长参数
    print(args)
    pass
params(*[1,2,3,5,6]) #被变成tuple 元组
params(1,2,3,5,6)#被变成tuple 元组

# **kwargs
def kwargsp(**kwargs):
    print(kwargs)
#global 修改作用域  字符串、数字不能在局部内修改需要使用global 实现声明，列表、字典、集合是可以的
kwargsp(name="aaa",age=111)
kwargsp(**{"name":"aaa","age":111})