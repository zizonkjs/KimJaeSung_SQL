# 람다식을 활용한 객체 정렬

class student:
    def __init__(self, name, grade, number):
        self.name = name
        self.grade = grade
        self.number = number

    def __repr__(self):
        return f'({self.name}, {self.grade}, {self.number})'
    
# Student 객체 리스트 생성

students= [student('홍길동', 3.9, 20240303),
           student('김유신', 3.0, 20240302),
           student('박문수', 4.3, 20240301)]
print(students[0])

sorted_list = sorted(students, key=lambda S: S.name)
print(sorted_list)