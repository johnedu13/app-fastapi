from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data
from config.db2 import Base

users = Table("users", meta_data,
              Column("id", Integer, primary_key=True), 
              Column("name", String(255), nullable=False),
              Column("username", String(255), nullable=False),
              Column("password", String(255), nullable=False))

meta_data.create_all(engine)

class Usuario(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))
    username = Column(String(20))
    password = Column(String(255))