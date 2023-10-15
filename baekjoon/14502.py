# pypy3

import sys 
import copy
from collections import deque
input = sys.stdin.readline


def bfs():
    virus_test = [row[:] for row in virus]  # 시간 down
    # virus_test = copy.deepcopy(virus)
    queue = deque()
    for i in range(n):
        for j in range(m):
            if virus_test[i][j] == 2:
                queue.append((i, j))
    

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if virus_test[nx][ny] == 0:
                virus_test[nx][ny] = 2
                queue.append((nx, ny))
    
    cnt = 0
    for i in range(n):
        cnt += virus_test[i].count(0)
    
    global res
    res = max(res, cnt)



def make_wall(k):
    global res
    if k == 3:
        bfs()
        return 
    
    for i in range(n):
        for j in range(m):
            if virus[i][j] == 0:
                virus[i][j] = 1
                make_wall(k + 1)
                virus[i][j] = 0


n, m = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
virus = []
res = 0

for i in range(n):
    virus.append(list(map(int, input().split())))

make_wall(0)
print(res)