# 윷놀이 만들기


import random as rd

# 윷가락 4개의 값을 저장
# 앞면 1, 뒷면 0

sticks=[0,0,0,0]

# 1111일 때 모 5점
# 0000일 때 윷 4점
# 1 한개일때 걸 3점
# 1 두개일때 개 2점
# 1 세개일때 도 1점

def 점수계산(던진결과):
    점수 = sum(던진결과)
    if 점수 == 0:
        return 4
    elif 점수 == 1:
        return 3
    elif 점수 == 2:
        return 2
    elif 점수 == 3:
        return 1
    elif 점수 == 4:
        return 5



# 윷놀이 규칙
# if (sticks[0]+sticks[1]+sticks[2]+sticks[3]==0) or (sticks[0]+sticks[1]+sticks[2]+sticks[3]==4):
#     #한번더 윷던지기 continue
# if 4>sticks[0]+sticks[1]+sticks[2]+sticks[3]>0:
#     #윷던지기 멈춤
#     break

# 흥부=[0]
# 놀부=[0]

# if 흥부[0]==20:
    #print('흥부승리')
    #break
# if 놀부[0]==20:
    #print('놀부승리')
    #break


# 선=[rd.randint(0,1)]
# 순서=선[0]
# print(순서)


# while True:
#     print('윷놀이')
#     print(' 윷놀이 규칙 ')
#     print('1값이 0일 때 모(4점)')
#     print('1값이 1일 때 걸(3점)')
#     print('1값이 2일 때 개(2점)')
#     print('1값이 3일 때 도(1점)')
#     print('1값이 4일 때 윷(5점)')
#     흥부=[0]
#     놀부=[0]

#     while 순서==0:
#         print('흥부턴')
#         던진결과=[rd.randint(0,1),rd.randint(0,1),rd.randint(0,1),rd.randint(0,1)]
#         print(f'던진결과 : {던진결과}')
    
        
#         if (sum(던진결과)==0) or (sum(던진결과)==4):
#             print(f'던진결과 : {던진결과}')
#             흥부[0] += 점수계산(던진결과)
#             print(f'흥부의 점수 : {흥부[0]}')
#             print('한번더 던집니다.')

#             continue
#         elif 4>sum(던진결과)>0:
#             print(f'던진결과 : {던진결과}')
#             흥부[0] += 점수계산(던진결과)
#             print(f'흥부의 점수 : {흥부[0]}')
#             print('그만던집니다.')
#             break
#         while 순서==1:
#             print('놀부턴')
#             던진결과=[rd.randint(0,1),rd.randint(0,1),rd.randint(0,1),rd.randint(0,1)]
#             print(f'던진결과 : {던진결과}')
        
            
#             if (sum(던진결과)==0) or (sum(던진결과)==4):
#                 print(f'던진결과 : {던진결과}')
#                 놀부[0] += 점수계산(던진결과)
#                 print(f'놀부의 점수 : {놀부[0]}')
#                 print('한번더 던집니다.')

#                 continue
#             elif 4>sum(던진결과)>0:
#                 print(f'던진결과 : {던진결과}')
#                 놀부[0] += 점수계산(던진결과)
#                 print(f'놀부의 점수 : {놀부[0]}')
#                 print('그만던집니다.')
#                 break


#     if 흥부[0]<=20 and 놀부[0]<=20:
#         print(f'{흥부}의 점수')
#         print(f'{놀부}의 점수')
#         print('게임을 계속합니다.')
#         continue
#     elif 흥부[0]>=20 or 놀부[0]>=20:
#         print(f'{흥부}의 점수')
#         print(f'{놀부}의 점수')
#         print('20점 이상인 사람이 나와서 게임을 종료합니다.')
#         break
while True:
    print('-------윷놀이-------')
    print(' 윷놀이 규칙 ')
    print('1값이 0일 때 모(4점)')
    print('1값이 1일 때 걸(3점)')
    print('1값이 2일 때 개(2점)')
    print('1값이 3일 때 도(1점)')
    print('1값이 4일 때 윷(5점)')
    print('-'*50)
    print('거만한 놀부가 흥부에게 선수를 양보합니다.')
    print('놀부 : 형이 양보할께 멍청한 동생아 ^^')
    print('게임을 시작합니다')
    print('-'*50)
    흥부 = [0]
    놀부 = [0]
    
    players = [흥부, 놀부]
    player_names = ["흥부", "놀부"]
    game_over = False
    
    while not game_over:
        for i in range(2):
            current_player = players[i]
            current_name = player_names[i]
            print(f'{current_name} 턴')
            
            while True:
                던진결과 = [rd.randint(0, 1), rd.randint(0, 1), rd.randint(0, 1), rd.randint(0, 1)]
                print(f'던진결과 : {던진결과}')
                
                if (sum(던진결과) == 0) or (sum(던진결과) == 4):
                    current_player[0] += 점수계산(던진결과)
                    print(f'{current_name}의 점수 : {current_player[0]}')
                    print('모나 윷이 나왔음으로 한번더 던집니다.')
                else:
                    current_player[0] += 점수계산(던진결과)
                    print(f'{current_name}의 점수 : {current_player[0]}')
                    print('그만 던집니다.')
                    print('-'*50)
                    break
            
            if current_player[0] >= 20:
                game_over = True
                break
    
    print(f'최종 점수 - 흥부: {흥부[0]}, 놀부: {놀부[0]}')
    if 흥부[0] >= 20:
        print('흥부가 20점 이상으로 승리하였습니다.')
    if 놀부[0] >= 20:
        print('놀부가 20점 이상으로 승리하였습니다.')
    
    break