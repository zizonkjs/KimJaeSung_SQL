import pymysql
import pandas as pd
import csv

conn = pymysql.connect(host='localhost', user='gmdgod123', password='1234',
                       db='sakila', charset='utf8')
# my sql에 sakila 데이터베이스에 연결

cur = conn.cursor()
cur.execute('select * from language')

desc = cur.description 
for i in range(len(desc)):
    print(desc[i][0], end=' ')
print()

rows = cur.fetchall() # 모든 데이터 가져오기
for data in rows:
    print(data)
print()

cur.close()
conn.close()

