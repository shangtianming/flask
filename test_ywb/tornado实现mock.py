import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    '''http服务端'''

    def get(self):
        '''get请求'''
        a = self.get_argument('a')
        self.write({'我有这么多钱': int(a)})

    def post(self):
        '''post请求'''
        h = self.request.headers
        u = self.request.uri
        b = self.request.body
        print("h", h)
        print("u", u)
        print("b", b)

        # 下面2行代码是设置返回的信息，目前没有想到使用场景
        # self.set_header('Content-Type', 'application/json; charset=UTF-8;')
        # self.set_status(200, '失败')

        self.write("返回的内容")

if __name__ == '__main__':
    application = tornado.web.Application([('/', MainHandler)])
    # 默认host: 127.0.0.1
    application.listen(address="127.0.0.2", port=8866)
    tornado.ioloop.IOLoop.instance().start()

    #和上面启动方式不同的地方就多了参数：decompress_request=True
    #在有这个配置项的时候，如果post请求的报文头部有说明编码方式是 gzip时，tornado将会对这个请求进行解压操作
    # http_server = tornado.httpserver.HTTPServer(application, decompress_request=True)
    # http_server.listen(8866)
    # tornado.ioloop.IOLoop.instance().start()