from common.mongo_dao import operate_mongo
from common.redis_dao import operate_redis
from flask import request, Blueprint

common = Blueprint("这里只是个描述", __name__)


@common.route('/mongo', methods=['post'])
def mongo_op():
    """请求示例
    {
    "type":"query",
    "space": "ph_risk_pipeline_gateway",
    "db": "external_api_result",
    "data": {"id_account": 26280},
    "updata": {"id_account": 26281}
    }
    """
    rq = request.get_json(force=True)
    return {"result": operate_mongo(rq)}


@common.route('/redis', methods=['post'])
def redis_op():
    """请求示例
    {
    "type":"query",
    "space": "risk-pipeline-gateway.ph",
    "key": "1be89d58485d529b2ba31a7bfe93ecef",
    "value" : "test"
    }
    """
    rq = request.get_json(force=True)
    return {"result": operate_redis(rq)}
