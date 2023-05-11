
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterable))  # Iterable 可迭代
print(isinstance({},Iterable))
print(isinstance((),Iterable))

#凡是可以作用于for循环的对象是iterable类型
#凡是可作用于next()函数的对象都是iterator类型，他们表示一个惰性计算的序列，惰性计算就是用的时候才会去计算
#集合数据类型如list dict str 等是Iterable 但不是Iterator ,不过可以通过iter函数来获得一个Iterator对象
#range就似乎迭代器   for循环其实也是在不断调用next的迭代器
isinstance(iter([]),Iterator)
it  = iter([1,2,3,4,5])

while True:
    try:
        x = next(it)
    except StopIteration as e:
        print(e.value)

        break