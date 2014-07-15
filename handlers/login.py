#!/usr/bin/env python
#coding=utf8

from models import Person, LoginInfo
from handlers.base import BaseHandler 
from datetime import datetime
import tornado.web

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html', message = None)
    def post(self):
        qq = self.get_argument("qq")
        try:
            person = Person.get(Person.qq == qq)
            self.set_secure_cookie("qq", qq, expires_days = 1)
            person.login_times += 1
            person.save()
            self.redirect("/")
        except Person.DoesNotExist:
            log = "对不起,仅幻想6班QQ群用户可以登陆"
            self.render("login.html", message = log)
        LoginInfo.create(login_time = datetime.now(), qq = qq)

class LogoutHandler(BaseHandler):
    def get(self):
        #if (self.get_argument("logout", None)):
        self.clear_cookie("qq")
        self.redirect("/")

routes = [
    (r"/login",LoginHandler),
    (r"/logout", LogoutHandler),
]

