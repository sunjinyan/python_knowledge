

class Dog(object):
    '''zelllll'''

    name = "ccc"

    def __init__(self,name):
        self.name = name
        self.__food = None

    def __str__(self):
        print("__str__")
        return "__str__"  #必须要有返回值
        pass

    @staticmethod
    #静态方法 只是名义上归属类管理，但实际和类没什么关系了，在静态方法里 访问不了类或实例中的任何属性

    # def eat(food):
    def eat(self,food):
        print("%s is eating %s" % (self.name,food))


    @classmethod
    #类方法 只能访问类变量 ，不能访问实例变量 如果Dog里的name属性没有定义 就算构造方法中给定了self.name,那么talk也是访问不到的
    def talk(self):
        print("ddd %s" % self.name)

    @property
    #属性方法就是把一个方法 变成一个静态属性  所以调用的话就不能使用括号来调用
    #如果有参数该怎么办？ 需要必须在下边写一个prope.setter修饰的方法来进行赋值 如下
    # def prope(self,food):
    def prope(self):
        print("%s eat dsa %s" % (self.name,self.__food))
        pass

    #给property修饰的同名属性 赋值
    @prope.setter
    def prope(self,food):
        print("%s eat dsa %s" % (self.name,food))
        self.__food = food
        pass

    #给property修饰的同名属性 在 del  d.prope时触发
    @prope.deleter
    def prope(self,food):
        del self.__food
        print("finish")
        pass

    def __call__(self, *args, **kwargs):

        print("__call__")
        pass



d  = Dog("das")

#如果是静态方法 需要传第一个对象的参数
d.eat(d,"da")
d.talk()

#TypeError: 'NoneType' object is not callable
# d.prope()  报错
d.prope
d.prope = "baozi1"  #如果是设置属性  就会调用setter 修饰的同名方法
# del  d.prope  #调用deleter
d.prope

print(d.__doc__) #打印说明文档
print(d.__module__) #打印所属模块  __main__
print(d.__class__) #打印类的本身  <class '__main__.Dog'>
#print(d.__call__) #对象后面加括号，触发执行。

# d() #调用了__call__方法

print(Dog.__dict__) #查看类中的所有成员，不包括实例属性
print(d.__dict__) #查看实例中的所有实例变量，不包括类属性

print(d) #如果一个类中定义了__str__方法，那么在打印对象时，默认输出该方法的返回值



class Foo:
    x=1
    z=1
    def __init__(self,y):
        self.y=y

    def __getattr__(self, item):
        print('----> from getattr:你找的属性不存在')


    def __setattr__(self, key, value):
        print('----> from setattr')
        # self.key=value #这就无限递归了,你好好想想
        # self.__dict__[key]=value #应该使用它

    def __delattr__(self, item):
        print('----> from delattr')
        # del self.item #无限递归了
        self.__dict__.pop(item)

#用于索引操作，如字典，下面分别表示获取、设置、删除数据
#__setattr__添加/修改属性会触发它的执行
f1=Foo(10)
print(f1.__dict__) # 因为你重写了__setattr__,凡是赋值操作都会触发它的运行,你啥都没写,就是根本没赋值,除非你直接操作属性字典,否则永远无法赋值
f1.z=3
print(f1.__dict__)

#__delattr__删除属性的时候会触发
f1.__dict__['a']=3#我们可以直接修改属性字典,来完成添加/修改属性的操作
del f1.a
print(f1.__dict__)

#__getattr__只有在使用点调用属性且属性不存在的时候才会触发
# f1.xxxxxx

