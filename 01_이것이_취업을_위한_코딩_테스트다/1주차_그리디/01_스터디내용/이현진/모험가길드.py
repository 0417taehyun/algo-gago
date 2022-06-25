'''
- 공포도가 가장 큰 수부터 멤버를 구성한다.
- 멤버 구성 순서는 공포도가 큰 순서대로 한다.
- 멤버 구성은 공포도가 남은 멤버의 수를 초과할 때까지 반복한다.
'''
#입력
n = map(int, input())
members = list(map(int, input().split()))
#알고리즘
members.sort() #공포도 순으로 정렬
max_fear = 0
result = 0
while max_fear <= n:
    max_fear = members[n-1] #공포도가 가장 큰 모험가
    n -= max_fear #멤버에서 공포도만큼의 구성원을 제외한다
    result += 1 #1회 반복할 때마다 하나의 그룹이 구성된다
#출력
print(result)