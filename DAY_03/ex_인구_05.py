import csv
import matplotlib.pyplot as plt
import re # 정규식 복잡한 문자열 처리
import koreanize_matplotlib

def parse_city_name(city):
    #행정구역 명칭에서 숫자 부분을 제거함

    city_name = re.split('[()]', city)
    return city_name[0]

# 전체 인구수 대비 투표 가능 인구의 파이차트 작성
def draw_pie(city_name, city_pop, voting_pop):
    non_voting_pop = city_pop - voting_pop
    pop = [non_voting_pop, voting_pop]
    color = ['tomato', 'royalblue']
    plt.pie(pop, labels=['18세 미만', '투표가능인구'], autopct='%.1f%%', colors=color, startangle=90)

    plt.legend()
    plt.title(city_name + '투표 가능 인구 비율')
    plt.show()

def get_voting_pop(city):
    f=open('age.csv', encoding='euc_kr')
    data = csv.reader(f)
    header= next(data)

    city_name=''
    city_pop = 0 # 도시 전체 인구수
    voting_pop = 0
    for row in data:
        if city in row[0]:
            city_pop = row[1]

            city_pop = city_pop.replace(',','')
            city_pop = int(city_pop)

            city_name = parse_city_name(row[0])
            for data in row[21:]: # 18세 이상
                data = data.replace(',', '')
                voting_num = int(data)
                #누적된 투표 가능 인구수
                voting_pop +=voting_num
            break
    f.close()
    print(f'{city_name}전체 인구수:{city_pop:,}명, 투표 가능 인구수: {voting_pop:,}명')
    
    draw_pie(city_name, city_pop, voting_pop)

city = input('투표 가능 인구수를 확인할 도시이름 입력 :')
get_voting_pop(city)

