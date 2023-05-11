#!/usr/bin/env python

# -*- coding:utf-8 -*-

# Author: Sunjinyan

name = input("name: ")
age = int(input("age: "))
print(type(age))
# info = '''
# Name: '''+name+'''
# Age: '''+age+'''
# '''

# 格式化输出 %d %s
info1 = '''
Name: %s
Age: %d
''' %(name,age)

info2 = '''
Name: {_name}
Age: {_age}
'''.format(
    _name=name,
    _age=age
)

info3 = '''
Name: {0}
Age: {1}
'''.format(
    name,
    age
)

print(info2)