n = int(input())

usage = []
for i in range(n):
    start, end = map(int, input().split())
    usage.append([start, end])

usage.sort( key= lambda x: (x[1],x[0]))

finish = usage[0][1]
meeting = 1

for i in range(n):
    if usage[i][0] >= finish:
        meeting += 1
        finish = usage[i][1]

print(meeting)