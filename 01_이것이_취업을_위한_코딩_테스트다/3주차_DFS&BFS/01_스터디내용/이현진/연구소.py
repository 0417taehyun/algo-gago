from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

#방문노드 리스트
visited = [False]*(n*m)
#안전한 영역 개수
safe = 0

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[v]:
        queue.append(i)
        visited[i] = True
        if i == 0:
          safe += 1