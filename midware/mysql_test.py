from mysql import get_mysql_conn


db=get_mysql_conn()

cursor = db.cursor()

sql = """INSERT INTO station_table(
              injection_and_extraction_station_number,date)
              VALUES ('test','2021-11-1')"""
cursor.execute(sql)

db.commit()
