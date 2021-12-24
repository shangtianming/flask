import pymongo
from config import MONGO_URL, MONGO_EXTERNAL_API_RESULT


class mongo_dao:
    '''
    这个是给项目内部逻辑判断使用的
    '''

    def __init__(self, database, url):
        myclient = pymongo.MongoClient(url, connect=False)
        db = myclient[database.get("space")]
        self.col = db[database.get("db")]

    def query(self, args):
        result = list(self.col.find(args).sort("created_at", -1))
        return result if len(result) > 0 else False

    def query_latest(self, args):
        mongo_result = self.query(args)
        return mongo_result[0] if mongo_result else {}

    def insert(self, args):
        result = self.col.insert_many(args)
        return result.inserted_ids

    def delete(self, args):
        result = self.col.delete_many(args)
        return result.deleted_count

    def update(self, args, update):
        result = self.col.update_many(args, update)
        return result.modified_count


# 第三方接口数据 {"space": "ph_risk_pipeline_gateway", "db": "external_api_result"}
mongo_ex = mongo_dao(database=MONGO_EXTERNAL_API_RESULT, url=MONGO_URL)


def operate_mongo(args, url=MONGO_URL):
    '''
    这个是给本地通过接口操作mongo时使用的，请求示例
    {
    "type":"query",
    "space": "ph_risk_pipeline_gateway",
    "db": "external_api_result",
    "data": {"id_account": 26280},
    "updata": {"id_account": 26281}
    }
    '''
    myclient = pymongo.MongoClient(url, connect=False)
    mydb = myclient[args.get("space")]
    mycol = mydb[args.get("db")]
    if args.get("type") == "query":
        result = list(mycol.find(args.get("data")).sort("created_at", -1))
        data = []
        for r in result:
            r.pop('_id')
            data.append(r)
        return result if len(data) > 0 else False
    if args.get("type") == "insert":
        result = mycol.insert_many(args.get("data"))
        return result.inserted_ids
    if args.get("type") == "delete":
        result = mycol.delete_many(args.get("data"))
        return result.deleted_count
    if args.get("type") == "update":
        result = mycol.update_many(args.get("data"), args.get("updata"))
        return result.modified_count
    return "type字段错误"


if __name__ == '__main__':
    # 注释的这个调不通，没有权限，只能在服务器上调试
    # url = "mongodb://root:Oriente2020@dds-gs5676c1c68d03c41.mongodb.singapore.rds.aliyuncs.com:3717,dds-gs5676c1c68d03c42.mongodb.singapore.rds.aliyuncs.com:3717/admin?replicaSet=mgset-300545039"
    url = 'mongodb://root:oriente2019@10.112.1.64:30100/'
    data = {
        "type": "query",
        "space": "ph_risk_pipeline_gateway",
        "db": "external_api_result",
        "key": {
            "id_account": 26280
        }
    }
    re = operate_mongo(data, url)
    print(list(re))
    for i in re:
        print(i)
