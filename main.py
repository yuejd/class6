#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world with peewee")

def main(port = 8080, ip = "127.0.0.1"):
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port, ip)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
