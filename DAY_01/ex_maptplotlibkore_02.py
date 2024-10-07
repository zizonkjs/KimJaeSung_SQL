import csv

f = open('daegu.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter=',')
count=0
for row in data:
    if count > 5:
        break
    else:
        print(row)
    count +=1
f.close()
#-------------------------------------------------------------------------------------------
import csv
# encoding='utf-8-sig'로 \ufeff 제거하기
fin = open('daegu.csv', 'r', encoding='utf-8-sig') # 'r' 읽기모드
data = csv.reader(fin, delimiter=',')

# newline='': 한 라인씩 건너 뛰며 저장되는 현상을 없애기
fout = open('daegu-utf8.csv', 'w', newline='', encoding='utf-8-sig') # 'w' 쓰기 모드
wr = csv.writer(fout)

for row in data: # csv파일안에 한개 행을 하나씩 읽기
    for i in range(len(row)):
        row[i] = row[i].replace('\t','')
    print(row) # 바뀐내용 출력
    wr.writerow(row) # 한행씩 파일안에 저장하기

fin.close()
fout.close()
print('파일 저장 완료')
#-------------------------------------------------------------------------------------------

import csv
# 대구 최저, 최고 기온 날짜와 온도 구하기
def get_minmax_temp(data):
    # 최고 기온 및 최고 기온의 날짜 설정
    header = next(data)

    min_temp = 100
    min_data = ''

    max_temp = -999
    max_date=''

    for row in data:
        if row[3]== '': # [-1]: 리스트에서 마지막 데이터가 없는 경우
            row[3]=100
        row[3] = float(row[3])

        if row[4] == '': # [-1]: 리스트에서 마지막 데이터가 없는 경우
            row[4]=-999
        row[4] = float(row[4])

        # 최저 기온 계산
        if row[3] < min_temp:
            min_temp = row[3]
            min_date = row[3]
        
        # 최고 기온 계싼
        if row[4] > max_temp:
            max_temp = row[4]
            max_date = row[0] # 날자 : index [0]
    

    print('-' * 50)
    print(f'대구 최저 기온 날짜 : {min_date}, 온도 : {min_temp}')
    print(f'대구 최고 기온 날짜 : {max_date}, 온도 : {max_temp}')

def main():
    f = open('daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    get_minmax_temp(data)
    f.close()

main()
#-------------------------------------------------------------------------------------------

# 최고 기온 데이터를 히스토그램으로 표현하기

# 1. 한글 폰트 사용시 레이블의 '-' 기호 깨지는 현상 해결하기

# plt.rc('axes', unicode_minus=False)또는plt.rcParams['axes.unicode_minus'] = False 사용

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)
res=[]

for row in data : 
    if row[-1] != '' :
        res.append(float(row[-1]))
f.close()

plt.figure(figsize=(10,2))
plt.hist(res, bins=500, color='blue')
plt.rc('font', family='Malgun Gothic')

plt.rcParams['axes.unicode_minus'] = False
plt.title('1907년 부터 2024년까지 대구 기온 히스토그램')
plt.show()
         
#-------------------------------------------------------------------------------------------

# 기온히스토그램 만들기 8월

f = open('daegu-utf8.csv', encoding='utf-8-sig')

data = csv.reader(f)
next(data)
aug = []

for row in data :
    if row[0] != '' and row[4] != '':
        month = row[0].split('-')[1]
        if month == '08':
            aug.append(float(row[-1]))
f.close()

plt.hist(aug, bins=100, color='tomato')
plt.title('대구 8월의 최고 기온 히스토그램')
plt.xlabel('Temperature')
plt.ylabel('Counts')
plt.show()
#-------------------------------------------------------------------------------------------

# # 매년 특정 날짜의 최고 기온 찾기

def draw_graph_on_date(month, day):
    f = open('daegu-utf8.csv', encoding='utf-8-sig')
    data=csv.reader(f)
    next(data)
    res=[]
    for row in data:
        if row[-1] != '':
            date_string = row[0].split('-')
            if date_string[1] == month and date_string[2] == day:
                res.append(float(row[-1])) # 최고 기온을 시수형으로 변환 후 리스트에 추가
    f.close()

    plt.figure(figsize=(15,2))
    plt.plot(res, 'royalblue')
    plt.rc('axes', unicode_minus=False)
    plt.title(f'매년 {month}월 {day}일 최고 기온 변화')
    plt.show()

month, date = input('날짜 월 일 을 공백 기준으로 입력하세요 : ').split()

draw_graph_on_date(month, date)

#-------------------------------------------------------------------------------------------

# 2000년 이후 특정일의 최저, 최고 기온 찾기 # 1
import platform

def draw_lowhigh_graph(start_year, month, day):
    f = open('daegu-utf8.csv', encoding='utf-8-fig')
    data = csv.reader(f)
    next(data)
    high_temp = []
    low_temp=[]
    x_year = []
    for row in data :
        if row[-1] != '':
            date_string = row[0].split('-') # 날짜 데이터를 분리함
            if int(date_string[0]) >= start_year: # 문자열 값을 int형으로 변환해서 비교
                if int(date_string[1]) == month and int(date_string[2]) == day:
                    high_temp.append(float(row[-1]))
                    low_temp.append(float(row[-2]))
                    x_year.append(date_string[0])
    f.close()
    
    plt.figure(figsize=(20,4))
    plt.plot(x_year, high_temp, 'hotpink', marker='o', label='최고기온')
    plt.plot(x_year, low_temp, 'royalblue', marker='s', label='최저기온')
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic', size=8)
    else:
        plt.rc('font', family='AppleGothic', size=8)

    plt.rcParams['axes.unicode_minus'] = False
    plt.title(f'{start_year}년 이후 {month}월 {day}일의 온도 변화 그래프', size=16)

    plt.legend(loc=2)
    plt.xlabel('year')
    plt.ylabel('temperature')
    plt.show()

draw_lowhigh_graph(2000, 7, 26)


