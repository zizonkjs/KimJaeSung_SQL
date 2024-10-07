# Dictcursor 사용
import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='gmdgod123', password='1234', db='sakila', charset='utf8')

cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select * from language')
rows = cur.fetchall()

language_df = pd.DataFrame(rows)
print(language_df)

print()

print(language_df['name'])
cur.close()
conn.close()

