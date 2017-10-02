from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crawlIP.model.proxyIP import BASE

ENGINE = create_engine('mysql://root:zhonghao1025@localhost:3306/test?charset=utf8',
                           convert_unicode=True)
Session = sessionmaker(bind=ENGINE, autocommit=False, autoflush=False)

BASE.metadata.create_all(ENGINE)