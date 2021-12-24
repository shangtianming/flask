import flask
import logging

# 创建接口后台服务
server = flask.Flask(__name__)
# 设置日志级别
logging.basicConfig(level=logging.INFO)
