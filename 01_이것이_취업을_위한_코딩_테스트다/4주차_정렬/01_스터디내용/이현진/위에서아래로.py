from re import I


#정렬할 데이터의 개수가 500개 이하로 적고,
#수의 범위 또한 100,000 이하로 적으므로 정렬 라이브러리 사용
#내림차순에 대한 구현은 reverse 속성을 파라미터로 하여 구현

#입력
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

#정렬
array.sort(reverse=True)

#출력
for i in range(n):
    print(array[i], end=" ")