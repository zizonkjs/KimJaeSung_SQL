'''
-분석 절차 안내-

1.데이터 수집

2.CSV 파일에서 CPI 및 GRDP 데이터를 읽어옴.
  데이터 전처리

3.NaN 값이 포함된 열을 삭제함.
  도시명을 인덱스로 변환하여 데이터베이스에 저장.
  데이터 저장 및 관리

4.MySQL 데이터베이스(product)에 연결하여 cpi_tb 테이블에 데이터 삽입.
  데이터 분석

5.CPI의 연도별 증가율을 계산.
  CPI와 GRDP의 관계를 시각화.
  데이터 시각화

6.연도별 평균 CPI 및 GRDP 변화를 선 그래프로 표현.
  CPI와 GRDP 간의 관계를 산점도로 표현.

'''

import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np
conn = pymysql.connect(host='172.20.97.217', user='member2', password='1234', db='product', charset='utf8')
cur = conn.cursor()


# CSV 파일 읽기
csv_data = pd.read_csv('Korean_CPI_by_City_2019-2023.csv')

# NaN 값이 포함된 열 삭제
csv_data.dropna(axis=1, how='all', inplace=True)


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

# 열을 리스트로 추출하기
cpi_year = list(csv_data[csv_data.columns[0]])
cpi_city = list(csv_data[csv_data.columns[1]])
cpi_data = list(csv_data[csv_data.columns[2]])
grdp_data = list(csv_data[csv_data.columns[3]])

print(cpi_data)
cpi_data_increse = []
trash=[]
for a in range(0,38):
    cpi=cpi_data[a+1]-cpi_data[a]
    if cpi < 0 :
        trash.append(round(cpi,1))
    else:
        cpi_data_increse.append(round(cpi,1))
print(cpi_data_increse)


# 고유한 도시 리스트 만들기
city_list = sorted(list(set(cpi_city)))

# 8개 도시를 평균화 시켜서 하나의 선그래프로 만들기
avg_cpi_by_year = csv_data.groupby(csv_data.columns[0])[csv_data.columns[2]].mean()

plt.figure(figsize=(14, 8))
plt.plot(avg_cpi_by_year.index, avg_cpi_by_year.values, marker='o', label='Average CPI')

plt.title('각년도 8개 도시 CPI지수 평균화')
plt.xlabel('Year')
plt.ylabel('CPI')
plt.legend(title='CPI 평균')
plt.grid(True)
plt.show()

# 각 도시의 연도별 지역내총생산(GRDP) 그래프 그리기
# 각 도시 지역내총생산 평균화 시키기
avg_grdp_by_year = csv_data.groupby(csv_data.columns[0])[csv_data.columns[3]].mean()

# 평균화한 GRDP를 그래프로 그리기
plt.figure(figsize=(14, 8))
plt.plot(avg_grdp_by_year.index, avg_grdp_by_year.values, marker='o', label='Average GRDP')

plt.title('각년도 8개 도시 GRDP평균화')
plt.xlabel('Year')
plt.ylabel('GRDP%')
plt.legend(title='GRDP 평균화')
plt.grid(True)
plt.show()

# dict로 변환
data = {
    'Year': cpi_year,
    'City': cpi_city,
    'CPI': cpi_data,
    'GRDP': grdp_data
}

df = pd.DataFrame(data)

# 산점도 그리기
plt.figure(figsize=(10, 6))
plt.scatter(df['CPI'], df['GRDP'], alpha=0.7, c='blue')
plt.title('CPI와 GRDP의 상관관계')
plt.xlabel('CPI (소비자물가지수)')
plt.ylabel('GRDP (지역총생산량)')
plt.grid(True)
plt.show()


