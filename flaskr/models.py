from flaskr import Base
from sqlalchemy import Column,String,Integer
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    name=Column(String(50),nullable=False)
    email=Column(String(100),nullable=False,unique=True)
    address=Column(String(200),nullable=False)