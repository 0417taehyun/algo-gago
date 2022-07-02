# 구현(Implementation)

> 아래 내용은 [[ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 구현](https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-implementation) 글을 통해서도 확인 가능합니다.

## 목차

- [개념](#개념)
- [예제](#예제)
  - [4-1. 상하좌우](#4-1-상하좌우)
  - [4-2. 시각](#4-2-시각)
- [실전문제](#실전문제
  - [01. 왕실의 나이트](#01-왕실의-나이트)
  - [02. 게임 개발](#02-게임-개발)
- [기출문제](#기출문제)
  - [01. 럭키스트레이트](#01-럭키-스트레이트)
  - [02. 문자열 재정렬](#02-문자열-재정렬)
  - [03. 문자열 압축](#03-문자열-압축)
  - [04. 자물쇠와 열쇠](#04-자물쇠와-열쇠)
  - [05. 뱀](#05-뱀)
  - [06. 기둥과 보 설치](#06-기둥과-보-설치)
  - [07. 치킨 배달](#07-치킨-배달)
  - [08. 외벽 점검](#08-외벽-점검)


## 개념

**구현(Implementation)**은 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정을 의미한다. 이는 곧 모든 범위의 코딩 테스트 문제 유형을 포함하는 개념이기도 하다.

해당 책에서는 **완전 탐색**과 **시뮬레이션** 알고리즘을 구현 유형으로 묶어서 다루고 있는데 완전 탐색의 경우 모든 경우의 수에 대해 계산해야 하는 알고리즘이고 시뮬레이션의 경우 문제에 제시된 알고리즘을 단계 별로 하나씩 수행해야 하기 때문이다.

구현에서는 결국 문제에서의 조건을 잘 해석하고 시간 복잡도에 대한 부분을 고민하는 게 중요한데 파이썬의 경우 C/C++과 같이 정적으로 자료형을 선언하지 않기 때문에 자료형의 크기에 대한 재설정 부분은 고민하지 않아도 좋고 대신 리스트의 크기만 생각해보면 좋다.

대부분의 코딩 테스트는 메모리를 128MB부터 512MB까지로 제한하는데 1,000만 이하의 데이터를 리스트로 다루는 게 약 40MB 정도의 메모리를 사용하기 때문에 리스트에 담기는 데이터의 수를 대략 계산해서 생각해보면 좋다.

추가로 2020년 파이썬 3.7을 기준으로 1초에 2,000만 번의 연산을 수행한다고 가정하면 대략적으로 시간과 메모리를 계산할 수 있다. 따라서 시간 제한이 1초이고 데이터의 개수가 100만 개인 문제가 있다면 시간 복잡도를 O(NlogN) 이내의 알고리즘을 이용하여 풀어야 한다. N의 값이 100만일 때 NlogN의 값이 곧 2,000만이기 때문이다.

## 예제

### 4-1. 상하좌우

#### 문제

여행가 A가 N X N 크기의 첫 시작 좌표가 (1, 1)인 정사각형 공간에서 주어진 위치 변환을 일러주는 문자에 따라 이동할 때 최종적으로 도착할 지점의 좌표를 구하라.

이때 각 좌표 길이의 끝에서 더 움직이는 요청이 들어올 경우 이는 무시한다.

#### 접근법

간단하게 주어진 이동 계획의 길이 만큼 반복문을 수행하면서 조건문을 통해 만약 좌표의 끝점에 존재할 경우 별다른 움직임을 보이징 않고 그렇지 않은 경우 해당 움직임에 맞게 움직여주면 된다.

#### 소스 코드

> 소스 코드는 [01. 상하좌우.py](./01_예제/01.%20상하좌우.py) 파일에서 확인 가능하다.

```Python
N: int = int(input())
plan: list[str] = list(input().split())

start: list[int] = [1, 1]
for move in plan:
    if move == 'R':
        if start[1] == N:
            pass
        else:
            start[1] += 1

    elif move == 'L':
        if start[1] == 1:
            pass
        else:
            start[1] -= 1

    elif move == 'U':
        if start[0] == 1:
            pass
        else:
            start[0] -= 1

    elif move == 'D':
        if start[0] == N:
            pass
        else:
            start[0] += 1

print(" ".join([ str(point) for point in start ]))
```

#### 시간 복잡도

시간 복잡도는 만약 주어진 이동 계획의 길이가 N이라 할 때 그 길이 만큼 반복문을 돌며 수행하면 되기 때문에 O(N)이다.

### 4-2. 시각

#### 문제

입력된 정수 N에 따라 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하라.

#### 접근법

분과 시의 경우 그 경우의 수가 동일하고 시간만 주어진 N에 따라 다르다.

각각의 조합을 구한 다음에 시와 분, 시와 초, 그리고 분과 초가 중복되는 경우의 수를 빼주고 최종적으로 시와 분과 초가 모두 중복되는 경우의 수를 더해주면 된다.

#### 소스 코드

> 소스 코드는 [02. 시각.py](./01_예제/02.%20시각.py) 파일에서 확인 가능하다.

```Python
N: int = int(input())

hour_count: int = 0
for time in range(N + 1):
    if '3' in str(time):
        hour_count += 1

others_count: int = 0
for time in range(60):
    if '3' in str(time):
        others_count += 1

second_count: int = others_count * 60 * (N + 1)
minute_count: int = others_count * 60 * (N + 1)
total_hour_count = hour_count * 60 * 60

second_minutue_dupliacated = (N + 1) * others_count * others_count
second_hour_dulicated = hour_count * 60 * others_count
minute_hour_duplicate = hour_count * others_count * 60
second_minute_hour_duplicated = hour_count * others_count * others_count

answer = (
    total_hour_count + \
        minute_count + \
            second_count
) - (
    second_minutue_dupliacated + \
        second_hour_dulicated + \
            minute_hour_duplicate
) + second_minute_hour_duplicated

print(answer)
```

책에서는 아래와 같이 삼중으로 중첩된 반복문을 사용해서 문제를 해결했다.

최악의 경우의 수인 N이 23이 주어지더라도 모든 경우의 수가 86,400가지이기 때문에 100,000이 넘지 않는 경우에서 파이썬의 연산은 시간 제한 2초 내에 풀 수 있기 때문이다.

```Python
N: int = int(input())

answer: int = 0
for hour in range(N + 1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second):
                answer += 1

print(answer)
```

#### 시간 복잡도

책에서 제시된 풀이의 경우 시간 복잡도가 최악의 경우를 산정하여 O(86,400)이지만 만약 조합의 경우를 생각하여 문제를 풀 경우 N의 값은 24보다 작기 때문에 아무리 최악의 경우라도 시와 분의 공통적인 경우를 구해주는 반복문의 반복 횟수인 60, 다시 말해 O(60)이 된다.

물론 내 풀이의 경우 중간에 사칙 연산이 포함되긴 하지만 책의 풀이 또한 결국 반복문 내에서 `in` 을 활용해 다시 비교해야 하는 경우도 존재하기에 반복문으로만 따졌을 때 대략적으로 1,440배의 차이가 발생한다.

완전탐색으로 문제를 풀어도 좋지만 수학적인 접근으로 효율적인 문제풀이를 도전해보는 것도 좋아 보인다.

## 실전문제

### 01. 왕실의 나이트

#### 접근법

처음에 상하좌우 모두 두 칸씩 움직이고 그 다음에는 상하로 움직인 경우 좌우 한 칸, 좌우로 움직인 경우 상하 한 칸을 움직이게 된다.

결국 딱 한번의 움직임에 대한 이동 가능여부를 구하면 되기 때문에 상하좌우로 두 칸씩 이동 가능한 경우인지 먼저 조건을 따지고 이후 그곳에서 한 칸 이동 가능한 경우인지 조건을 따지면 된다.

#### 소스 코드

> 소스 코드는 [01. 왕실의 나이트.py](./02_실전%20문제/01.%20왕실의%20나이트.py) 파일에서 확인 가능하다.

```Python
point: str = input()

answer: int = 0
moves = ['U', 'R', 'D', 'L']
for move in moves:
    if move == 'U':
        if int(point[1]) > 2:
            if (point[0] != 'a') and (point[0] != 'h'):
                answer += 2
            else:
                answer += 1

    elif move == 'R':
        if point[0] < 'g':
            if (int(point[1]) != 1) and (int(point[1]) != 8):
                answer += 2
            else:
                answer += 1

    elif move == 'D':
        if int(point[1]) < 7:
            if (point[0] != 'a') and (point[0] != 'h'):
                answer += 2
            else:
                answer += 1

    elif move == 'L':
        if point[0] > 'b':
            if (int(point[1]) != 1) and (int(point[1]) != 8):
                answer += 2
            else:
                answer += 1

print(answer)
```

#### 시간 복잡도

상하좌우 네 번에 대한 경우의 수만 구하면 되기 때문에 시간 복잡도는 상수 시간으로 O(4)이다. 내부적으로 조건문을 따지는 게 사실 반복문의 수보다 더 많이 들어서 해당 상수시간보다는 크지만 그렇게 유의미한 결과를 내지는 않을 것 같아 반복문으로만 따졌다.

#### 기타

조금 더 까다롭게 문제를 출제할 경우 입력 문자가 열과 행이 아닌 행과 열 형태로 들어왔을 경우에 대한 예외 처리를 요구할 수 있다고 적혀 있었다. 라이브 코딩으로 문제를 풀 경우 이러한 입력이 완전히 잘못된 경우에 대한 예외 케이스를 항상 생각해야겠다.

### 02. 게임 개발

#### 접근법

이런 문제의 경우 방문했던 곳에 대한 정보를 저장해두는 게 좋기 때문에 방문한 좌표를 저장할 2차원 배열을 선언한다.

다음으로는 반복을 멈추게 되는 경우에 대한 조건을 확실히 판단하는 게 좋다.

따라서 한 바퀴를 다 돌아서 뒤로 한칸 움직이려 할 때 해당 부분이 바다가 아니면 이미 가봤던 곳이더라도 이동할 수 있지만 만약 바다일 경우 반복문을 빠져 나와야 한다.

#### 소스 코드

> 소스 코드는 [02. 게임 개발.py](./02_실전%20문제/02.%20게임%20개발.py) 파일에서 확인 가능하다.

```Python
N, M = list(map(int, input().split()))
x, y, direction = list(map(int, input().split()))
map_info: list[list[int]] = [ list(map(int, input().split())) for _ in range(N) ]
visited_info: list[list[int]] = [ [0] * M for _ in range(N) ]

answer: int = 1
visited_info[x][y] = 1

circle: int = 0
move_measures: list[tuple(int, int)] = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]

while True:
    if circle == 4:
        x_destination = x - move_measures[direction][0]
        y_destination = y - move_measures[direction][1]

        if map_info[x_destination][y_destination] == 1:
            break

        else:
            circle = 0
            x, y = x_destination, y_destination

    else:
        direction -= 1
        if direction == -1:
            direction = 3

        x_destination = x + move_measures[direction][0]
        y_destination = y + move_measures[direction][1]

        if visited_info[x_destination][y_destination] == 0 and \
            map_info[x_destination][y_destination] == 0:
                circle = 0
                visited_info[x_destination][y_destination] = 1

                answer += 1
                x, y = x_destination, y_destination

        else:
            circle += 1

print(answer)
```

#### 시간 복잡도

이런 시뮬레이션 유형의 구현 문제는 시간 복잡도를 어떻게 구해야할지 감이 잘 안 온다.

최악의 경우를 생각했을 때 주어진 N,M 크기에서 모든 가변을 제외하고 가운데를 전부 도는 경우라 생각되어 O((N-2) \* (M-2)) 정도로 예측했는데 정확한 측정 방법인지 잘 모르겠다.

## 기출문제

### 01. 럭키 스트레이트

#### 접근법

좌측과 우측을 나누어 각각 합하고 그 결괏값을 비교하면 된다.

#### 소스 코드

> 소스 코드는 [01. 럭키 스트레이트.py](./03_알고리즘%20유형별%20기출문제/01.%20럭키%20스트레이트.py) 파일에서 확인 가능하다.

```Python
N: list[int] = [ int(number) for number in input() ]

left_sum: int = 0
right_sum: int = 0
for idx in range(len(N) // 2):
    left_sum += N[idx]
    right_sum += N[len(N) - idx - 1]

if left_sum == right_sum:
    print("LUCKY")

else:
    print("READY")
```

#### 시간 복잡도

주어진 N의 길이의 절반 만큼만 반복문을 작동하면 되기 때문에 시간 복잡도는 결국 O(N/2)이다.

그런데 상수 등은 전부 제외하니까 단순하게 O(N)으로 생각해도 될 것 같다.

### 02. 문자열 재정렬

#### 접근법

반복문을 문자열 S의 길이 N만큼 작동하며 `isnumeric()` 내장함수를 통해 만약 숫자일 경우 누적합을 구하고 아닐 경우 문자이기 때문에 새로운 문자에 이어 붙인다.

이후 `sorted()` 내장함수를 사용하 문자열을 오름차순 정렬하고 그 뒤에 누적합을 `str()` 내장함수를 사용해 문자열로 변경하여 이어 붙이면 된다.

이때 유의할 점은 `sorted()` 내장함수의 반환 자료형이 리스트이기 때문에 `join()` 내장함수를 사용하여 그 반환값을 문자열로 만들어줘야 한다는 것이다.

#### 소스 코드

> 소스 코드는 [02. 문자열 재정렬.py](./03_알고리즘%20유형별%20기출문제/02.%20문자열%20재정렬.py) 파일에서 확인 가능하다.

```Python
S: str = input()

only_characters: str = ""
cumulative_number: int = 0
for character in S:
    if character.isnumeric():
        cumulative_number += int(character)

    else:
        only_characters += character

answer = "".join(sorted(only_characters)) + str(cumulative_number)
print(answer)
```

#### 시간 복잡도

`sorted()` 내장함수의 시간 복잡도가 O(NlogN)이기 때문에 결국 시간 복잡도는 O(NlogN)이다.

### 03. 문자열 압축

#### 접근법

처음에는 그리디를 풀듯 접근했다. 그래서 첫 문자와 동일한 문자를 만나기 바로 직전까지로 생각했었는데 이 경우 `"aababa"` 같은 테스트 케이스를 통과하지 못한다.

그래서 단순히 완전 탐색으로 문자열 길이의 절반까지 반복문을 돌며 내부에 중첩 반복문으로 문자열 길이의 절반 이하까지의 정수를 `range()` 내장함수의 건너뛰기 값으로 사용했다.

이때 이전 문자열과 현재 문자열이 같은 경우 개수를 늘리고 다른 경우 새로운 문자열이 등장한 것이기 때문에 이전 문자열과 함께 그 개수가 2 이상이면 문자열에 함께 더해준다.

마지막에 남은 문자열과 그 개수가 2 이상이면 더해주고 이때 그 길이가 이전 압축에 대한 길이보다 작을 경우 그것을 사용하여 가장 작은 값을 반환하면 된다.

#### 소스 코드

> 소스 코드는 [03. 문자열 압축.py](./03_알고리즘%20유형별%20기출문제/03.%20문자열%20압축.py) 파일에서 확인 가능하다.

```Python
s: str = input()

answer: int = len(s)
for jump_idx in range(1, (len(s) // 2) + 1):
    count: int = 0
    result_string: str = ""
    previous_string: str = s[:jump_idx]
    for idx in range(0, len(s), jump_idx):
        target_string: str = s[idx:idx+jump_idx]

        if target_string == previous_string:
            count += 1
        
        else:
            result_string += previous_string
            if count != 1:
                result_string += str(count)
            
            count = 1
            previous_string = target_string
    
    result_string += previous_string
    if count != 1:
        result_string += str(count)
    
    if answer > len(result_string):
        answer = len(result_string)

print(answer)
```

#### 시간 복잡도

시간 복잡도는 O(N^2)이다.

### 04. 자물쇠와 열쇠

#### 접근법

기본적으로 `key[M-1][M-1]` 요소의 값과 `lock[0][0]` 값을 비교하면서 반복문을 수행해야 하기 때문에 상하좌우에 `M-1`개 만큼의 배열이 추가된 새로운 자물쇠 배열을 만들어서 문제를 풀 수 있다.

이렇게 새로운 배열이 만들어졌을 때 서로 다른 크기의 2차원 배열에 대한 비교를 어떻게 반복문을 통해 가능할지 구현하는데 쉽지 않았으며 추가로 최종적으로 자물쇠가 전부 요구사항에 맞게 열렸는지 확인할 때 돌기와 돌기가 만난 경우에 대한 처리를 해주지 못해서 몇 개의 테스트 케이스를 통과하지 못했었다.

2차원 배열을 90도로 회전할 때 기존 `array[x][y]` 값은 `array[y][length-1-x]` 와 같다는 공식을 잊지 말아야겠다.

#### 소스 코드

> 소스 코드는 [04. 자물쇠와 열쇠.py](./03_알고리즘%20유형별%20기출문제/04.%20자물쇠와%20열쇠.py) 파일에서 확인 가능하다.

```Python
def validate_lock(M: int, N: int, new_lock: list[list[int]]) -> bool:
    for i in range(N):
        for j in range(N):
            if new_lock[M-1+i][M-1+j] != 1:
                return False

    return True


def rotate(key: list[list[int]]) -> list[list[int]]:
    temp: list[list[int]] = [ [0] * len(key) for _ in range(len(key)) ]
    for i in range(len(key)):
        for j in range(len(key)):
            temp[i][j] = key[j][len(key)-1-i]

    return temp


def solution(key: list[list[int]], lock: list[list[int]]) -> bool:
    M: int = len(key)
    N: int = len(lock)
    new_lock: list[list[int]] = [
        [0] * ((M-1)*2+N) for _ in range((M-1)*2+N)
    ]

    for i in range(N):
        for j in range(N):
            new_lock[M-1+i][M-1+j] = lock[i][j]
    
    answer: bool = False
    for _ in range(4):
        for x in range((M-1)+N):
            for y in range((M-1)+N):
                for i in range(M):
                    for j in range(M):
                        new_lock[x+i][y+j] += key[i][j]

                if validate_lock(M, N, new_lock):
                    return True
                
                else:
                    for i in range(M):
                        for j in range(M):
                            new_lock[x+i][y+j] -= key[i][j]

        key = rotate(key)

    return answer
```

#### 시간 복잡도

시간 복잡도를 구하는 게 조금 무의미한 문제라 생각은 되는데 M은 무조건 N보다 작거나 같기 때문에 최악의 경우 M과 N의 크기가 같을 때 반복문이 총 4번 중첩되기 때문에 시간 복잡도는 O(N^4)이라 할 수 있다.

#### 기타

2차원 배열을 각각 90도, 180도, 270도를 회전하는 함수는 각각 아래와 같다.

```Python
def rotate_90(array: list[list[int]]) -> list[list[int]]:
    x_length: int = len(array)
    y_length: int = len(array[0])

    temp: list[list] = [
        [0] * x_length for _ in range(y_length)
    ]
    for i in range(x_length):
        for j in range(y_length):
            temp[i][j] = array[j][x_length-1-i]

    return temp


def rotate_180(array: list[list[int]]) -> list[list[int]]:
    x_length: int = len(array)
    y_length: int = len(array[0])

    temp: list[list] = [
        [0] * x_length for _ in range(y_length)
    ]
    for i in range(x_length):
        for j in range(y_length):
            temp[i][j] = array[x_length-1-i][y_length-1-j]

    return temp


def rotate_270(array: list[list[int]]) -> list[list[int]]:
    x_length: int = len(array)
    y_length: int = len(array[0])

    temp: list[list] = [
        [0] * x_length for _ in range(y_length)
    ]
    for i in range(x_length):
        for j in range(y_length):
            temp[i][j] = array[y_length-1-j][i]

    return temp    
```

### 05. 뱀

#### 접근법

이전에 풀었던 [게임 개발](#02-게임-개발) 문제와 유사하다.

방문한 위치에 대한 정보를 저장하는 배열을 만들고 현재 위치 정보를 계속 저장해나가는데 만약 목표 위치에 사과가 있을 경우 배열에 가장 처음 들어왔던 정보부터 제거하면 된다.

#### 소스 코드

> 소스 코드는 [05. 뱀.py](./03_알고리즘%20유형별%20기출문제/05.%20뱀.py) 파일에서 확인 가능하다.

```Python
N: int = int(input())
map_info: list[int] = [ [0] * N for _ in range(N) ]
for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    map_info[x-1][y-1] += 1

move_info: dict[int, str] = {}
for _ in range(int(input())):
    time, direction = input().split()
    move_info[int(time)] = direction

visited_info: list = []
moved_measure: list[tuple(int, int)] = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]

current_x: int = 0
current_y: int = 0
current_direction: int = 0

answer: int = 0
while True:
    answer += 1
    x_destination = current_x + moved_measure[current_direction][0]
    y_destination = current_y + moved_measure[current_direction][1]

    if (x_destination > (N-1)) or (y_destination > (N-1)) or \
        (x_destination < 0) or (y_destination < 0):
        break
    
    elif (x_destination, y_destination) in visited_info:
        break

    else:
        visited_info.append((current_x, current_y))
        current_x, current_y = x_destination, y_destination

        if map_info[x_destination][y_destination] == 1:
            map_info[x_destination][y_destination] = 0

        else:
            visited_info.pop(0)

    if answer in move_info.keys():
        if move_info[answer] == 'L':
            current_direction -= 1
            if current_direction == -1:
                current_direction = 3

        else:
            current_direction += 1
            if current_direction == 4:
                current_direction = 0

print(answer)
```

#### 시간 복잡도

최악의 경우 보드의 크기인 N을 전부 다 도는 경우이기 때문에 시간 복잡도는 O(N^2)이다.

### 06. 기둥과 보 설치

#### 접근법

처음에 전체 좌표가 존재하는 2차원 배열을 만들고 기둥과 보를 설치할 때마다 각 구조에 맞게 해당 배열에 값을 입력했다.

이때 `validate_strucutre` 라는 함수를 따로 만들어 해당 기둥과 보를 설치 가능한지, 혹은 삭제 가능한지 확인했는데 이때 문제는 전체 구조가 유효한지 여부를 판단한 것이 아닌 해당 설치 또는 삭제의 대상이 되는 기둥과 보의 설치 이후 좌표에 대한 부분만 유효성 검사를 진행했다는 점이다.

그래서 문제를 해결하지 못해서 정답을 확인한 결과 전체 배열에 대한 유효성 검사를 진행하는 게 접근 방법이었다.

#### 소스 코드

> 소스 코드는 [06. 기둥과 보 설치.py](./03_알고리즘%20유형별%20기출문제/06.%20기둥과%20보%20설치.py) 파일에서 확인 가능하다.

```Python
def validate_structure(answer: list[list[int]]) -> bool:
    for x, y, structure in answer:
        if structure == 0:
            if y == 0:
                pass
            
            elif [x, y-1, 0] in answer:
                pass
            
            elif [x-1, y, 1] in answer:
                pass
            
            elif [x, y, 1] in answer:
                pass
            
            else:
                return False
            
        else:
            if [x, y-1, 0] in answer:
                pass
            
            elif [x+1, y-1, 0] in answer:
                pass
            
            elif ([x-1, y, 1] in answer) and ([x+1, y, 1] in answer):
                pass
            
            else:
                return False
    
    return True


def solution(n: int, build_frame: list[list[int]]) -> list[list[int]]:
    answer: list[list[int]] = []
    
    for x, y, structure, work in build_frame:
        if work == 0:
            answer.remove([x, y, structure])
            if not validate_structure(answer):
                answer.append([x, y, structure])
        
        else:
            answer.append([x, y, structure])
            if not validate_structure(answer):
                answer.remove([x, y, structure])
    
    return sorted(answer)
```

#### 시간 복잡도

시간 복잡도의 경우 주어진 배열의 크기인 N만큼 -내부 유효성 검사에서의 `in` 연산을 포함하여- 총 세 번의 반복문을 수행해야 하기 때문에 O(N^3)이다.

### 07. 치킨 배달

#### 접근법

#### 소스 코드

```Python

```

#### 시간 복잡도

### 08. 외벽 점검

#### 접근법

#### 소스 코드

```Python

```

#### 시간 복잡도
