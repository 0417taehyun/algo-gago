'''
실전 3 숫자 카드 게임
n개의 행과 m개의 행을 첫번째 줄에 입력받음
둘째줄부터는 각 행의 데이터를 입력받는다
'''
n,m = map(int, input().split())

max = 0
for i in range(n):
    arr = list(map(int, input().split()))
    min = min(arr)
    max = max(max, min)

print(max)
    