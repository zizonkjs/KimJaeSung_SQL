import csv
import matplotlib.pyplot as plt
import re # 정규식 복잡한 문자열 처리
import koreanize_matplotlib

def print_pop(pop):
    #특정 지역의 인구 현황 출력

    for i in range(len(pop)):
        print(f'{i:3d}세 : {pop[i]:4d}명', end=' ')
        if ( i + 1 ) % 10 == 0 :
            print()
    print()

def draw_g_pop(title, male_list, female_list):
    plt.barh(range(len(male_list)), male_list, label='남성')
    plt.barh(range(len(female_list)), female_list, label='여성')
    plt.rcParams['axes.unicode_minus'] = False
    plt.title(title + '성별 인구 비율')
    plt.legend()
    plt.show()

def cal_pop():
    f = open('gender.csv', encoding='euc_kr')
    data = csv.reader(f)
    male_list = []
    female_list = []

    district = input('시군구 이름을 입력:')
    for row in data:
        if district in row[0]:
            for male in row[106:207]:
                male = male.replace(',','')
                male_list.append(int(male))
            for female in row[209:310]:
                female = female.replace(',','')
                female_list.append(int(female))
    f.close()

    print(f'남성 총 인구:{sum(male_list):,}')
    print_pop(male_list)
    print('-'*50)
    print(f'여성 총 인구:{sum(female_list):,}')
    print_pop(female_list)
    draw_g_pop(district, male_list, female_list)

def cal_pop_minus():
    f = open('gender.csv', encoding='euc_kr')
    data = csv.reader(f)
    male_list = []
    female_list = []

    district = input('시군구 이름을 입력:')
    for row in data:
        if district in row[0]:
            for male in row[106:207]:
                male = male.replace(',','')
                male_list.append(-int(male))
            for female in row[209:310]:
                female = female.replace(',','')
                female_list.append(int(female))
            break
    f.close()

    print(f'남성 총 인구:{sum(male_list):,}')
    print_pop(male_list)
    print('-'*50)
    print(f'여성 총 인구:{sum(female_list):,}')
    print_pop(female_list)
    draw_g_pop(district, male_list, female_list)



cal_pop_minus()