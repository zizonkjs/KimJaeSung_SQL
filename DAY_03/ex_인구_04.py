import csv
import matplotlib.pyplot as plt
import re # 정규식 복잡한 문자열 처리
import koreanize_matplotlib

# 동 이름을 입력하면 해당 동의 인구 분포를 그리는 함수 구현
def parse_district_name(city):
    #행정구역 명칭에서 숫자 부분을 제거함

    city_name = re.split('[()]', city)
    return city_name[0]

def print_pop(pop):
    #x특정 지역의 인구 현황을 화면에 출력함
    for i in range(len(pop)):
        print(f'{i:3d}세: {pop[i]:4d}명', end=' ')
        if ( i + 1) % 10 == 0:
            print()

def draw_pop(city_name, pop_list):
    # 특정 지역에 대한 인구 분포를 그래프로 나타냄
    # city_name : 지역 이름
    # pop_list : 0~100tp  이상까지 인구수 리스트

    plt.title(f'{city_name} 인구 현황')
    plt.xlabel('나이')
    plt.ylabel('인구수')
    plt.bar(range(101), pop_list)
    plt.xticks(range(0, 101, 10)) # 0~100세 이상
    plt.show()

# 인구 구조 그래프 함수 구현
def get_pop(city):
    f = open('age.csv', encoding='euc_kr')
    data = csv.reader(f)
    next(data)

    pop_list=[]
    full_district_name=''
    for row in data:
        if city in row[0]: # city에 '대' 자만 있어도 in 덕분에 row[0]에서 일치하는 문자열 하나를 찾음.
            full_district_name = parse_district_name(row[0])
            for data in row[3:]:
                data = data.replace(',','') # 천단위 콤마제거
                pop_list.append(int(data))
            break # 처음으로 일치하는 도시명만 검색
    f.close()
    print_pop(pop_list)
    draw_pop(full_district_name, pop_list)

city = input('인구 구조를 알고 싶은 지역의 이름(동 단위):')
get_pop(city)