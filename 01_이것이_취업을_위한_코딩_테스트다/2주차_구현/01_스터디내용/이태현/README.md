# 구현(Implementation)

## 목차

- [개념](#개념)

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

#### 소스코드

> 소스코드는 [01. 상하좌우.py](./01_%EC%98%88%EC%A0%9C/01.%20%EC%83%81%ED%95%98%EC%A2%8C%EC%9A%B0.py) 파일에서 확인 가능하다.

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

#### 소스코드

> 소스코드는 [02. 시각.py](./01_%EC%98%88%EC%A0%9C/02.%20%EC%8B%9C%EA%B0%81.py) 파일에서 확인 가능하다.

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

#### 소스코드

```Python

```

#### 시간 복잡도

### 02. 게임 개발

#### 접근법

#### 소스코드

```Python

```

#### 시간 복잡도

## 기출문제

### 01. 럭키 스트레이트

### 02. 문자열 재정렬

### 03. 문자열 압축

### 04. 자물쇠와 열쇠

### 05. 뱀

### 06. 기둥과 보 설치
