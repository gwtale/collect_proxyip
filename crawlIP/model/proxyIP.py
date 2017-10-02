from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
BASE = declarative_base()
class proxyIP(BASE):
    __tablename__ = 'proxyIP'
    id = Column(Integer, primary_key=True)
    ip = Column(String(20))
    port = Column(String(10))
    high_hide = Column(String(10))
    type = Column(String(10))



