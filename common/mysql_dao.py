import pymysql
from config import *


class mysql_dao:
    def __init__(self, db):
        self.db = pymysql.connect(**account, database=db)
        self.cur = self.db.cursor()

    def query(self, sql):
        self.cur.execute(sql)
        result_list = self.cur.fetchall()  # 获取查询结果
        cols = [i[0] for i in self.cur.description]  # 获取字段名
        self.db.close()
        return [{key: value for key, value in zip(cols, i)} for i in result_list] if result_list else None

    def handle(self, *sql):
        try:
            for i in sql:
                self.cur.execute(i)
            self.db.commit()
        except Exception as e:
            print(f"操作异常：{e}")
            self.db.rollback()
        finally:
            self.db.close()


# ph_sit_db库 ,在多次进行增删查改时会出问题，因为是同一个对象，事务没有改变
mysql_ph_sit = mysql_dao(ph_sit_db)

if __name__ == '__main__':
    sql = '''
    SELECT *  from phrisk_rule_cutoff_line_config where product_type = 'cf' and channels = 'iPrice Group Corporation'
    '''
    result = mysql_dao("risk_sit_ph").query(sql)
    for i in result:
        print(i)
