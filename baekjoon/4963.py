# bfs

import sys
from collections import deque
input = sys.stdin.readline

# 상, 하, 좌, 우, 대각선
dx = [0, 0, -1, 1, -1, 1, -1, 1] 
dy = [-1, 1, 0, 0, -1, -1, 1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if land_sea_map[nx][ny] == 1:
                queue.append((nx, ny))
                land_sea_map[nx][ny] = 0


while True:
    w, h = map(int, input().split())
    land_sea_map = []
    if w == 0 and h == 0:
        break

    # map input
    for i in range(h):
        land_sea_map.append(list(map(int, input().split())))
    
    ans = 0
    # bfs
    for x in range(h):
        for y in range(w):
            if land_sea_map[x][y] == 1:
                bfs(x, y)
                ans += 1

    print(ans)
