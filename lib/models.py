from sqlalchemy import Column, String, Integer
from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base
metadata=MetaData()
Base=declarative_base(metadata=metadata)

class Converter(Base):
  __tablename__="converter"
  id = Column(Integer, primary_key = True)
  sentence=Column(String, nullable=False)
  

class Encripted(Base):
  __tablename__="encripted"
  id = Column(Integer, primary_key = True)
  encript=Column(String, nullable = False)
  key = Column(String, nullable=False)
  
  
class Keys(Base):
  __tablename__="keys"
  id = Column(Integer, primary_key = True)
  keys=Column(String, nullable = False)
  
  