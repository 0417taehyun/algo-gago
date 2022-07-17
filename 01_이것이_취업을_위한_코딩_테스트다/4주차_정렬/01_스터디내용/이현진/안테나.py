#입력
n = int(input())
houses = list(map(int, input().split()))

#정렬
houses.sort()
#안테나의 위치는 집의 거리 총합의 중간값
#즉, 집들이 거리순으로 정렬되어 있다면 해당 리스트의 중간 인덱스의 값이 정답
#이때, 집의 개수가 짝수라면 중간값이 2개가 될 수도 있으나 그 중 최소값이니 그대로
antena = (n-1)//2 

#출력
print(houses(antena))