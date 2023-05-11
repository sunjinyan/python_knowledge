

#同一种接口 多种的继承形态


class Animal:

    def __init__(self,name):
        self.name = name

    def talk(self):
        print("%s is say" % self.name)
        pass
        #抛出异常
        #raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):

    def __init__(self,name):
        super().__init__(name)
        self.name = name

    # def talk(self):
    #     return "Meow"

    # @classmethod
class Dog(Animal):

    def __init__(self,name):
        super().__init__(name)
        self.name = name

    # def talk(self):
    #     return "Woof"

c = Cat("cat")
d = Dog("dog")

#一种类的形态 在继承之后 产生了多种形态
c.talk()
d.talk()