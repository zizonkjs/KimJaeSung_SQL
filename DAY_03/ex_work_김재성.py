import csv
import matplotlib.pyplot as plt
import re # 정규식 복잡한 문자열 처리
import koreanize_matplotlib
import math
import platform

f = open('gender.csv', encoding='euc_kr')
data = csv.reader(f)
city_list = ['대구광역시', '대구광역시 중구', '대구광역시 동구', '대구광역시 서구', '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구', '대구광역시 달서구', '대구광역시 달성군', '대구광역시 군위군']
male_list = []
female_list = []
for city in city_list:

    for row in data:
        if city in row[0]:
            for i in [105]:
                male_list.append(int(row[i].replace(',','')))
                female_list.append(int(row[i+103].replace(',','')))
            break

total=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
    total[i]=male_list[i]+female_list[i]

print(f'대구 남자 인구 : {male_list}')
print(f'대구 여자 인구 : {female_list}')
print(f'대구 여자남자 전체 인구 : {total}')

fig, axs = plt.subplots(5, 2, figsize=(10, 15))

axs[0, 0].pie([male_list[0], female_list[0]])


