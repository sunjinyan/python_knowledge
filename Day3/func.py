#面向对象   class
#面向过程   def
#函数式编成  def
import time


def test(x):
    '''
    this is a test func
    '''
    x += 1
    return x

time_format = "%Y-%m-%d %X"
time_cur =time.strftime(time_format)
print(test(5))


def test1(): #返回0
    print("in the test1")
    return 0

def test2(): #返回None
    print("in the test2")

def test3(): #返回元组
    print("in the test2")
    return 0,"hello",["d","v"],{"ads":"qwa"}

print(test1())
print(test2())
print(test3())