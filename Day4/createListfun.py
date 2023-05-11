

#生成器  列表生成器

#通过列表生成式，我们可以直接创建一个列表，但是收到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间
#如果我们只是需要访问前面几个元素，那后面绝大多数元素占用的空间就浪费了
#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断的推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间，
#python中，这种一边循环一边计算的机制，成为生成器：generator
#要创建一个generator 有很多方法，第一种方法很简单，只是把list的生成式[]改成(),就创建了一个generator

#列表是直接生成
L = [x * x for x in range(0,10)]
print(L)

#不生成 如果访问了才进行创建  只能一个一个的去访问
g = (i*2 for i in range(10))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
print(g)


#用函数操作

#生成器的应用场景  以及使用方式

#斐波那契  生成器
def  fib(max):
    n,a,b=0,0,1
    try:
        while n < max:
            # print(b)
            yield b #想把什么返回到外边，就在那个前面加 yield
            a, b = b, a + b
            n = n + 1
    except StopIteration as  e:
        print(e.value)

    # 如果有yield 那么这个就不是函数，就是生成器了，那么return 的就是try抛出的异常 而不是返回值
    return 'done'
fb = fib(10)
print(fb.__next__())
print(fb.__next__())
print(fb.__next__())