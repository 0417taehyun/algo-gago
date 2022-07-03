#Combinations -> 조합이니까? 같은 무게 제외는 따로?
from itertools import combinations

n,m = map(int, input().split())
k = list(map(int, input().split()))

result = combinations(k,2)

print(result)

#중첩반복을 통해 비교 -> 복잡도를 줄이는 방법은 없나?
n,m = map(int, input().split())
k = list(map(int, input().split()))

result = 0
for i in range(len(k)-1):
  for j in range(i+1,len(k)):
    if k[i] != k[j]:
      result += 1

print(result)