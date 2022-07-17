from tkinter import N


def solution(N,stages):
    result = []
    length = len(stages)

    for i in range(1,N + 1):
        InStagePerson = stages.count(i)
        if length == 0:
            failure = 0
        else:
            failure = InStagePerson/length

        result.append(i,failure)
        length -= InStagePerson
    
    result = sorted(result, key = lambda x:x[1], reverse=True)
    result = [x[0] for x in result]
    return result

