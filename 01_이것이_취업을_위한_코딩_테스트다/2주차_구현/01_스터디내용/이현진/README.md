# 2주차 개념 : 아이디어를 코드로 바꾸는 구현

## 1. 구현이란
+ 코딩테스트에서 구현이란 머릿속에 있는 '알고리즘을 소스코드로 바꾸는 과정'이다.
+ 따라서 구현은 문제를 해결하기 위해 어떤 알고리즘을 사용하는지에 대한 초점이 아니라,
  해당 알고리즘을 어떻게 컴퓨터 언어로 표현할 것인지에 중점을 맞춘다.
---------------

## 2. 구현을 이용하는 문제
+ 구현 유형의 문제에는 '알고리즘을 떠올리기는 쉬우나 소스코드로 옮기기 어려운 문제'들이 해당한다.
+ 따라서 코딩테스트에서 문제를 처음 구현의 방식으로 해결하려고 시도해보고 이가 통하지 않을 경우,
  다른 해결법으로 푸는 것은 일종의 팁이 될 수도 있다.
+ 구현 유형 문제 예시
    + 알고리즘은 간단하지만 코드가 지나치게 길어지는 문제
    + 특정 소수점까지 출력해야하는 문제
    + 리스트로 받은 입력을 한 문자 단위로 파싱해야 하는 문제
    + 라이브러리를 사용해야 하는 문제
---------------

## 3. 방향벡터
+ 코딩테스트에서 주로 구현의 개념이 사용되는 문제에는 '완점탐색'과 '시뮬레이션' 문제가 있다.
    + 완전탐색 : 모든 경우의 수를 주저 없이 다 계산해야하는 해결 방법
    + 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야하는 문제
+ 이러한 문제는 주로 '방향벡터'의 개념을 활용하여 해결한다.
    + 방향벡터 : 주어진 입력이나 상황을 행렬(2차원 리스트)을 통해 구현하고, 이에 따른 움직임을 상하좌우로 표현
    + 예시 :
    ```Python
    # x축과 y축의 이동 방향 : 왼쪽에서부터 차례로 동,서,남,북
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    # 현재 위치 : 시작점이 0,0라는 가정
    x = 0
    y = 0

    for i in range(이동횟수):
        # 다음 위치
        nx = x + dx[i]
        ny = y + dy[i]
    
    # 이동 수행
    x = nx
    y = ny
    ```
------------

## 4. 예제문제풀이
+ 상하좌우
```Python
n = int(input()) 
move = input().split() 

#풀이1. 방향에 따른 좌표이동을 배열로 표현
#인덱스가 동일하면 같은 이동으로 간주한다
dx = [-1,0,1,0]
dy = [0,1,0,-1]
directions = ['U','R','D','L']

x,y = 1,1 

#풀이2. 입력(move)에 따른 이동
#이동계획표만큼 반복하며, 내부에서 방향의 개수만큼 반복하여 서로 비교하여 동일한 방향으로 좌표이동
for m in move:
  for d in range(len(directions)):
    if m == directions[d]:
      if 1<=x+dx[d]<=n and 1<=y+dy[d]<=n:
        x += dx[d]
        y += dy[d]

print(f"{x} {y}")
```
[상세풀이](01_이것이_취업을_위한_코딩_테스트다\2주차_구현\01_스터디내용\이현진\상하좌우.py)
---------------

+ 시각
```Python
n = int(input())

count = 0 

#풀이1. 모든 경우의 수 확인
#시,분,초는 일정한 반복횟수를 가지고 있으므로 모두 반복하며 모든 경우의 수를 확인한다
for x in range(n+1):
  for y in range(60):
    for z in range(60):
      if '3' in str(x) or '3' in str(y) or '3' in str(z): #풀이2. 원소단위의 판별은 배열형태와 유사한 문자열에서 가능하다
        count += 1

print(count)
```
[상세풀이](01_이것이_취업을_위한_코딩_테스트다\2주차_구현\01_스터디내용\이현진\시각.py)
---------------

+ 왕실의 나이트
```Python
place = input()

#풀이1. 문자열의 각 원소를 행과열로 구분한다
#알파벳으로 표현된 열은 ord() 함수를 통해 아스키코드로 변환후, 정수로 변환한다
#해당 아스키코드가 어떤 것인지 모르기 때문에 시작점인 a의 아스키코드를 빼준다
#결과적으로 +1을 해주면 시작점 1을 잘 표현할 수 있다
x = int(place[1])
y = int(ord(place[0])) - int(ord('a')) + 1

#풀이2. 나이트의 이동가능 경로에 따라 좌표의 이동을 리스트로 나타낸다
dx = [-1,1,-1,1,-2,-2,2,2]
dy = [2,2,-2,-2,1,-1,1,-1]
directions = [0,1,2,3,4,5,6,7]

count = 0

for d in directions:
  if 1<=x+dx[d]<=8 and 1<=y+dy[d]<=8:
    count += 1

print(count)
```
[상세풀이](01_이것이_취업을_위한_코딩_테스트다\2주차_구현\01_스터디내용\이현진\왕실의나이트.py)
---------------

+ 게임 개발
```Python
n,m = map(int, input().split())
x,y,d = map(int,input().split())
area = []
for i in range(n):
  area[i].append(list(map(int,input().split)))

#풀이2. 방향에 따른 좌표이동을 표현한다
#해당 축의 이동 리스트의 인덱스와 방향은 일치한다
directions = [0,1,2,3]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#풀이3. 방문여부를 판단하기 위한 배열을 생성하여 사용한다
visited = [[0]*m for _ in range(n)]
count = 0 
cant = 0  

#풀이1. 메뉴얼을 분기할 수 있는 부분을 찾아 조건문을 건다
while(1): #더이상 움직일 수 없을때까지 반복한다
  d = directions[d-1] 
  if visited[x+dx[d]][y+dy[d]] == 0 and area[x+dx[d]][y+dy[d]] == 0: #방문한적없는 육지
    x += dx[d]
    y += dy[d]
    visited[x+dx[d]][y+dy[d]] = 1
    count += 1
    cant = 0
  else: #이미방문했거나 바다이거나 둘다인 경우
    if cant == 4: #사방이 모두 전진할 수 없는 경우
      if area[x-dx[d]][y-dy[d]] == 1: #후진할 수 없는 경우
        break
      else: #후진할 수 있는 경우
        x -= dx[d]
        y -= dy[d]
        count += 1
        cant = 0
    cant += 1
    d = directions[d-1]

print(count)
```
[상세풀이](01_이것이_취업을_위한_코딩_테스트다\2주차_구현\01_스터디내용\이현진\게임개발.py)
----------

+ 럭키 스트레이트
```Python
score = input()

left = []
right = []
for i in range(len(score)):
  if i <= len(score)//2:
    left.append(score[i])
  else:
    right.append(score[i-len(score)//2])

sumL,sumR = 0,0
for i in range(len(left)):
  sumL += int(left[i])
  sumR += int(right[i])

if sumL == sumR:
  print("LUCKY")
else:
  print("READY")
```
[상세풀이](01_이것이_취업을_위한_코딩_테스트다\2주차_구현\01_스터디내용\이현진\럭키스트레이트.py)
-----------

+ 문자열 재정렬
```Python
string = input()

sum = 0
alpha = []
for i in string:
  if 65 <= ord(i) <= 90:
    alpha.append(i)
  else:
    sum += int(i)
alpha.sort()

for i in alpha:
  print(i, end="")
print(sum)
```
[상세풀이](01_이것이_취업을_위한_코딩_테스트다\2주차_구현\01_스터디내용\이현진\문자열재정렬.py)
-----------

+ 문자열 압축
```Python
def compact(s):
  alpha = dict()

  for i in range(len(s)-1):
    for j in range(i,len(s)):
      if s[j] == s[j+1]:
        alpha[s[j]] += 1

  values = alpha.values().sort()
  max = 0
  
  for i in values:
    if len(s)%i == 0:
      max = i
      break

  temp = ""
  result = ""
  count = 0

  for i in range(2,len(s)):
    for j in range(max):
      temp[i] += s[j+i]
      if temp[i] == temp[i-1]:
        count += 1
      else:
        result += str(count)
        result += temp[i]
        count = 0
  
  return count(result)
```
[상세풀이](01_이것이_취업을_위한_코딩_테스트다\2주차_구현\01_스터디내용\이현진\문자열압축.py)
------------

+ 자물쇠와 열쇠
```Python

```
[상세풀이](01_이것이_취업을_위한_코딩_테스트다\2주차_구현\01_스터디내용\이현진\자물쇠와열쇠.py)
------------

+ 뱀
```Python

```
[상세풀이]()
------------

+ 기둥과 보 설치
```Python

```
[상세풀이]()
------------