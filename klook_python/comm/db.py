import pymysql
from conf.read_conf import conf_Data


class MySqlCon:
    def __init__(self, dbname, sql):
        self.dbname = dbname
        self.sql = sql

    def mysql_con(self) -> iter:
        try:
            database = pymysql.connect(
                        host=conf_Data.db_info("db", "db_host"),
                        user=conf_Data.db_info("db", "db_user"),
                        password=conf_Data.db_info("db", "db_password"),
                        port=int(conf_Data.db_info("db", "db_port")),
                        db=self.dbname)
            cur = database.cursor()
            cur.execute(self.sql)
            data = cur.fetchall()
            cur.close()
            database.close()
            yield data
        except Exception as e:
            print("数据库连接异常: {}, 请检查".format(e))


