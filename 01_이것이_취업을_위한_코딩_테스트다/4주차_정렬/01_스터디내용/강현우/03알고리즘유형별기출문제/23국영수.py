number = int(input())

student_info = []

for _ in range(number):
    student_info.append(int(input()))# 이름,국어,영어,수학 순

student_info.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for name in student_info:
    print(student_info[0])
