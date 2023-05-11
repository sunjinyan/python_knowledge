
import getpass

_name = "boy"
_pwd  = "aaa"

name = input("name: ")
pwd  = getpass.getpass("pwd: ")

# 强制缩进  避免了结束符
if  _name == name and _pwd == pwd:
    print("Welcome user {__name} login...".format(__name=name))
else:
    print("{__name} logout...".format(__name=name))

if  pwd == "111" :
    print("111")
elif pwd == "333" :
    print("333")
else:
    print("666")
    
print(name,pwd)