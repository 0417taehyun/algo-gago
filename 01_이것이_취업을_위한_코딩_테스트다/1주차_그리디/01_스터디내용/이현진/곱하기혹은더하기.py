'''
- 연산하는 두 수 중 하나라도 0,1이면 더하는 것이 더 큰 수를 도출해낸다.
- 0,1 이외의 나머지 수는 무조건 곱하는 것이 더 큰 수를 도출해낸다.
- 문자열의 경우 배열과 동일하게 데이터에 접근할 수 있다.
'''
data = input()
result = int(data[0]) #연산을 시작할 첫번째 수
for i in range(1,len(data)):
    number = int(data[i])
    if result <= 1 or number <= 1: #연산하는 두 수중 하나라도 0,1인 경우
        result += number
    else:
        result *= number
print(result)