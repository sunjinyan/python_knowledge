

import  os


os.system("dir") #成功返回0 失败返回1
res = os.popen("dir").read() #返回执行结果

os.mkdir("new")

#pyc complied的缩写

#PyCodeObject和pyc文件
'''
简述Python的运行过程

在说这个问题之前，我们先来说两个概念，PyCodeObject和pyc文件。

我们在硬盘上看到的pyc自然不必多说，而其实PyCodeObject则是Python编译器真正编译成的结果。我们先简单知道就可以了，继续向下看。

当python程序运行时，编译的结果则是保存在位于内存中的PyCodeObject中，当Python程序运行结束时，Python解释器则将PyCodeObject写回到pyc文件中。

当python程序第二次运行时，首先程序会在硬盘中寻找pyc文件，如果找到，则直接载入，否则就重复上面的过程。

所以我们应该这样来定位PyCodeObject和pyc文件，我们说pyc文件其实是PyCodeObject的一种持久化保存方式。

如果py文件有改动，源代码会从时间上判断pyc的时间是否落后py文件
'''