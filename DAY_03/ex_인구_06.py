import csv
import matplotlib.pyplot as plt
import re # 정규식 복잡한 문자열 처리
import koreanize_matplotlib

def draw_pie(city, pop_list, label_list):
    plt.pie(pop_list, labels=label_list, autopct='%.1f%%', startangle=90, colors=plt.cm.Pastel2.colors, textprops={'fontsize':8})
    plt.legend(loc=1)
    plt.title(city + '학령인구 비율')
    plt.show()

def draw_donut(city, pop_list, label_list):
    plt.pie(pop_list, labels=label_list, autopct='%.1f%%', startangle=90, colors=plt.cm.Pastel1.colors, pctdistance=0.85, textprops={'fontsize':6})
    center_circle= plt.Circle((0,0), 0.7, facecolor='white')
    fig = plt.gcf()
    plt.legend(loc=1)
    plt.title(city + '학령인구 비율')
    plt.show()

def get_pop(row, start, end):
    pop = 0
    for num in row[start:end+1]:
        num = num.replace(',','')
        num = int(num)
        pop += num
    return pop

def school_age_pop(city):
    city_pop=0
    non_school_pop=0
    school_age_pop=0

    label_list = ['초등학생', '중학생', '고등학생', '대학생', '비학령인구']
    pop_list = []

    f=open('age.csv', encoding='euc_kr')
    data = csv.reader(f)
    header = next(data)

    for row in data:
        if city in row[0]:
            city_pop = row[1]
            city_pop = city_pop.replace(',','')
            city_pop = int(city_pop)

            # 초딩 : 6세[9]~11세[14]
            elementary_pop = get_pop(row, 9 , 14)
            pop_list.append(elementary_pop)

            # 중딩 : 12세[15]~14세[17]
            middleschool_pop = get_pop(row, 15, 17)
            pop_list.append(middleschool_pop)

            # 고딩 : 15세[18]~17세[20]
            highschool_pop= get_pop(row, 18, 20)
            pop_list.append(highschool_pop)

            # 대딩 : 18세[21]~21세[24]
            university_pop = get_pop(row, 21, 24)
            pop_list.append(university_pop)

            school_age_pop = (elementary_pop + middleschool_pop + highschool_pop + university_pop)
            
            # 비학령 인구 계산
            non_school_pop = city_pop - school_age_pop
            pop_list.append(non_school_pop)
            break
    school_age_pop_rate= round((school_age_pop*100)/city_pop, 1)

    print(f'전체 인구수: {city_pop}',
          f'학령 인구수: {school_age_pop}',
          f'학령 인구 비율: {school_age_pop_rate}%')
    
    draw_pie(city, pop_list, label_list)
    draw_donut(city, pop_list, label_list)

city=input('학령 인구 분석할 도시 입력 :')
school_age_pop(city)
    
            
