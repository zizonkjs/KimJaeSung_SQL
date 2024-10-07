import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv
import pandas as pd
import numpy as np

# 판다스 실행
wdf= pd.read_csv('daegu-utf8.csv', encoding='utf-8-sig')
print(wdf.columns)
print(wdf['날짜'].dtype)

# 날짜 컬럼의 데이터 타입을 datetime타입으로 변경
wdf['날짜']=pd.to_datetime(wdf['날짜'], format='%Y-%m-%d')
# print(wdf['날짜'].dt.year == 2024)
# print(wdf['날짜'].dt.month == 6)

# # 결측시 개수 구하기
# print(wdf.head(5))
# print(wdf.shape)
# num_rows = wdf.shape[0]

# num_missing = num_rows - wdf.count()
# print(num_missing)
# print('-'*50)
# # 결측치 처리
# wdf= wdf.dropna(axis=0)
# print(wdf.count())
# print(wdf.head(5))

# wdf.to_csv('daegu-utf8-df.csv', index=False, mode='w', encoding='utf-8-sig')



# 최고기온 및 최저기온 데이터를 이용하여 입력된 달의 각각 평균값을 구함
# 특정 연도와 달의 DataFrame 가져오기
wdf=pd.read_csv('daegu-utf8-df.csv')
# datetime 객체 접근
wdf['날짜']=pd.to_datetime(wdf['날짜'], format='%Y-%m-%d')

def min_max_mean(year, month):
    year_df = wdf[wdf['날짜'].dt.year== year]
    month_df = year_df[year_df['날짜'].dt.month==month]

    max_t_mean = round(month_df['최고기온'].mean(), 1)
    min_t_mean = round(month_df['최저기온'].mean(), 1)

    return max_t_mean, min_t_mean
    # year년 month월 최저 기온 평균 : XX, 최고 기온 평균 : XX

# # 시작 연도, 마지막연도 최고 기온 비교
# def main():
#     start_year=int(input("시작할 년도를 입력하세요."))
#     last_year=int(input("마지막년도를 입력하세요."))
#     search_month=int(input("비교할 월을 입력하세요."))

#     startyear=list(min_max_mean(start_year, search_month))
#     lastyear=list(min_max_mean(last_year, search_month))

#     print(f"시작 연도({start_year})의 최고 기온 평균: {startyear[0]}, 최저 기온 평균: {startyear[1]}")
#     print(f"마지막 연도({last_year})의 최고 기온 평균: {lastyear[0]}, 최저 기온 평균: {lastyear[1]}")
#     return startyear, lastyear

# main()

def main():
    search_month=int(input('비교할 월 입력 :'))
    first_decade = int(input('시작할 년도 :'))
    second_decade = int(input('마지막 년도 :'))

    max_list=[]
    min_list=[]

    
    for a in range(first_decade,second_decade+1):
        max_mean, min_mean = min_max_mean(a, search_month)
        max_list.append(max_mean)
        min_list.append(min_mean)

    print(max_list)
    print(min_list)
    return first_decade, second_decade, search_month, max_list, min_list
first_decade, second_decade, search_month, max_list, min_list=main()


yyear=list(range(first_decade,second_decade+1))
plt.figure(figsize=(20,4))
plt.plot(yyear, max_list,'red', marker='o', label='최고기온')
plt.plot(yyear, min_list,'royalblue', marker='s', label='최저기온')
plt.rcParams['axes.unicode_minus']=False
plt.title(f'KOR {first_decade} ~ {second_decade} to {search_month} change temperature ')

plt.legend(loc=2)
plt.xlabel('year')
plt.ylabel('temperature')
plt.show()



