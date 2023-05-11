# 包的本质就是一个目录(必须带有一个__init__.py文件)  从逻辑上来组织模块的
# 模块的定义
# 本质就是一个python 文件
import os.path
import sys

# 模块的导入方法
# import module_name
# import module_name,module_name2
# from  module_name import *  导入的不是模块  而是模块里的所有代码  按顺序覆盖
# from  module_name import logger as log  导入的不是模块  而是模块里的所有代码  按顺序覆盖
# from  module_name import m1,m2,m3  导入的不是模块  而是模块里的所有代码  按顺序覆盖

# import本质（路径搜索和搜索路径）
# import 把module赋值给了 import的变量  是个变量
# from  是把文件里的文件 把要引入的都拿到当前位置 执行一遍
# 导入包就是在解释这个包下的__init__.py文件  如果init里有代码，就会直接执行该部分文件

'''
import  必须要找到导入文件的路径  找的时候就是路径搜索的过程  ，首先到当前路径，然后到sys.path下定义的搜索路径下去找
abs = os.path.abspath(__file__) #获取当前文件的绝对路径
dir = os.path.dirname(abs) #获取当前文件的所在目录
dirq = os.path.dirname(os.path.dirname(abs)) #获取当前文件夹的所在目录
sys.path.append(dirq)  #加到path最后 会被最后搜索，则 就会冲突
sys.path.insert(dirq)  #加到path最前边 会被第一搜索，避免冲突
improt  xxxx
'''

# 导入优化
# from  module_name import *  导入的不是模块  而是模块里的所有代码  按顺序覆盖
# from  module_name import logger as log  导入的不是模块  而是模块里的所有代码  按顺序覆盖
# from  module_name import m1,m2,m3  导入的不是模块  而是模块里的所有代码  按顺序覆盖

# 模块分类
# a.标准库
# b.开源、第三方模块
# c.自定义模块