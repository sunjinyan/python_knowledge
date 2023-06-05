import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import  Column,String,Integer

from  sqlalchemy.orm import  sessionmaker


engine = sqlalchemy.create_engine(url="mysql+pymysql://root:root@localhost/shop_user_srv",encoding='utf-8', echo=True)


Base = declarative_base()

class User(Base):
    __tablename__ = "users" # 表明

    id  = Column(Integer,primary_key=True)

    name = Column(String(32))

    password = Column(String(64))


Base.metadata.create_all(engine) #创建表结构


# 最基本的表我们创建好了，那我们开始用orm创建一条数据试试
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例 相当于 cursor

user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None

Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
print(user_obj.name, user_obj.id)  # 此时也依然还没创建

Session.commit()  # 现此才统一提交，创建数据