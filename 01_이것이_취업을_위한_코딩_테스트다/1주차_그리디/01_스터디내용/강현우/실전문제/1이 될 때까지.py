n,k = map(int, input().split())
acount = 0
parameter = int(n**(1/2)) # 루트n보다 k를 더 나눌 순 없다. 

for y in range(1,parameter):
    if k**y <= n: # 미세하게나마 나눌셈보다는 곱셈이 더 연산 속도가 빠른걸로 알아서, 곱셈 적용.
        acount += 1 

result = n-k**acount + acount # n-k**acout가 1번 조건(-1씩 하는 조건)의 총 횟수, acount가 나누는 횟수.

print(result)