import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import  Column,String,Integer
from sqlalchemy import  func

from  sqlalchemy.orm import  sessionmaker


engine = sqlalchemy.create_engine(url="mysql+pymysql://root:root@localhost/shop_user_srv",encoding='utf-8', echo=True)


Base = declarative_base()

class User(Base):
    __tablename__ = "users" # 表明

    id  = Column(Integer,primary_key=True)

    name = Column(String(32))

    password = Column(String(64))

    def __repr__(self): #格式化输出数据

        return "<%s name: %s>" %(self.id,self.name)

Base.metadata.create_all(engine) #创建表结构


# 最基本的表我们创建好了，那我们开始用orm创建一条数据试试
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例 相当于 cursor

data_first = Session.query(User).filter_by(name="alex").first()
data_all = Session.query(User).filter_by(name="alex").all()
data_filter = Session.query(User).filter(User.id >= 1).filter(User.id < 10).all()
data_in = Session.query(User).filter(User.name.in_(['ddd','alex'])).filter(User.id < 10).all()
data_like = Session.query(User).filter(User.name.like("Ra%")).filter(User.id < 10).all()
print(data_all,data_first,data_filter)
print(Session.query(func.count(User.name),User.name).group_by(User.name).all())
print(Session.query(User).filter(User.name.like("Ra%")).count())
data_first.name = 'alex'
data_first.password = 'dsadsad'


# 连表查询 join
# Session.query(User,Favor).filter(User.id == Favor.nid).all()
# Session.query(User).join(Favor).all()
# Session.query(User).join(Favor,isouter=True).all()

# Session.rollback()



Session.commit()  # 现此才统一提交，创建数据