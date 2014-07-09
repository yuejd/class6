from peewee import *
from datetime import date
from config import *

database = MySQLDatabase(DB_NAME, 
        **{"passwd": DB_PASSWD, 
            "host": DB_HOST, 
            "port": DB_PORT, 
            "user": DB_USER})

class BaseModel(Model):
    class Meta:
        database = database

class Person(BaseModel):
    name = CharField()
    pnumber = CharField()
    address = CharField()
    qq = CharField()
    mdf_time = DateTimeField()
    login_times = IntegerField()

class LoginInfo(BaseModel):
    login_time = DateTimeField()
    qq = CharField()
