num = int(input())
loca = list(map(int, input().split()))

loca.sort()

print(sum(loca)//num)

