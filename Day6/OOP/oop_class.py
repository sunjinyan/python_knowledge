
class Dog:

    def __init__(self,name):
        self.name = name
    def bulk(self):
        print("hello world %s" % self.name)



d = Dog("yan").bulk()
