# bfs
from collections import deque

def bfs(x, y, h):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] > h and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
    

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

safe_zone_max = 0
m = max(map(max, graph))

for h in range(m + 1):
    visited = [[False] * N for _ in range(N)]
    safe_zone = 0

    for x in range(N):
        for y in range(N):
            if not visited[x][y] and graph[x][y] > h:
                bfs(x, y, h)
                safe_zone += 1
    
    safe_zone_max = max(safe_zone, safe_zone_max)

print(safe_zone_max)





# dfs
import sys
sys.setrecursionlimit(10 ** 8)
def dfs(x, y, h):
    visited[x][y] = True

    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if graph[nx][ny] > h and not visited[nx][ny]:
            dfs(nx, ny, h)
    

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

safe_zone_max = 0
m = max(map(max, graph))

for h in range(m + 1):
    visited = [[False] * N for _ in range(N)]
    safe_zone = 0

    for x in range(N):
        for y in range(N):
            if not visited[x][y] and graph[x][y] > h:
                dfs(x, y, h)
                safe_zone += 1
    
    safe_zone_max = max(safe_zone, safe_zone_max)

print(safe_zone_max)