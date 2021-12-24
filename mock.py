from flask import request, jsonify
from common import server, logging
from common.common_api import common

server.register_blueprint(common)


@server.route('/user/login/', methods=['post'])
def login():
    rq = request.get_json(force=True)
    logging.info(f"flask服务，请求参数是：{rq}")

    if request.method == 'POST':
        data = request.get_json()
        if data.get('username') == 'whitewall' and data.get('password') == '12356':
            return jsonify({'token': '你敢相信这是一个token？', 'msg': '登录成功'})
        else:
            return jsonify({'msg': '账号密码错误'})


if __name__ == '__main__':
    server.run(host="0.0.0.0", port=3333, debug=True)
