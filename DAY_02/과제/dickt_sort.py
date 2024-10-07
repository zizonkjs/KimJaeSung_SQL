# 1. 딕셔너리 정렬 프로그램

# 아래에 주어진 총 6개 나라의 수도에 대한 국가명, 대륙, 인구수를 표시한 테이블을 이용하여
# 딕셔너리를 작성하고, 아래 실행 화면과 같이 출력을 하는 프로그램을 작성하시오.

con_dict={'Soeul':['South Korea', 'Asia', 9655000],
          'Tokyo':['Japan', 'Asia', 14110000],
          'Beijing':['China', 'Asia', 21540000],
          'London':['United Kingdom','Europe', 14800000],
          'Berlin':['Germany', 'Europe', 3426000],
          'Mexico City':['Mexico', 'America', 21200000]}

# 전체 데이터 출력
def 전체데이터출력():
    print('-'*100)
    for city, details in con_dict.items():
        country = details[0]
        continent = details[1]
        population = details[2]
        print(f'{city:12} | {country:20} | {continent:10} | {population:10,}')
    print('-'*100)

# 수도 이름 오름차순 출력
def 수도이름오름차순출력():
    print('-'*100)
    sorted_con_dict = dict(sorted(con_dict.items()))
    
    # 각 항목을 자리수를 맞춰 출력
    for city, details in sorted_con_dict.items():
        country = details[0]
        continent = details[1]
        population = details[2]
        print(f'{city:12} | {country:20} | {continent:10} | {population:10,}')
    print('-'*100)

# 모든 도시의 인구수 내림차순 출력
def 모든도시인구수_내림차순():
    print('-'*100)
    rsorted_con_dict = sorted(con_dict.items(), key=lambda x: x[1][2], reverse=True)
    for city, details in rsorted_con_dict:
        population = details[2]
        print(f'{city:12} | {population:10,}')
    print('-'*100)

# 특정 도시의 정보 출력
def 특정도시의정보():
    print('-'*100)
    city_name= input('수도이름을 입력하세요(Beijing,Mexico City,London,Tokyo,Soeul,Berlin):')
    if city_name in con_dict:
        city_info = con_dict[city_name]
        print(f"{city_name}:")
        print(f"  나라: {city_info[0]}")
        print(f"  대륙: {city_info[1]}")
        print(f"  인구: {city_info[2]:,}")
    else:
        print(f"도시이름: {city_name}은(는) key에 없습니다.")
    print('-'*100)

# 대륙별 인구수 계산 및 출력

# 대륙 이름 입력 받기
    # continent_name = input("대륙 이름을 입력하세요(Asia,Europe,America): ")

# 대륙별 인구수 계산 및 출력
def 대륙별인구수계산():
    print('-'*100)
    continent_name = input("대륙 이름을 입력하세요(Asia,Europe,America): ")
    total_population = 0
    continent_cities = []

    for city, details in con_dict.items():
        if details[1] == continent_name:
            continent_cities.append((city, details[2]))
            total_population += details[2]
    print('-'*100)

    # 대륙에 속한 국가들의 인구수 출력
    print(f"{continent_name}에 속한 국가들의 인구수:")
    for city, population in continent_cities:
        print(f"{city}: {population:,}")

    # 전체 인구수의 합 출력
    print(f"{continent_name} 전체 인구수의 합: {total_population:,}")
    print('-'*100)

while True:
    print('-'*50)
    print('1. 전체 데이터 출력')
    print('2. 수도 이름 오름차순 출력')
    print('3. 모든 도시의 인구수 내림차순 출력')
    print('4. 특정 도시의 정보 출력')
    print('5. 대륙별 인구수 계산 및 출력')
    print('6. 프로그램 종료')
    num=input('원하는 번호를 누르세요.')
    
    if num in '1':
        전체데이터출력()
    elif num in '2':
        수도이름오름차순출력()
    elif num in '3':
        모든도시인구수_내림차순()
    elif num in '4':
        특정도시의정보()
    elif num in '5':
        대륙별인구수계산()
    elif num in '6':
        print('프로그램을 종료합니다.')
        break
    else:
        print('잘못된 입력입니다. 다시 입력하세요.')
        continue
