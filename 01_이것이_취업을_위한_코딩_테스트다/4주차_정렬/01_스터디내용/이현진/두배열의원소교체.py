#입력
n,k = map(int, input().split())
a = []
b = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))
  
#정렬
#원리 : a의 가장 작은 수 <-> b의 가장 큰 수
a.sort() #가장 작은 숫자순으로 교환
b.sort(reverse=True) #가장 큰 숫자순으로 교환

for i in range(k):
  if(a[i] < b[i]):
    a[i], b[i] = b[i], a[i]

#출력
print(sum(a))