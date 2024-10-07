import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
conn = pymysql.connect(host='172.20.97.217', user='member2', password='1234', db='product', charset='utf8')
cur = conn.cursor()


# CSV 파일 읽기
csv_data = pd.read_csv('Korean_CPI_by_City_2019-2023.csv')

# NaN 값이 포함된 열 삭제
csv_data.dropna(axis=1, how='all', inplace=True)

# 2023년의 GRDP 값이 0인 행 삭제
csv_data = csv_data[~((csv_data['Year'] == 2023) & (csv_data['GRDP'] == 0))]

print(csv_data)

# 데이터 추출
cpi_year = list(csv_data[csv_data.columns[0]])
cpi_city = list(csv_data[csv_data.columns[1]])
cpi_city_r = []
cpi_data = list(csv_data[csv_data.columns[2]])
grdp_data = list(csv_data[csv_data.columns[3]])
city_list = ['Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', 'Daejeon', 'Ulsan', 'Sejong']

for ci in cpi_city:
    cpi_city_r.append((city_list.index(ci) + 1))

for i in range(len(cpi_city_r)):
    sql = 'insert into cpi_tb(city_id, data, GRDP, year) values(%s, %s, %s, %s)'
    cur.execute(sql, (cpi_city_r[i], cpi_data[i], grdp_data[i], cpi_year[i]))

conn.commit()
cur.close()
conn.close()

# # 열을 리스트로 추출하기
cpi_year = list(csv_data[csv_data.columns[0]])
cpi_city = list(csv_data[csv_data.columns[1]])
cpi_data = list(csv_data[csv_data.columns[2]])
grdp_data = list(csv_data[csv_data.columns[3]])

for a in cpi_data:
    

