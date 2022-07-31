n = int(input())
numbers = list(map(int,input().split()))

numset = set(numbers) 
a = list(numset)
a.sort() 

cordict = {}
for i in range(len(a)):
    cordict[a[i]] = i

for i in numbers:
    print(cordict[i], end=' ')

