import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

#  지하철 각 노선별 7~9시 최대 하차 인원을 막대그래프로 표시하고, 하차인원 출력

# 호선 변수를 넣으면 시간대에 맞게 하차 인원 반환


# def subway_time():

#     with open('subwaytime.csv', encoding='utf-8-sig')as f:
#         data= csv.reader(f)
#         next(data)
#         next(data)

#         for row in data:
#             row[4:]= map(int,row[4:])
일호선='1호선'
이호선='2호선'
삼호선='3호선'
사호선='4호선'
오호선='5호선'
육호선='6호선'
칠호선='7호선'




# def subway_time(subway_name):
#     res=[]
#     total_number=0

#     with open('subwaytime.csv', encoding='utf-8-sig')as f:
#         data= csv.reader(f)
#         next(data)
#         next(data)

#         for row in data:
#             if row[1] in subway_name:
#                 row[4:]= map(int,row[4:])
#                 total_number += row[12]+row[14]
                
#                 res.append(row[12])
#     print(f'총 지하철 역의 수 : {len(res)}')
#     print(f'아침 7시~9시 {subway_name} 하차인원 : {total_number}')

    
#     return total_number

# t1=subway_time(일호선)
# print(t1)

# t2=subway_time(이호선)
# print(t2)

# t3=subway_time(삼호선)
# print(t3)

# t4=subway_time(사호선)
# print(t4)

# t5=subway_time(오호선)
# print(t5)

# t6=subway_time(육호선)
# print(t6)

# t7=subway_time(칠호선)
# print(t7)

# 하차인원=[t1, t2, t3, t4, t5, t6, t7]
def hosen(name):
    max_num=[]
    for row in data:
        row[4:] = map(int, row[4:])
        print(row[11])
        
            
        station_name = row[3] + '(' + row[1] + ')'
        return station_name, passenger_num
# station_list.append((station_name, passenger_num))
# 지하철 각 호선 별 하차인원이 가장 많은 역과 하차인원 표시
with open('subwaytime.csv', encoding='utf-8-sig')as f:
    data= csv.reader(f)
    next(data)
    next(data)

    station_list=[]
    passenger_num=[]
    max_num = -1
    max_station=''

    station_name1, passenger_num1=hosen(일호선)
    station_list.append(station_name1)
    passenger_num.append(passenger_num1)

    station_name2, passenger_num2=hosen(이호선)
    station_list.append(station_name2)
    passenger_num.append(passenger_num2)

    station_name3, passenger_num3=hosen(삼호선)
    station_list.append(station_name3)
    passenger_num.append(passenger_num3)

    station_name4, passenger_num4=hosen(사호선)
    station_list.append(station_name4)
    passenger_num.append(passenger_num4)

    station_name5, passenger_num5=hosen(오호선)
    station_list.append(station_name5)
    passenger_num.append(passenger_num5)

    station_name6, passenger_num6=hosen(육호선)
    station_list.append(station_name6)
    passenger_num.append(passenger_num6)

    station_name7, passenger_num7=hosen(칠호선)
    station_list.append(station_name7)
    passenger_num.append(passenger_num7)


    
print(station_list)
print(passenger_num)
    