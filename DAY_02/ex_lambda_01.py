#  여러 항목을 가지는 리스트 정렬
# key 매개변수에 lambda 사용

students= [('Alice', 3.9, 20160303),
           ('Bob', 3.0, 20160302),
           ('Charlie', 4.3, 20160301)]

# 학번 (students[2]을 기준으로 오름차순 정렬)
sorted_students1 = sorted(students, key = lambda s: s[2])
print(sorted_students1)

# 학점(s[1])을 기준으로 내림 차순 정렬
sorted_students2 = sorted(students, key = lambda s: s[1], reverse=True)
print(sorted_students2)