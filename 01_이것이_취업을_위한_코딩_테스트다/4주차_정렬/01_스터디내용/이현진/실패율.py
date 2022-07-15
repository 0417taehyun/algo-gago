def solution(N, stages):
    answer = []
    
    failed = [0]*N
    for i in range(len(stages)):
        failed[stages[i]] += 1
    
    for i in range(len(failed)):
        if failed[i] != 0:
            percent = float(failed[i]/N)
            answer.append(failed[i],percent)
    
    def setting(data):
        return data[1]
    
    answer.sort(key=setting)
    
    return answer