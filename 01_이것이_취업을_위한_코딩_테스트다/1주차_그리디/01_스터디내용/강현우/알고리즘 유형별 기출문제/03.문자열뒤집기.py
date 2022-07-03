S = list(map(int, input().split()))

countofzero = 0
answer = 0

for i in S:
    if S[i] != 0:
        S[i] = 0
        countofzero += 1
        if countofzero > int(len(S)/2):
            answer = len(S) - countofzero
        else:
            answer = countofzero

