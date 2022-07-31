n,m = list(map(int,input().split('')))
array = list(map(int,input().split()))

def solution(array,answer):
    needed = 0
    for x in array:
        if x >= answer:
            needed += x - answer
        else: 
            needed += 0
    return needed

answer = max(array)
while (answer >= 0 ):
    if solution(array,answer) >= m:
        break
    else: 
        answer -= 1
        solution(array,answer)

print(answer)