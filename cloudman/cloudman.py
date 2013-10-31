#coding=utf8
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import settings as site_settings

class Application(tornado.web.Application):
    def __init__(self):
        handlers = site_settings.URLS
        settings = site_settings.APPLICATION_SETTINGS
        tornado.web.Application.__init__(self, handlers, **settings)
        #Global var here
        self.globalvar = 'test'

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(site_settings.PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()