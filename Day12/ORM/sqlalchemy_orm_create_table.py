# 除上面的创建之外，还有一种创建表的方式，虽不常用，但还是看看吧

from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper

metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('fullname', String(50)),
             Column('password', String(12))
             )


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password


mapper(User,user)
# the table metadata is created separately with the Table construct,
# then associated with the User class via the mapper() function
#事实上，我们用第一种方式创建的表就是基于第2种方式的再封装。