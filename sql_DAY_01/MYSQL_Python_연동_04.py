# 복잡한 쿼리 실행
import pymysql

conn = pymysql.connect(host='localhost', user='gmdgod123', password='1234', db='sakila', charset='utf8')

cur = conn.cursor()

query = """
select c.email
from customer as c
    inner join rental as r
    on c.customer_id = r.customer_id
where date(r.rental_date) = (%s)""" # 쿼리에 전달된 값 %s 문자열

cur.execute(query, ('2005-06-14'))
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()