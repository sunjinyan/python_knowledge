
#__new__\__metaclass__ 讲解

class MyType(type):

    def __init__(self, what,bases=None,dict=None):
        print("--MyType init--")
        super(MyType,self).__init__(what,bases,dict)

    def __call__(self, *args, **kwargs):
        print("--MyType call--")
        # obj = self.__new__(self,*args, **kwargs)
        obj = self.__new__(*args, **kwargs)
        self.__init__(obj,*args, **kwargs)
class Foo(object):
    __metaclass__ = MyType

    def __init__(self,name):
        self.name=name

    def __new__(cls, *args, **kwargs):
        print("Foo __new__")
        #new 方法 是类自带的方法 要在init之前执行  也就是说实例化的时候 首先是new方法被调用，然后new出发了init
        #用来创建实例的作用
        #既然重构了new方法就代表需要重构实例了
        #那么需要哪些步骤呢？又不知道
        #所以需要继承父类的，如何继承父类？那么可以使用super
        #但是super是为了在继承之后 在后面还干其他的，所以就使用基类的new 并把自身传给，因为还没有实例化，所以还没有init方法中的self
        #就是把类Foo(本身也是个对象) 作为对象传递给基类的new去创建对象 cls 就相当于init的self，也就是Foo本身
        return  object.__new__(cls) #这句话的意思就是 去继承基类的new方法 不然没办法实例化

f=Foo("all")

print(type(f))
print(type(Foo))


#把他装配到一个类中
def func(self):
    print('hello aald')

def __init__(self,name):
    self.name = name
    print('hello aald')

#类是由type类实例化产生的
Fooo = type('Foo',(),{'func':func,'__init__':__init__})

#__metaclass__ 表示该类由谁来实例化创建，所以我们可以为__metaclass__设置一个type 类的派生类
