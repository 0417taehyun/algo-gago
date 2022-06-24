# 그리디(Greedy)

> 아래 내용은 [[ 알고리즘 ] 이것이 취업을 위한 코딩 테스트다 with 파이썬 : 그리디](https://velog.io/@dev_taehyun/algorithm-this-is-coding-test-for-employment-greedy) 글을 통해서도 확인 가능합니다.

## 목차

- [개념](#개념)
- [예제](#예제)
- [3-1. 거스름돈](#3-1-거스름돈)
- [실전문제](#실전문제)
  - [01. 큰 수의 법칙](#01-큰-수의-법칙)
  - [02. 숫자 카드 게임](#02-숫자-카드-게임)
  - [03. 1이 될 때까지](#03-1이-될-때까지)
- [기출문제](#기출문제)
  - [01. 모험가 길드](#01-모험가-길드)
  - [02. 곱하기 혹은 더하기](#02-곱하기-혹은-더하기)
  - [03. 문자열 뒤집기](#03-문자열-뒤집기)
  - [04. 만들 수 없는 금액](#04-만들-수-없는-금액)

## 개념

이름에서 알 수 있듯이 어떠한 문제가 있을 때 단순 무식하게, 탐욕적으로 문제를 푸는 알고리즘이다. 여기서 **탐욕적**이란 단어의 의미는 **현재 상황에서 지금 당장 좋은 것만 고르는 방법**을 의미하기 때문에 현재의 선택이 이후에 끼칠 영향에 대해서는 고민하지 않고 매 순간 가장 좋아 보이는 것만 선택한다.

기준에 따라 가장 좋은 것을 선택하는 알고리즘이기 때문에 문제에서 **정렬** 과 관련된 기준이 제시된다. 따라서 정렬 알고리즘과 짝을 이루어 출제되는 경우가 대다수다. 이외에도 다익스트라(Dijkstra) 알고리즘이나 크루스칼(Kruskal) 알고리즘 또한 그리디 알고리즘에 해당된다.

## 예제

### 3-1. 거스름돈

#### 문제

당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈은 N은 항상 10의 배수이다.

#### 접근법

가장 큰 수인 500원부터 크기가 큰 순서대로 최대한 많은 동전을 사용해야 결론적으로 거슬러 줘야 할 돈의 개수가 가장 적어진다. 따라서 500원부터 차례 대로 주어진 수 N원을 나누어 생긴 몫은 그 개수로 더하고 나머지는 다시 다음 동전으로 나누어 반복하면 된다.

#### 소스코드

> 소스코드는 [01. 거스름돈.py](./01_%EC%98%88%EC%A0%9C/01.%20%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88.py) 파일에서 확인 가능하다.

```Python
N: int = int(input())

answer: int = 0
coins: list[int] = [500, 100, 50, 10]
for coin in coins:
    answer += (N // coin)
    N %= coin

print(answer)
```

#### 시간 복잡도

동전의 수에 영향을 받기 때문에 해당 문제에서 주어진 동전의 개수는 4개라 O(4), 즉 상수 시간과 같다.

## 실전문제

### 01. 큰 수의 법칙

#### 접근법

가장 큰 수를 최대 반복할 수 있는 만큼 반복한 이후 그 다음으로 큰 수를 하나씩 섞어주면 된다. 따라서 내장함수 `sort()`를 사용해 내림차순 정렬한 뒤 배열의 첫 번째 요소와 두 번째 요소를 각각 변수에 할당한다.

결과적으로 가장 큰 수를 최대 K번 반복하고 그 다음 수 1번 반복하는 (K + 1) 개의 반복적인 형태로 구성되기 때문에 M을 해당 (K + 1) 수로 나누어 생긴 몫을 (K + 1)의 반복횟수, 나머지를 가장 큰 수의 반복 횟수로 가져가면 된다.

#### 소스코드

> 소스코드는 [01. 큰 수의 법칙.py](./02_%EC%8B%A4%EC%A0%84%20%EB%AC%B8%EC%A0%9C/01.%20%ED%81%B0%20%EC%88%98%EC%9D%98%20%EB%B2%95%EC%B9%99.py) 파일에서 확인 가능하다.

```Python
N, M, K = list(map(int, input().split(" ")))
numbers: list[int] = list(map(int, input().split(" ")))

numbers.sort(reverse=True)
largest_number: int = numbers[0]
second_number: int = numbers[1]

set_count = M // (K + 1)
remained_count = M % (K + 1)

answer: int = (
    (largest_number * K + second_number) * set_count
    +
    largest_number * remained_count
)

print(answer)
```

#### 시간 복잡도

내림차순 정렬을 수행하는 내장함수 `sort()`의 시간 복잡도가 O(NlogN)이기 때문에 결론적으로 O(NlogN)이다. 나머지 연산의 경우 인덱스를 통한 배열의 요소 조회 및 사칙 연산일 뿐이기 때문에 상수 시간이 걸린다.

### 02. 숫자 카드 게임

#### 접근법

이중 반복문을 돌면서 행마다 가장 작은 수를 구하고 그 중 가장 큰 수를 출력하면 된다.

#### 소스코드

> 소스코드는 [02. 숫자 카드 게임.py](./02_%EC%8B%A4%EC%A0%84%20%EB%AC%B8%EC%A0%9C/02.%20%EC%88%AB%EC%9E%90%20%EC%B9%B4%EB%93%9C%20%EA%B2%8C%EC%9E%84.py) 파일에서 확인 가능하다.

```Python
N, M = list(map(int, input().split()))

answer: int = 0
for _ in range(N):
    smallest_card: int = 10000
    for card in list(map(int, input().split())):
        if card < smallest_card:
            smallest_card = card

    if answer < smallest_card:
        answer = smallest_card

print(answer)
```

#### 시간 복잡도

N번 반복문이 도는 내부에 M번의 반복문이 추가적으로 돌기 때문에 시간 복잡도는 O(NM)이다.

### 03. 1이 될 때까지

#### 접근법

주어진 N이 K로 나누어 떨어질 때까지 1씩 빼다가 나누어 떨어지면 나누면 된다.

#### 소스코드

> 소스코드는 [03. 1이 될 때까지.py](./02_%EC%8B%A4%EC%A0%84%20%EB%AC%B8%EC%A0%9C/03.%201%EC%9D%B4%20%EB%90%A0%20%EB%95%8C%EA%B9%8C%EC%A7%80.py) 파일에서 확인 가능하다.

```Python
N, K = list(map(int, input().split()))

answer: int = 0
while N > 1:
    if not N % K:
        answer += 1
        N //= K

    else:
        answer += 1
        N -= 1

print(answer)
```

위와 같이 계산할 경우 주어진 입력 값의 범위 내에서는 상관 없지만 입력 값의 범위가 더 커지면 하나씩 빼기 때문에 느리게 작동한다.

따라서 아래 코드와 같이 하나씩 빼주던 경우의 수를 한번에 계산하여 조금 더 최적화 해줄 수 있다.

주어진 N 자체를 K로 나누고 그 나머지 몫과 함께 나누는 횟수까지 포함하여 N이 K보다 작아질 때까지 더하게 된다.

N이 K보다 작아지는 순간 더이상 K로 나눌 수 없다는 걸 의미하기 때문에 1이 되기 전까지의 수인 (N - 1) 만큼을 최종적으로 횟수에 더해준다.

```Python
N, K = list(map(int, input().split()))

answer: int = 0
while N >= K:
    answer += (N % K) + 1
    N //= K

answer += (N - 1)

print(answer)
```

#### 시간 복잡도

나눌 때마다 계산해야 할 경우의 수가 어림잡아 반씩 줄어들기 때문에 시간 복잡도는 O(logN)이다.

## 기출문제

### 01. 모험가 길드

#### 접근법

공포도의 경우 동일한 공포도 값이 배수로 존재해야 그룹이 하나씩 증가하게 된다.

예를 들어 공포도 값이 2일 경우 2인 모험가가 4명 있으면 그룹이 두 개가 만들어지는 것이다.

다른 공포도를 섞을 경우 해당 공포도보다 값이 적으면 상관 없지만 해당 공포도보다 값이 크면 결국 그 값에 맞춰 그룹을 만들어야 하기 때문에 동일한 공포도끼리 묶어 그 개수를 공포도로 나누었을 때의 정수 몫이 곧 모험가의 그룹 수에 더해져야 한다.

#### 소스코드

> 소스코드는 [01. 모험가 길드.py](./03_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%9C%A0%ED%98%95%EB%B3%84%20%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C/01.%20%EB%AA%A8%ED%97%98%EA%B0%80%20%EA%B8%B8%EB%93%9C.py) 파일에서 확인 가능하다.

```Python
from collections import defaultdict


N: int = int(input())
F: list(int) = list(map(int, input().split()))

fearnesses: dict[int, int] = defaultdict(int)
for fearness in F:
    fearnesses[fearness] += 1

answer: int = 0
for fearness, count in fearnesses.items():
    answer += (count // fearness)

print(answer)
```

#### 시간 복잡도

배열을 한번 돌면서 딕셔너리 자료형에 그 개수를 만드는 것과 마지막에 그 개수에 따라 모험가의 수를 구하는 것 자체가 동일한 수의 반복문을 수행하기 때문에 모험가의 수인 N만큼의 시간 복잡도인 O(N)이다.

### 02. 곱하기 혹은 더하기

#### 접근법

0과 1을 제외한 나머지 수는 곱해야 가장 큰 수가 될 수 있다.

따라서 인덱스 1번부터 반복문을 돌며 누적된 값이 0 또는 1이거나 요소 본인 자체가 0 또는 1일 경우 더하고 나머지는 곱하면 된다.

#### 소스코드

> 소스코드는 [02. 곱하기 혹은 더하기.py](./03_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%9C%A0%ED%98%95%EB%B3%84%20%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C/02.%20%EA%B3%B1%ED%95%98%EA%B8%B0%20%ED%98%B9%EC%9D%80%20%EB%8D%94%ED%95%98%EA%B8%B0.py) 파일에서 확인 가능하다.

```Python
S: str = input()

answer: int = int(S[0])
for idx in range(1, len(S)):
    if (answer <= 1) or (int(S[idx]) <= 1):
        answer += int(S[idx])
    else:
        answer *= int(S[idx])

print(answer)
```

#### 시간 복잡도

문자열 S의 길이 만큼 반복문을 수행하면 되기 때문에 시간 복잡도는 O(N)이다.

### 03. 문자열 뒤집기

#### 접근법

첫 시작 문자와 다를 때부터 개수를 세는데 이때 연속된 동일한 문자는 한번에 뒤집기 때문에 이전 수와 다를 경우만 변해야 한다.

#### 소스코드

> 소스코드는 [03. 문자열 뒤집기.py](./03_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%9C%A0%ED%98%95%EB%B3%84%20%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C/03.%20%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%92%A4%EC%A7%91%EA%B8%B0.py) 파일에서 확인 가능하다.

```Python
S: str = input()

answer: int = 0
first_num, previous_num = S[0], S[0]
for num in S:
    if (num != first_num) and (num != previous_num):
        previous_num = num
        answer += 1

    elif num != previous_num:
        previous_num = num

print(answer)
```

#### 시간 복잡도

문자열 S의 길이 만큼 반복문을 수행하면 되기 때문에 시간 복잡도는 O(N)이다.

### 04. 만들 수 없는 금액

#### 접근법

고민을 하다가 브루트 포스인 것 같은 방법 밖에 떠오르지 않아 우선은 그렇게 풀었다. 아마 시간초과가 될 것이다.

만들 수 있는 수의 조합을 구한 다음 그 개수를 세서 다시 1부터 만들 수 있는 가장 큰 수보다 하나 큰 값까지 반복문을 돌아 만약 해당 조합이 만들 수 없는 경우면 출력하는 방식으로 접근했다.

#### 소스코드

> 소스코드는 [04. 만들 수 없는 금액.py](./03_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%9C%A0%ED%98%95%EB%B3%84%20%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C/04.%20%EB%A7%8C%EB%93%A4%20%EC%88%98%20%EC%97%86%EB%8A%94%20%EA%B8%88%EC%95%A1.py) 파일에서 확인 가능하다.

```Python
N: int = int(input())
coins: list[int] = list(map(int, input().split()))

max_price: int = sum(coins)
possible_price: dict[int, int] = { number: 0 for number in range(1, max_price + 1) }

for i in range(len(coins)):
    for j in range(i + 1, len(coins) + 1):
        possible_price[sum(coins[i:j])] += 1

for price in range(1, max_price + 2):
    if not possible_price[price]:
        print(price)
        break
```

아래는 책에 나온 모범 답안이었다.

1부터 시작하는 목표값을 설정한 뒤 내림차순으로 정렬된 동전을 하나씩 더해서 만약에 해당 목표값이 동전보다 작을 경우 그 수를 만들 수 없는 것이기에 출력하고 반복문을 멈춘다.

예를 들어서 예시 입력값인 `[3, 2, 1, 1, 9]` 의 경우 내림차순 정렬하여 `[1, 1, 2, 3, 9]` 가 되고 `1` 부터 차례로 목표값인 `1` 과 비교하고 만약 목표값이 동전보다 작지 않을 경우 해당 동전을 목표값에 더하게 되는데 `3` 까지 더해진 직후인 목표값 `8` 이 다음 동전 `9` 보다 작기 때문에 `8` 보다 작은 동전은 존재하는 동전들로 만들 수 있다는 의미가 되고 그 다음부터는 `9` 이상이기 때문에 `8` 이 곧 만들 수 없는 최소가 된다.

목표값의 시작을 `1` 로 하기 때문에 주어진 동전의 차례 합보다 무조건적으로 하나씩 커져서 이를 비교하게 된다. 따라서 모든 합을 다 비교하더라도 결국 최대로 구할 수 있는 값보다 `1` 크기 때문에오류가 발생하지 않는다.

```Python
N: int = int(input())
coins: list[int] = list(map(int, input().split()))

coins.sort()
target: int = 1
for coin in coins:
    if target < coin:
        break

    target += coin

print(target)
```

#### 시간 복잡도

처음 생각한 접근법으로 문제를 풀 경우 시간 복잡도는 O(N^2)이다.

책에 나온 모범 답안으로 접근하여 문제를 풀 경우 주어진 N개의 동전 개수 만큼만 반복문을 수행하면 되기 때문에 O(N), 오름차순 정렬을 위해 사용한 내장함수 `sort()` 의 시간 복잡도가 O(NlogN)이기 때문에 결국 O(NlogN)이다.
