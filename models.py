#!/usr/bin/env python
#coding=utf-8

from peewee import *
from config import *

database = MySQLDatabase(DB_NAME, 
        **{"passwd": DB_PASSWD, 
            "host": DB_HOST, 
            "port": DB_PORT, 
            "user": DB_USER,
            "charset": "utf8"})

class BaseModel(Model):
    class Meta:
        database = database

class Person(BaseModel):
    name = CharField(max_length=40)
    qq = CharField()
    pnumber = CharField(null=True)
    address = TextField(null=True)
    others = TextField(null=True)
    mdf_time = DateTimeField(null=True)
    login_times = IntegerField(null=True)

class LoginInfo(BaseModel):
    login_time = DateTimeField()
    qq = CharField()
