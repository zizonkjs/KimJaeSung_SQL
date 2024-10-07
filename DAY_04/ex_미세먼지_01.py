# 미세먼지 데이터 확인
#----------------------------------------------------------------

import pandas as pd
from tabulate import tabulate

dust = pd.read_excel('dust.xlsx')

print(dust.head())
print(tabulate(dust.head(), headers='key', tablefmt='pretty'))
#----------------------------------------------------------------

# 미세먼지 데이터 구조 확인
print(dust.info())

#----------------------------------------------------------------

# 미세먼지 데이터 가공 : 컬럼이름 변경
# 한글 컬럼명을 영문으로 변경
# rename() 사용
dust.rename(columns={'날짜': 'date', '아황산가스':'so2', '일산화탄소':'co', 
                     '오존':'o3', '이산화질소':'no2'}, inplace=True)

print(tabulate(dust.head(), headers='keys', tablefmt='psql'))

#----------------------------------------------------------------

# 날짜 데이터 변경
# 기존 데이터 : '년도-월-일 시간'-> 변경 : '년도-월-일'만 추출
dust['date'] = dust['date'].str[:10]
print(tabulate(dust.head(), headers='keys', tablefmt='psql'))

#----------------------------------------------------------------

# ['date'] 자료형 변경
# object -> datetime타입
dust['date'] = pd.to_datetime(dust['date'])
print(dust.dtypes)

#----------------------------------------------------------------

#컬럼순서변경
# date 컬럼에서 년도, 월, 일을 추출하여 새로운 컬럼 생성
dust['year'] = dust['date'].dt.year
dust['month'] = dust['date'].dt.month
dust['day'] = dust['date'].dt.day
print(dust.columns)

# 컬럼순서재정렬
dust = dust[['date','year','month','day','so2','co','o3','no2',
             'PM10','PM2.5']]
print(dust.columns)

#----------------------------------------------------------------

# 결측치 확인
print(' ---결측치 개수 확인하기--- ')
print(dust.isna().sum()) # isnull() 동일

# 미세먼지 데이터에서 결측치를 포함하는 행 출력하기
print(' ---결측치를 포함한 데이터 출력--- ')
print(dust[dust.isna().any(axis=1)])

#----------------------------------------------------------------

# 결측치 값 채우기
# 결측치가 나타나기 이전 값으로 결측치를 채움 ffill
print('----결측치 채우기----')
dust.ffill(inplace=True)
print(dust.isnull().sum())

#이전 결측치의 index를 다시 출력해서 확인
print('----이전 결측치 index----')
print(dust.iloc[132:134])
print()
print()

#----------------------------------------------------------------
# 날씨 데이터 정보 확인
#----------------------------------------------------------------
print('---------------------------날씨---------------------------')
# 날시 데이터 읽기
wtr= pd.read_excel('weather.xlsx')
print(tabulate(wtr.head(), headers='key', tablefmt='psql'))

print('----날시데이터 기본정보----')
print(wtr.info())

#----------------------------------------------------------------

# 날씨 데이터 컬럼 삭제 및 컬럼 이름 변경
wtr.drop(['지점', '지점명'], axis=1, inplace=True)
wtr.columns = ['date', 'temp', 'wind', 'rain', 'humidity']
print(tabulate(wtr.head(), headers='keys', tablefmt='pretty'))

#----------------------------------------------------------------

# 날씨 데이터 가공: 시간정보삭제
# wtr['date']컬럼에서 시간 정보 삭제 후 데이터 타입 확인
# 년도-월-일 시간 -> 년도-월-일
wtr['date'] = pd.to_datetime(wtr['date'].dt.date)
print(wtr.info())
print(wtr.head())
print()

#----------------------------------------------------------------

# 날씨 데이터 결측치 확인
print('---날씨 데이터 결측치 개수 확인하기---')
print(wtr.isna().sum())

print()

print('---날씨 데이터에서 결측치를 포함하는 행 출력---')
print(wtr[wtr.isna().any(axis=1)])

print()

#----------------------------------------------------------------

print('-----결측치채우기-----')
# 결측치 채우기
# 날씨 데이터 결측치 채우기 ffill()
wtr.ffill(inplace=True)
print(wtr.isna().sum())

print(wtr.iloc[[369,565,742]])

print()

#----------------------------------------------------------------

# 강수량 데이터 변경
# 강수량측정
# 기상청에서는 0.1 단위로 강수량 측정 : 강수량이 0.1 이하면 0으로 표시
# 강수량 rain 컬럼에서 0인 데이터를 0.01로 변경 후 빈도수 출력
print('---강수량이 0인 항목을 0.01로 변경---')
wtr['rain'] = wtr['rain'].replace(0, 0.01)
print(wtr['rain'].value_counts())

print()

#----------------------------------------------------------------

print('----------두 데이터 크기 확인----------')
# 두 데이터를 병합하기 위해 필요 없는 행을 삭제
# 미세먼지 데이터와 날씨 데이터의 (행,열)의 크기를 확인
print('dust, wtr의 크기 확인')
print('dust.shape : ', dust.shape)
print('wtr.shape : ', wtr.shape)

print()

print('---데이터 갯수 확인 후 같게 만들기---')
print(dust.iloc[740:])

print()

print(wtr.iloc[740:])

print()

print('삭제후 미세먼지 데이터확인')
dust.drop(index=743, inplace=True)
print(dust.shape)

print()

#----------------------------------------------------------------

print('----------데이터프레임 병합하기:merge()----------')
#데이터 병합
# 내부 조인(inner join) : 둘 이상의 df에서 조건에 맞는 행을 연결
#                         즉 공통인 행(ex:date) 우리가 삭제하고 크기를 같게한 이유
# 외부 조인(outer join) : 한쪽 df에만 존재하는 데이터를 다른 df에 결합
#                         그냥 다 같다 붙이기

# 사용법
# pd.merge(df1(left), df2(right), how='inner', on=None, left_on=None,
#          right_on=None, left_index=True, right_index=Ture)

print('dust, wtr를 합쳐 새로운 데이터 프레임탄생')
merged_df = pd.merge(dust, wtr, on='date')
print(merged_df.head())
print(merged_df.info())

print()

#----------------------------------------------------------------

print('----------데이터 분석----------')
print('모든 요소별 상관관계 확인')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(merged_df.corr())

print()

print('미세먼지(PM10)과 상관관계 분석')
corr = merged_df.corr()
print(corr['PM10'].sort_values(ascending=False)) # 내림차순 정렬

print()

#----------------------------------------------------------------
print('----------히스토그램으로 시각화----------')

import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

plt.figure(figsize=(15,10))
daygraph = sns.barplot(x='day', y='PM10', data=merged_df)
plt.title('날짜별 PM10 농도')
plt.show()

# 히트맵 작성
plt.figure(figsize=(15,10))
sns.heatmap(data=corr, annot=True, fmt='.2f', cmap='hot')
plt.show()

# 산점도
plt.figure(figsize=(15,10))
x = merged_df['PM10']
y = merged_df['PM2.5']

plt.plot(x, y, marker='o', linestyle='none', color='red', alpha=0.5)
plt.title('PM10 vs. PM2.5')
plt.xlabel('PM10')
plt.ylabel('PM2.5')
plt.show()














