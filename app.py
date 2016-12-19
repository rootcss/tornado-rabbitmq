import tornado.ioloop
import tornado.web

import pika
from pika.adapters.tornado_connection import TornadoConnection

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print 'Server started @ http://localhost:8888'
    tornado.ioloop.IOLoop.current().start()