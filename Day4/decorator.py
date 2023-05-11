import time




'''
装饰器：
定义：本质是函数,目的是装饰其他函数,就是说为其他函数添加附加功能

原则：
1、不能修改被装饰的函数的源代码
2、不能修改被装饰的函数的调用方式
3、装饰器对装饰器透明

实现装饰器知识储备：
1、函数即变量  函数可以声明在内存中并将内存地址赋值给 变量
2、高阶函数  
   a、把一个函数名当作实参 传给另外一个函数  
   b、返回值中包含函数名 
3、嵌套函数
'''
'''
def timmer(func): #装饰器模式
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return warpper



@timmer
def test1():
    time.sleep(3)
    print("in the test1")

test1()
'''
def bar():
    print("in the bar")

def test2(func):
    #func()
    # print(func())
    return func
bar = test2(bar) #bar 就是一个内存地址 门牌号


#函数 bar的调用方式在test2的装饰后 没有改变
bar()



##############

def timer(auth_type):
    def aouter_wrapper(func):
        def deco(*args,**kwargs):
            print(args,kwargs)
            if auth_type == "local":
                start_time = time.time()
                res = func(*args,**kwargs)
                end_time = time.time()
                print("the func run time is %s - %s" % (end_time - start_time,0))
                return  res
            elif auth_type == "ldap":
                return ""
        return  deco
    return aouter_wrapper()
@timer(auth_type="ldap")   #相当于a = timer(a)
def a():
    time.sleep(3)
    print("in the a")
    return "999"

@timer(auth_type="local")
def b(arg):
    time.sleep(3)
    print("in the b",arg)

print(a())
print(b("ddd"))