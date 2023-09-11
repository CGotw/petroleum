import pymysql

MYSQL_CONN = None


def get_mysql_conn():
    global MYSQL_CONN
    if MYSQL_CONN is None:
        MYSQL_CONN = pymysql.connect(
            host='localhost',
            port=3306,
            database='petroleum',
            charset='utf8',
            user='root',
            password='123456'
        )
    return MYSQL_CONN

