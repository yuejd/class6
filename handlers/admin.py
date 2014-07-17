#!/usr/bin/env python
#coding=utf8

from models import Person, LoginInfo
from handlers.base import BaseHandler
import tornado.web
from datetime import datetime

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        current_qq = self.current_user
        self.render('index.html', 
                    qq = current_qq,
                    persons = Person.select())
        LoginInfo.create(login_time = datetime.now(), qq = current_qq)

class EditHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('edit.html', 
                    person = Person.get(Person.qq == self.current_user))
    def post(self):
        person = Person.get(Person.qq == self.current_user)
        person.pnumber = self.get_argument("mobile")
        person.address = self.get_argument("address")
        person.others = self.get_argument("others")
        person.mdf_time = datetime.now()
        person.save()
        self.redirect("/")
        
routes = [
    (r"/", IndexHandler),
    (r"/edit", EditHandler),
]
