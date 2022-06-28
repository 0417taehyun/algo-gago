n = map(int, input().split()) #총 N명
m = list(map(int, input().split())) #N명의 각 공포도

#접근 방식: 정렬 후 공포도가 높은 사람부터 순서대로 묶어버리기 
#-> 최대라서 가능 최소면 정렬 후 공포도가 높은 사람을 기준으로 리스트 뒤에서 부터 묶어버리기

m.sort()
group = 0
fear = 0
for i in m:
    fear += 1
    if fear >= i:
        group += 1
        fear = 0

    




