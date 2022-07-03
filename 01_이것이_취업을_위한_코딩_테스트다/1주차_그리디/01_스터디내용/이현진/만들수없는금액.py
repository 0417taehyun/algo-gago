'''
- 만들 수 없는 금액을 도출하기 위해서 리스트의 수를 순서대로 더하며 건너뛰는 숫자가 있는지 확인한다.
'''
n = map(int, input())
data = list(map(int, input().split()))
data.sort()

result = 1
for i in data:
    if result < i:
        break
    result += data[i]

print(data)