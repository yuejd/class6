#!/usr/bin/env python
#coding=utf8
from handlers import admin, login

routes = []
routes.extend(admin.routes)
routes.extend(login.routes)
