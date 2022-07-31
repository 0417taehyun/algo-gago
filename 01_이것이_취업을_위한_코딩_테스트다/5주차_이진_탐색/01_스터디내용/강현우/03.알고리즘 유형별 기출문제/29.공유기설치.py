n,c = list(map(int,input().split('')))
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

def solution(array,n,c,start,end):
    mid = (start+end) // 2
    previous = array[0]
    count = 1
    for i in range(0,n):
        if array[i] >= mid + previous:
            previous = array[i]
            count += 1
        if count >= c:
            solution(array,n,c,mid+1,end)
        else: 
            solution(array,n,c,start,mid -1)
    return mid
