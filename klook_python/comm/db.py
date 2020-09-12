import pymysql
from sshtunnel import SSHTunnelForwarder


class MySqlCon:

    def __init__(self, dbname, sql_contxt):
        self.dbname = dbname
        self.sql_contxt = sql_contxt

    def ssh_conn(self):
        server = SSHTunnelForwarder(
            ("xxxx", "xxxx"),
            ssh_username="",
            ssh_pkey="",
            remote_bind_address="")
        server.start()

        dbcon = pymysql.connect(
            host="127.0.0.1",
            port=server.local_bind_port,
            username="",
            password="",
            db=self.dename
        )
        cur = dbcon.cursor()
        try:
            cur.execute(self.sql_contxt)
            data = cur.fetchall()
            cur.close()
            dbcon.cursor()
            server.close()
            return data
        except Exception as e:
            print("db connect error...{}".format(e))

