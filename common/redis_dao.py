import redis, json
from config import *


class redis_dao:
    '''
    这个是给项目内部逻辑判断使用的
    '''

    def __init__(self, default=None, con=REDIS_CONFIG):
        self.redis_obj = redis.Redis(**con)
        self.default = default

    def query(self, key):
        data = self.redis_obj.get(key) if self.default == None else self.redis_obj.get(f"{self.default}.{key}")
        return json.loads(data) if data else None

    def insert(self, key, value):
        self.redis_obj.set(key, value) if self.default == None else self.redis_obj.set(f"{self.default}.{key}", value)
        return

    def delete(self, key):
        result = self.redis_obj.delete(key) if self.default == None else self.redis_obj.delete(f"{self.default}.{key}")
        return result if result else None


redis_ex = redis_dao(default=REDIS_GATEWAY_PH, con=REDIS_CONFIG)


def operate_redis(args, con=REDIS_CONFIG):
    '''
    这个是给本地通过接口操作redis时使用的，请求示例：
    {
    "type":"query",
    "space": "risk-pipeline-gateway.ph",
    "key": "1be89d58485d529b2ba31a7bfe93ecef",
    "value" : "test"
    }
    '''
    redis_obj = redis.Redis(**con)
    key = f"{args.get('space')}.{args.get('key')}"

    if args.get("type") == "query":
        data = redis_obj.get(key)
        return json.loads(data) if data else None
    if args.get("type") == "delete":
        result = redis_obj.delete(key)
        return result if result else None
    if args.get("type") in ["update", "insert"]:
        redis_obj.set(key, args.get('value'))
        return
    return "type字段错误"


if __name__ == '__main__':
    arg = {
        "type": "delete",
        "space": "risk-pipeline-gateway.ph",
        "key": "1be89d58485d529b2ba31a7bfe93ecef",
    }
    redis_result = operate_redis(arg)
