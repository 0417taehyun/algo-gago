def binary_search(x,array):
    answer = 0
    left = 0 
    right = 0
    reversed_array = array.reverse()
    if x > max(array):
        answer = -1
        return answer
    while left != right:
        for i in len(array):
            if array[i] == x:
                left = i
        for j in len(array):
            if reversed_array[j] == x:
                right = j
    answer = len(array) - (i+j+2)
    return answer
        

