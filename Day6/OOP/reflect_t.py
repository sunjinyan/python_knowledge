
class Cat(object):
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s is eating" % self.name)
        return True

c = Cat("ca")
choice = input(">> : ").strip()


# add = lambda x,y:x+y
# print(add(3,4))
def bulk(self):
    print("%s is aaa" % self.name)


if hasattr(c,choice):
    print(getattr(c,choice,True)())
else:
    #将用户输入 装配给类
    setattr(c, choice, bulk)

    # c.talk(c) #talk字符串 是input用户输入的

delattr(c,choice)
print(hasattr(c,choice))
exit(0)
#反射
#通过字符串映射或修改程序运行时的状态、属性、方法、有以下4个方法
#getattr(object,name,default=None)  Get a named attribute from an object
#hasattr(object,name)  判断object中有没有一个name字符串对应的方法或属性
#setattr(x,y,z) Sets the named attribute on the given object to the specified value
#delattr(x,y) Deletes the named attribute from the given object

class BlackMedium:
    feature='Ugly'
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

    def sell_house(self):
        print('%s 黑中介卖房子啦,傻逼才买呢,但是谁能证明自己不傻逼' %self.name)
    def rent_house(self):
        print('%s 黑中介租房子啦,傻逼才租呢' %self.name)

b1=BlackMedium('万成置地','回龙观天露园')

#检测是否含有某属性
print(hasattr(b1,'name'))
print(hasattr(b1,'sell_house'))

#获取属性
n=getattr(b1,'name')
print(n)
func=getattr(b1,'rent_house')
func()

# getattr(b1,'aaaaaaaa') #报错
print(getattr(b1,'aaaaaaaa','不存在啊'))

#设置属性
setattr(b1,'sb',True)
setattr(b1,'show_name',lambda self:self.name+'sb')
print(b1.__dict__)
print(b1.show_name(b1))

#删除属性
delattr(b1,'addr')
delattr(b1,'show_name')
delattr(b1,'show_name111')#不存在,则报错

print(b1.__dict__)


#类也是对象
class Foo(object):
    staticField = "old boy"

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'

    @staticmethod
    def bar():
        return 'bar'


print(getattr(Foo, 'staticField'))
print(getattr(Foo, 'func'))
print(getattr(Foo, 'bar'))


#反射当前模块成员
import sys


def s1():
    print( 's1')


def s2():
    print( 's2')


this_module = sys.modules[__name__]

hasattr(this_module, 's1')
getattr(this_module, 's2')