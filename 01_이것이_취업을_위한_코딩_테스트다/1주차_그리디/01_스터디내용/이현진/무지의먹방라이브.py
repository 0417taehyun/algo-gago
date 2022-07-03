def solution(food_times, k):
    answer = 0
    food_amount = len(food_times)
    
    for i in range(1,k+1):
        if food_times[i%food_amount-1] < 1:
            continue
        food_times[i%food_amount-1] -= 1
        answer = i%food_amount
        
    return answer

food_times = list(map(int, input().split()))
k = int(input())

result = solution(food_times, k)
print(result)