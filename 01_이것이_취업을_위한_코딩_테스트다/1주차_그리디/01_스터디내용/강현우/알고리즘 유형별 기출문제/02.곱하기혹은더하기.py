S = list(map(int, input().split()))


for i in S:
    maxnum = S[i]
    if i > 1:
       maxnum *= i
    else:
        maxnum += i

