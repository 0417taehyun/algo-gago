'''
- 0을 바꾸는 횟수와 1을 바꾸는 횟수중 최솟값을 구한다.
- 각 숫자를 바꾸는 경우는 이전의 데이터와 일치하지 않을 때이다.
'''
data = input()
count0 = 0 #0을 뒤집는 횟수
count1 = 0 #1을 뒤집는 횟수
'''
if data[0] == 0: #이후의 데이터와 일치하는지 비교하기 위해 첫번째 데이터를 뒤집는다
    count0 += 1 #첫번째 원소가 0인 경우
else:
    count1 += 1 #첫번째 원소가 1인 경우
'''
for i in range(len(data)):
    if data[i] != data[i+1]: #이전의 데이터와 일치하지 않는 경우
        if data[i+1] == '0':
            count0 += 1
        else:
            count1 += 1

result = min(count0, count1)
print(result)