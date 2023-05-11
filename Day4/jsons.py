#!/usr/bin/env python
import json

#_*_  coding:utf-8 _*_


# info = {
#     'name':'alex',
#     'age':22
# }
#
# f = open('test.txt','w')
#
# f.write(str(info))
#
# f.close()
#
# f = open('test.txt','r')
#
# data = f.read()
#
# print(eval(data))
# f.close()


info = {
    'name':'alex',
    'age':22
}

s = json.dumps(info)

print(s,type(s))

i = json.loads(s)

print(i,type(i))