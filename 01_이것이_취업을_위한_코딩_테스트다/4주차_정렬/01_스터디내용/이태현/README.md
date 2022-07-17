# 정렬

> 아래 내용은 [[ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 정렬](https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-sort) 글을 통해서도 확인 가능합니다.

## 목차

- [개념](#개념)
  - [선택 정렬](#선택-정렬)
  - [삽입 정렬](#삽입-정렬)
  - [퀵 정렬](#퀵-정렬)
  - [계수 정렬](#계수-정렬)
  - [파이썬의 정렬 라이브러리](#파이썬의-정렬-라이브러리)
- [실전문제](#실전문제)
  - [01. 위에서 아래로](#01-위에서-아래로)
  - [02. 성적이 낮은 순서로 학생 출력하기](#02-성적이-낮은-순서로-학생-출력하기)
  - [03. 두 배열의 원소 교체](#03-두-배열의-원소-교체)
- [기출문제](#기출문제)
  - [01. 국영수](#01-국영수)
  - [02. 안테나](#02-안테나)
  - [03. 실패율](#03-실패율)
  - [04. 카드 정렬하기](#04-카드-정렬하기)

## 개념

**정렬(Sorting)** 알고리즘은 데이터를 특정한 기준에 따라서 순서대로 나열한 것을 말한다.

정렬 알고리즘은 앞서 살펴보았던 [그리디](../../../1%EC%A3%BC%EC%B0%A8_%EA%B7%B8%EB%A6%AC%EB%94%94/01_%EC%8A%A4%ED%84%B0%EB%94%94%EB%82%B4%EC%9A%A9/%EC%9D%B4%ED%83%9C%ED%98%84/README.md) 알고리즘과 함께 출제되기도 하며 이후 살펴볼 **이진 탐색(Binary Search)** 개념에 필요한 지식이기 때문에 필히 알고 있어야 한다.

아래 정렬 종류는 모두 오름차순을 기준으로 하는데 내림차순의 경우 간단히 `reverse()` 메서드를 활용하면 되기 때문이다.

이때 해당 메서드의 시간 복잡도는 O(N)이다.

### 선택 정렬

반복문을 돌면서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 과정을 통해 정렬하는 알고리즘을 **선택 정렬(Selection Sort)** 알고리즘이라 한다.

0부터 9까지 10개의 정수가 무작위로 삽입된 배열을 선택 정렬 알고리즘을 활용해 정렬하면 아래와 같다.

```Python
def selection_sort() -> list[int]:
    cards: list[int] = [ 9, 5, 4, 0, 3, 2, 1, 7, 6, 8 ]

    for i in range(len(cards)):
        min_idx: int = i
        for j in range(i+1, len(cards)):
            if cards[min_idx] > cards[j]:
                min_idx = j

        cards[i], cards[min_idx] = cards[min_idx], cards[i]

    return cards # > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

이때 선택 정렬의 시간 복잡도는 중첩된 반복문을 수행해야 하기 때문에 주어진 배열의 길이가 N이라 할 때 O(N^2)이다.

### 삽입 정렬

**삽입 정렬(Insertion Sort)** 알고리즘은 선택 정렬과 달리 필요할 때만 위치를 바꾸기 때문에 훨씬 효율적이다.

선택 정렬은 현재 데이터의 상태와 상관없이 무조건 모든 원소를 비교하고 위치를 바꾸기 때문이다.

따라서 삽입 정렬은 데이터가 거의 정렬되어 있을 때 효율적이다.

0부터 9까지 10개의 정수가 무작위로 삽입된 배열을 선택 정렬 알고리즘을 활용해 정렬하면 아래와 같다.

기준이 되는 요소를 기준으로 좌측 방향으로 거꾸로 이동하면서 하나씩 비교해서 만약 기준이 되는 요소의 값이 비교 대상보다 작을 경우 두 위치를 바꿔주면 된다.

이때 알아두면 좋은 점은 비교 대상이 되는 요소의 좌측에 위치한 모든 요소는 이미 오름차순 정렬이 되어 있다는 점이다.

```Python
def insertion_sort() -> list[int]:
    cards: list[int] = [ 9, 5, 4, 0, 3, 2, 1, 7, 6, 8 ]

    for i in range(1, len(cards)):
        for j in range(i, 0, -1):
            if cards[j] < cards[j-1]:
                cards[j], cards[j-1] = cards[j-1], cards[j]

            else:
                break

    return cards # > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

삽입 정렬 또한 선택 정렬과 마찬가지로 중첩된 반복문을 수행해야 하기 때문에 주어진 배열의 길이가 N이라 할 때 시간 복잡도는 O(N^2)이다.

그러나 최선의 경우, 다시 말해 앞서 언급한 것처럼 데이터가 거의 정렬되어 있는 최선의 경우 시간 복잡도는 O(N)이다.

### 퀵 정렬

**퀵 정렬(Quick Sort)** 알고리즘은 기준을 설정한 다음 큰 수와 작은 수를 교환하는 방식으로 작동하는 알고리즘이다.

이때 그 기준이 되는 수를 피벗(Pivot)이라 하는데 피벗을 어떻게 설정하는 지에 따라서 퀵 정렬이 세부적으로 나뉜다.

여기서는 가장 대표적인 분할 방식인 호어 분할(Hoare Partition) 방식을 기준으로 퀵 정렬을 알아보고자 한다.

호어 분할의 경우 피벗을 기준으로 좌측에는 피벗보다 작은 데이터를, 우측에는 피벗보다 큰 데이터를 위치하게 한다.

이러한 작업을 분할(Divide) 또는 파티션(Partition)이라 한다.

```Python

```

퀵 정렬의 평균 시간 복잡도는 주어진 배열의 길이가 N이라 할 때 O(NlogN)이지만 이미 데이터가 정렬되어 있는 최악의 경우 시간 복잡도는 O(N^2)이다.

### 계수 정렬

**계수 정렬(Count Sort)** 알고리즘은 데이터의 크기 범위가 제한 되어 정수 형태로 표현할 수 있지만 매우 빠른 정렬 알고리즘이다.

일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적이다.

가장 큰 수까지 담길 수 있게 배열을 만든 뒤 해당 인덱스 번호를 활용해 수의 등장 횟수를 증가시키는 방식으로 작동하기 때문이다.

따라서 데이터가 0과 999,999처럼 단 두 개의 수만 존재하는데 그 차이가 무수히 클 경우 정작 정렬해야 하는 대상의 수는 두 개이지만 이를 위해 배열의 길이가 1,000,000이 되어야 하기 때문에 공간 복잡도에 있어서 매우 비효율적이다.

0부터 9까지 10개의 정수가 무작위로 삽입된 배열을 선택 정렬 알고리즘을 활용해 정렬하면 아래와 같다.

```Python
def count_sort() -> list[int]:
    cards: list[int] = [ 9, 5, 4, 0, 3, 2, 1, 7, 6, 8 ]

    count: list[0] = [ 0 for _ in range(max(cards) + 1) ]
    for card in cards:
        count[card] += 1

    return [ card for card, count in enumerate(count) if count > 0 ] # > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

계수 정렬의 시간 복잡도는 데이터의 개수가 N, 데이터 중 최대값이 K일 때 O(N + K)이다.

### 파이썬의 정렬 라이브러리

파이썬에서는 `sorted()` 내장함수 또는 배열의 내장 메서드인 `sort()` 를 사용해서 정렬할 수 있다.

이때 매개변수 `key` 또는 `reverse` 의 값을 적절히 활용하여 정렬의 기준을 설정하거나 오름차순 또는 내림차순 여부를 결정할 수 있다.

이 내장함수 또는 내장 메서드의 시간 복잡도는 주어진 배열의 길이가 N이라 할 때 O(NlogN)이다.

### 알고리즘 출제 방향성

정렬 알고리즘이 사용되는 경우는 일반적으로 아래와 같이 세 가지 문제 유형이다.

#### 1. 정렬 라이브러리로 풀 수 있는 문제

단순히 정렬 기법을 알고 있는지 물어보는 문제로 기본 정렬 라이브러리 사용법만 알고 있어도 충분하다.

#### 2. 정렬 알고리즘의 원리에 대해서 물어보는 문제

앞서 살펴보았던 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고 있어야 문제를 풀 수 있다.

#### 3. 더 빠른 정렬이 필요한 문제

퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며 계수 정렬 등의 다른 정렬 알고리즘을 이용하거나 문제에서 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다.

## 실전문제

### 01. 위에서 아래로

#### 접근법

`sorted()` 내장함수를 활용해서 N개의 수를 내림차순 정렬하고 출력하면 된다.

#### 소스 코드

> 소스 코드는 [01. 위에서 아래로.py](./02_%EC%8B%A4%EC%A0%84%20%EB%AC%B8%EC%A0%9C/01.%20%EC%9C%84%EC%97%90%EC%84%9C%20%EC%95%84%EB%9E%98%EB%A1%9C.py) 파일에서도 확인 가능합니다.

```Python
N: int = int(input())
numbers: list[int] = [ int(input()) for _ in range(N) ]

for number in sorted(numbers, reverse=True):
    print(number, end=' ')
```

#### 시간 복잡도

`sorted()` 내장함수를 사용했기 때문에 시간 복잡도는 O(NlogN)이다.

### 02. 성적이 낮은 순서로 학생 출력하기

#### 접근법

학생의 이름을 키로 하고 성적을 값으로 하는 해시 테이블을 하나 만들고 `sorted()` 내장함수를 사용해서 성적을 기준으로 오름차순 정렬하면 된다.

#### 소스 코드

> 소스 코드는 [02. 성적이 낮은 순서로 학생 출력하기](./02_%EC%8B%A4%EC%A0%84%20%EB%AC%B8%EC%A0%9C/02.%20%EC%84%B1%EC%A0%81%EC%9D%B4%20%EB%82%AE%EC%9D%80%20%EC%88%9C%EC%84%9C%EB%A1%9C%20%ED%95%99%EC%83%9D%20%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0.py) 파일에서도 확인 가능합니다.

```Python
N: int = int(input())
students: dict[str, int] = {}
for _ in range(N):
    name, score = input().split()
    students[name] = int(score)

for name, _ in sorted(students.items(), key=lambda x: x[1]):
    print(name, end=' ')
```

#### 시간 복잡도

`sorted()` 내장함수를 사용했기 때문에 시간 복잡도는 O(NlogN)이다.

### 03. 두 배열의 원소 교체

#### 접근법

A 배열은 오름차순, B 배열은 내림차순으로 정렬한 다음 만약 A 배열의 요소가 B 배열의 요소보다 작을 경우 해당 요소를 서로 바꿔주면 된다.

이때 바꿀 수 있는 횟수는 주어진 K만큼이다.

#### 소스 코드

> 소스 코드는 [03. 두 배열의 원소 교체](./02_%EC%8B%A4%EC%A0%84%20%EB%AC%B8%EC%A0%9C/03.%20%EB%91%90%20%EB%B0%B0%EC%97%B4%EC%9D%98%20%EC%9B%90%EC%86%8C%20%EA%B5%90%EC%B2%B4.py) 파일에서도 확인 가능합니다.

```Python
N, K = map(int, input().split())
A: list[int] = list(map(int, input().split()))
B: list[int] = list(map(int, input().split()))

answer: int = 0
for a_num, b_num in zip(sorted(A), sorted(B, reverse=True)):
    if K > 0:
        if a_num < b_num:
            answer += b_num

        else:
            answer += a_num

        K -= 1

    else:
        answer += a_num

print(answer)
```

#### 시간 복잡도

`sorted()` 내장함수를 사용했기 때문에 시간 복잡도는 O(NlogN)이다.

## 기출문제

### 01. 국영수

#### 접근법

`sorted()` 내장함수를 사용해서 국어 점수 내림차순, 영어 점수 오름차순, 수학 점수 내림차순, 끝으로 이름 사전 순으로 정렬하면 된다.

#### 소스 코드

> 소스 코드는 [01. 국영수.py](./03_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%9C%A0%ED%98%95%EB%B3%84%20%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C/01.%20%EA%B5%AD%EC%98%81%EC%88%98.py) 파일에서도 확인 가능합니다.

```Python
N: int = int(input())

students: dict[str, list[int]] = {}
for _ in range(N):
    name, korean, enlgish, math = input().split()
    students[name] = [int(korean), int(enlgish), int(math)]

students = sorted(
    students.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0])
)
for name, _ in students:
    print(name)
```

#### 시간 복잡도

`sorted()` 내장함수를 사용했기 때문에 시간 복잡도는 O(NlogN)이다.

### 02. 안테나

#### 접근법

중간에 위치한 집이 모든 집까지의 거리의 총합이 가장 작다.

따라서 오름차순으로 집의 위치를 정렬한 다음 그 중간값을 출력한다.

#### 소스 코드

> 소스 코드는 [02. 안테나.py](./03_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%9C%A0%ED%98%95%EB%B3%84%20%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C/02.%20%EC%95%88%ED%85%8C%EB%82%98.py) 파일에서도 확인 가능합니다.

```Python
N: int = int(input())
houses: list[int] = list(map(int, input().split()))

houses.sort()
if N % 2:
    print(houses[N//2])
else:
    print(houses[(N//2)-1])
```

#### 시간 복잡도

배열 객체의 `sort()` 메서드를 사용했기 때문에 시간 복잡도는 O(NlogN)이다.

### 03. 실패율

#### 접근법

스테이지를 키로 하고 실패율을 값으로 하는 해시 테이블을 하나 만들어 `stages` 배열을 오름차순 정렬한 뒤 첫 번째 요소부터 반복문을 돌면서 각 스테이지의 실패율을 계산해 값으로 입력한다.

이때 전체 사용자 수는 주어진 `stages` 배열의 길이와 같은데 동일한 요소에 대한 반복 횟수에 따라 그 사용자 수를 계속해서 빼줘야 한다.

해시 테이블을 실패율을 기준으로 내림차순, 스테이지를 기준으로 오름차순 정렬한 뒤 해당 배열을 반환하면 된다.

#### 소스 코드

> 소스 코드는 [03. 실패율.py](./03_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%9C%A0%ED%98%95%EB%B3%84%20%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C/03.%20%EC%8B%A4%ED%8C%A8%EC%9C%A8.py) 파일에서도 확인 가능합니다.

```Python
def soltuion(N: int, stages: list[int]) -> list[int]:
    total_users: int = len(stages)
    failures: dict[int, int] = { stage: 0 for stage in range(1, N+1) }

    stages.sort()
    if not stages[0] > N:
        count: int = 0
        previous_stage: int = stages[0]

        for stage in stages:
            if stage > N:
                break

            elif stage == previous_stage:
                count += 1

            else:
                failures[previous_stage] = count / total_users

                previous_stage = stage
                total_users -= count
                count = 1

        failures[previous_stage] = count / total_users

    answer = [
        stage for stage, failure
        in sorted(failures.items(), key=lambda x: (-x[1], x[0]))
    ]

    return answer
```

#### 시간 복잡도

`sorted()` 내장함수를 사용했기 때문에 시간 복잡도는 O(NlogN)이다.

### 04. 카드 정렬하기

#### 접근법

#### 소스 코드

> 소스 코드는 []() 파일에서도 확인 가능합니다.

```Python

```

#### 시간 복잡도
