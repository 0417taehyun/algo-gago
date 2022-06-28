S = list(map(int, input().split()))

listsum = 0
comparenum = 0
answer = 0 


S.sort(reverse=True)

for i in S:
    if i != 1:
        answer = 0
    else: 
        listsum += i
        comparenum += 1
        if listsum > comparenum:
            answer = comparenum