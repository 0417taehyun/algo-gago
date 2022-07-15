from collections import deque

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
while m:
  v1, v2 = map(int, input().split())
  graph[v1].append(v2)

visited = []*(n+1)
#각 노드에 대한 거리를 계산하기 위한 리스트
#우선 디폴트값을 -1로 초기화
distance = [-1]*(n+1) 

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  distance[start] += 1 #인접하는 노드가 있을 경우 +1 증가
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[v]:
        queue.append(i)
        visited[i] = True
        distance[i] += 1 #인접하는 노드가 있을 경우 +1 증가

bfs(graph, x, visited)
for i in graph[x]:
  if i == k:
    print(i, end=" ")