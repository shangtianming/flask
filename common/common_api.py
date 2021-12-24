from flask import request, Blueprint, jsonify

common = Blueprint("这里只是个描述", __name__)


@common.route('/test', methods=['post'])
def test():
    '''blueprint测试'''
    rq = request.get_json(force=True)
    return jsonify({'msg': '账号密码错误'})
