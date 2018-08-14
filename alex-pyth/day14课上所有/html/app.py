# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print('111')
        u = self.get_argument('user')
        m = self.get_argument('mail')
        p = self.get_argument('pwd')
        if u == 'gsy' and p == '123' and m == '123@qq.com':
            self.write('登陆OK')
        else:
            self.write("滚")

    def post(self, *args, **kwargs):
        print('333')
        u = self.get_argument('user')
        m = self.get_argument('mail')
        p = self.get_argument('pwd')
        if u == 'gsy' and p == '123' and m == '123@qq.com':
            self.write('登陆OK')
        else:
            self.write("滚")

application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()