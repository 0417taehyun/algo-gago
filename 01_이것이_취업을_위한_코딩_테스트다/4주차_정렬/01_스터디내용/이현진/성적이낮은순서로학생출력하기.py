#입력
n = int(input())
array = []
for i in range(n):
  name, score = input().split() #두 입력을 서로 다른 타입으로 저장하기 위해 일단 구분
  array.append((name,int(score))) #튜플형으로 저장하되, 점수는 정수형으로
  
#정렬
def setting(data): #정렬의 기준은 튜플의 1st 인덱스
  return data[1]
  
array.sort(key=setting) 

#출력
for a in array:
  print(a[0], end="") #튜플의 0st 원소인 이름 출력