#pymysql.connect() 함수
# host : DB가 존재하는 서버의 주소(localhost 또는 IP주소)
# user : 사용자 ID, db : 연결할 데이터베이스 이름
# 리턴 : connection 객체
import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='gmdgod123',
                       password='1234',
                       db = 'sakila', charset='utf8')

cur = conn.cursor()
cur.execute('select * from language')
row = cur.fetchall()
print(row)

language_df = pd.DataFrame(row)
print(language_df)

cur.close()
conn.close()