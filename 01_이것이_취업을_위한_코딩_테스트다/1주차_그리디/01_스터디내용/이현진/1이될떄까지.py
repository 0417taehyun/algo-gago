'''
실전 4 1이 될 때까지
입력 25 5
출력 2
'''
n,k = map(int, input().split()) #map()를 통해 입력받은 수를 구분하고, int형으로 형변환
count = 0
'''
while n != 1:
    if n%k == 0: #n이 k로 나누어 떨어지는 경우
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)
'''
while True:
    if n < k:
        break #N이 K보다 작으면 더이상 나눌 수 없음

    target = (n//k)*k #N에서 K를 나눈 몫에 K를 곱하면 나누어떨어질 수 있는 가장 가까운 수 도출
    count += (n-target) #따라서 N에서 target을 빼면 나누어 떨어지는 수를 구할 수 있는 가장 최소의 1의 횟수 도출
    
    n = target #1을 뺴는 반복을 위의 과정에서 이미 거침 따라서 n은 k로 나누어떨어지는 수
    n //= k
    count += 1

count += (n-1) #남은 수를 1로 만드는 연산
print(count)