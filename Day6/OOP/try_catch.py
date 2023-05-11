
# 自定义异常
class SelfException(Exception):

    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message

class Cat(object):
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s is eating" % self.name)
        return True

c = Cat("ca")
choice = input(">> : ").strip()


def bulk(self):
    print("%s is aaa" % self.name)

#断言  作用就是在断言之后的操作必须要保证不可出错，所以在这里做断言式判断
assert type(c.name) is int

if hasattr(c,choice):
    print(getattr(c,choice,True)())
else:
    #将用户输入 装配给类
    setattr(c, choice, bulk)

    #使用异常避免报错

    try:
        raise SelfException("self Exception")
        c.talk(c)  # talk字符串 是input用户输入的
    except IndexError as e:
        print(e)
    except KeyError as e:
        print(e)
    except ValueError as e:
        print(e)
    # except Exception as e: #有了Exception 就会 提示已经有Exception  不需要在写 SelfException
    #     print(e)
    except SelfException as e:
        print(e)
    else:
        #没发生异常就执行
        pass
    finally:
        #总是执行
        pass



'''
常用异常

AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的

其他错误种类
ArithmeticError
AssertionError
AttributeError
BaseException
BufferError
BytesWarning
DeprecationWarning
EnvironmentError
EOFError
Exception
FloatingPointError
FutureWarning
GeneratorExit
ImportError
ImportWarning
IndentationError
IndexError
IOError
KeyboardInterrupt
KeyError
LookupError
MemoryError
NameError
NotImplementedError
OSError
OverflowError
PendingDeprecationWarning
ReferenceError
RuntimeError
RuntimeWarning
StandardError
StopIteration
SyntaxError
SyntaxWarning
SystemError
SystemExit
TabError
TypeError
UnboundLocalError
UnicodeDecodeError
UnicodeEncodeError
UnicodeError
UnicodeTranslateError
UnicodeWarning
UserWarning
ValueError
Warning
ZeroDivisionError
'''