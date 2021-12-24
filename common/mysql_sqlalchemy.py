from sqlalchemy import create_engine
from config import ph_sit_db_url
from sqlalchemy.orm import sessionmaker
from sql.ph_rule_model_total_score import PHTotalScore


class DatabaseEngine:

    def __init__(self):
        # echo=True是开启调试，这样当我们执行文件的时候会提示相应的文字
        engine = create_engine(ph_sit_db_url, echo=False)
        self.conn = engine.connect()
        RiskSession = sessionmaker()
        RiskSession.configure(bind=engine)
        self.session = RiskSession()  # 创建会话实例

    def get_total_score(self, transaction_id):
        return self.session.query(PHTotalScore).filter(PHTotalScore.transaction_id == transaction_id).first()


if __name__ == '__main__':
    # result = DatabaseEngine().get_total_score("5939554322861670400")
    # print('=====', result.transaction_id)

    with DatabaseEngine() as de:
        result = de.get_total_score("5939554322861670400")
        print(result.transaction_id)
