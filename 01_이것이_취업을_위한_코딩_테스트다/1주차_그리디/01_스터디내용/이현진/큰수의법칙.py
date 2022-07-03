'''
실전 2 큰 수의 법칙
첫째 줄에 N, M, K 입력
둘째 줄에 N개의 자연수 입력
K <= M
'''
#가장 큰 수와 두번째로 큰 수 도출
n,m,k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
fir = arr[n-1]
sec = arr[n-2]

#주어진 조건의 큰 수 도출
count = m//(k+1)*k #전체 연산의 횟수에서 K+1을 나눈 몫은 가장 큰 수와 두번째로 큰 수를 더한 수열의 반복횟수
count += m%(k+1) #전체 연산의 횟수에서 k+1을 나눈 나머지는 가장 큰 수를 더할 수 있는 횟수

max = count*fir
max += (m-count)*sec

print(max)