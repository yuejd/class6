#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.web
import os

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            blog_title = u"Class 6",
            template_path = os.path.join(os.path.dirname(__file__), "templates"),  
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            #ui_modules = {"Entry1": EntryModule, "topx": TopXModule},
            xsrf_cookies = True,
            cookie_secret = "5ACGQhYDRrKEma881Gj9F5h+FOU5dU2sslE9sVSX/0g=",
            debug = True,
            login_url = "/login"
        )
        from urls import routes as handlers
        tornado.web.Application.__init__(self, handlers, **settings)

def main(port = 8080, ip = "127.0.0.1"):
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(port, ip)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
