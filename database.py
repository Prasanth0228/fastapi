# database.py
import os

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus, quote

#MYSQL_URL = "mysql+mysqlconnector://testdbuser:MySq1DB2k22@corp.rigelsoft.com/rever"
#MYSQL_URL = "mysql+mysqlconnector://rever-user:%s@reverpro.com/rever" % quote_plus("Rever@db124")
POOL_SIZE = 20
POOL_RECYCLE = 3600
POOL_TIMEOUT = 15
MAX_OVERFLOW = 0
CONNECT_TIMEOUT = 60
#MYSQL_URL = "mysql+mysqlconnector://testdbuser:MySq1DB2k22@corp.rigelsoft.com/rever"
'''DB = {
    'drivername': 'mysql',
    'host': 'reverpro.com',
    'port': '3306',
    'username': 'rever-user',
    'password': 'Rever@db124',
    'database': 'rever'
}'''
#engine = create_engine(URL(**DB), connect_args={'charset':'utf8'},pool_size=POOL_SIZE, pool_recycle=POOL_RECYCLE,
                                            #pool_timeout=POOL_TIMEOUT, max_overflow=MAX_OVERFLOW)
Passw= 'Rever@db124'
engine = create_engine("mysql+mysqlconnector://rever-user:%s@dev.reverpro.com/OHMS" % quote(Passw),pool_size=POOL_SIZE, pool_recycle=POOL_RECYCLE,
                                            pool_timeout=POOL_TIMEOUT, max_overflow=MAX_OVERFLOW)


#engine = create_engine("mysql+mysqlconnector://rever-user:%s@reverpro.com/rever" % quote_plus("Rever@db124"),auth_plugin='mysql_native_password')
#engine = create_engine(MYSQL_URL, pool_size=POOL_SIZE, pool_recycle=POOL_RECYCLE,
                                            #pool_timeout=POOL_TIMEOUT, max_overflow=MAX_OVERFLOW)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
'''
Base = declarative_base()
POOL_SIZE = 20
POOL_RECYCLE = 3600
POOL_TIMEOUT = 15
MAX_OVERFLOW = 2
CONNECT_TIMEOUT = 60


class Database():
    def __init__(self) -> None:
        self.connection_is_active = False
        self.engine = None

    def get_db_connection(self):
        if self.connection_is_active == False:
            connect_args = {"connect_timeout": CONNECT_TIMEOUT}
            try:
                self.engine = create_engine(MYSQL_URL, pool_size=POOL_SIZE, pool_recycle=POOL_RECYCLE,
                                            pool_timeout=POOL_TIMEOUT, max_overflow=MAX_OVERFLOW,
                                            connect_args=connect_args)
                return self.engine
            except Exception as ex:
                print("Error connecting to DB : ", ex)
        return self.engine

    def get_db_session(self, engine):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            return session
        except Exception as ex:
            print("Error getting DB session : ", ex)

'''
