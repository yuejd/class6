#!/usr/bin/env python
#coding=utf-8

from tornado.options import define,options

define("cmd", default='runserver')

def syncdb():
    import models
    from lib.utils import find_subclasses
    mods = find_subclasses(models.BaseModel)
    for model in mods:
        if model.table_exists():
            model.drop_table()
        model.create_table()
        print 'created table:',model._meta.db_table
    with open("./qqlist") as qqlist:
        for name_qq in qqlist:
            pname, pqq = name_qq.split(',')
            #print pname, ':', pqq.strip()
            models.Person.create(name = pname, 
                                 qq = pqq.strip(),
                                 login_times = 0)

if __name__ == '__main__':
    options.parse_command_line()
    if options.cmd == 'syncdb':
        syncdb()
