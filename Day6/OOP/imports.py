
import libs

mod = __import__('lib.aa')
print(mod)

instance = getattr(mod.aa,"C")
#调用aa模块下的c 类

obj = instance()
print(obj.name)


#官方建议

import importlib
importlib.import_module('lib.aa')