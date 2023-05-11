
class Role(object):
    n = 1 #类变量
    #构造函数  只能通过init 方法传参
    def __init__(self,name,role,weapon,life_val=100,money=100):
        self.name=name # 实例变量 静态属性 作用域就是实例本身
        self.role=role
        self.weapon=weapon
        self.__life_val=life_val #加两个下滑线  表示私有属性 外部访问不到
        self.money=money


    def buy_gun(self): # 类的方法 功能 动态属性
        print("buy one gun")

    def shut(self):
        print("shut one gun %s" % self.name)

    def __del__(self):
        print("finished")

r1 = Role("name","police","AK47") #实例化对象

r1.name = "dsadsadsa"

r1.shut()
print(r1.n)