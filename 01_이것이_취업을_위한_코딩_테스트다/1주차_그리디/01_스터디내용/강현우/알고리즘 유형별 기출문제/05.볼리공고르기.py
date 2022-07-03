from itertools import combinations


n,m = map(int, input().split())
k = list(map(int, input().split()))

keylist = []
number = 0
for i in range(n):
    number += 1
    keylist.append(number)

data = { keylist:k for keylist,k in zip(keylist,k) }
result = 0

#첫 풀이
for i in range(n):
    for j in range(i+1,n):
        if data.values(i) != data.values(j):
            result +=1
print(result)

#두번째 풀이

from itertools import combinations

k = [1,2,3,4,5,6,2,2]
answer = list(combinations(k,2))
for i in range(len(answer)-1):
    if answer[i][0] == answer[i][1]:
        answer.remove(answer[i])
print(len(answer))



    