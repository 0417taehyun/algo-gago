def solution(array,start,end):
    mid = (start+end)//2
    if start > end:
        return None
        
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return solution(array, start, mid - 1)
    else:
        return solution(array,mid + 1,end)