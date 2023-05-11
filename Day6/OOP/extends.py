

#class People: 经典类 写法
class People(object): #object 标准写法 新式类
    # 新式类主要影响在继承上

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


    def eat(self):
        print("eating……")

    def drink(self):
        print("drink……")
        pass

    def sleep(self):
        print("%s is sleeping……" % self.name)

class Other(object):

    # def __init__(self,name,age,gender):
    #     self.name = name
    #     self.age = age
    #     self.gender = gender

    def friedns(self,obj):
        print("%s is sleeping…… %s" % (self.name,obj.name))
    pass

class Man(People,Other): #这就是继承了People  默认从左到右的继承执行顺序

    def __init__(self,name,age,gender,money="money"):

        #第一种写法  多继承要写两个
        # People.__init__(self,name,age, gender)
        # Other.__init__(self,name,age, gender)
        #第二中写法 多继承只需要写一个
        super(Man,self).__init__(name,age,gender) #新式类写法
        # self.name = name
        # self.age = age
        # self.gender = gender
        self.money = money

    # pass
    def sleep(self):#重构了父类方法
        People.sleep(self) #必须加self 否则报错
        print("sleeping in man")


m2 = Man("a 2a",22,11)
m1 = Man("a a",2,1)

m1.friedns(m2)