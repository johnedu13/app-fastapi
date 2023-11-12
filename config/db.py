from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/userdb")

sessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

meta_data = MetaData()

Base = declarative_base()