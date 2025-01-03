# magic square 

import numpy as np

def generate_magic_square(n):
    # 마방진 배열 초기화
    magic_square = [[0] * n for _ in range(n)]

    # 시작 위치 설정
    num = 1
    i, j = 0, n // 2

    while num <= n * n:
        magic_square[i][j] = num
        num += 1

        # 다음 위치 계산
        new_i, new_j = (i - 1) % n, (j + 1) % n

        if magic_square[new_i][new_j] != 0:  # 이미 숫자가 있는 경우
            new_i, new_j = (i + 1) % n, j

        i, j = new_i, new_j

    return magic_square

def print_magic_square(magic_square):
    n = len(magic_square)
    print(f"Magic Square ({n}x{n})")
    for row in magic_square:
        print("\t".join(map(str, row)))
    print("\n")


n = int(input("홀수차 배열의 크기를 입력하세요: "))
if n % 2 == 0:
    print("홀수 크기의 배열만 가능합니다.")
else:
    magic_square = generate_magic_square(n)
    print_magic_square(magic_square)


#   magic_square = [[0] * n for _ in range(n)]
#   for_in range(n) -> range(n)이 생성한 숫자에 대해 반복문을 실행, 실제로 사용하진 않음
# 각 반복에서 [0]*n -> 이코드를 n번 반복해서 0으로 채워진 n개의 요소로 작용함.
