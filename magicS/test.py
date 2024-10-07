# 값을 무시하기 위해 _ 사용
for _ in range(5):
    print("Hello, world!")

# 값을 사용하지 않는 반복
squares = [i**2 for i in range(10)]  # 일반적인 리스트 컴프리헨션
# useless_squares = [i**2 for _ in range(10)]  # 여기서는 _가 i 대신 사용될 수 있음
print(squares)

# 튜플 언패킹에서 무시되는 값
person = ("John", "Doe", 30)
first_name, last_name, _ = person  # 나이는 무시됨
