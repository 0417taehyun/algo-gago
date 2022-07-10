from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

#상하좌우로 움직일 것에 대한 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#방문노드를 처리하기 위한 리스트
visited = [[False] for _ in range(m)] * n
#거리를 기록하기 위한 리스트
distance = [[0] for _ in range(m)] * n

def bfs(graph, visited, x, y):
  queue = deque()
  queue.append((x,y)) #큐에 시작좌표 삽입
  while queue:
    x,y = queue.popleft() #현재 위치 좌표
    for i in range(4): #상하좌우 방향으로 이동
      nx = x + dx[i]
      ny = y + dy[i]
      if graph[nx][ny] == 1 and visited[nx][ny] == False: #괴물이 없는 부분만 카운팅
        distance[x][y] += 1
      else:
        continue

bfs(graph, visited, 0, 0)