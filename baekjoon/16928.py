import sys 
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = [False] * 101
    visited[1] = True
    queue = deque()
    queue.append((1, 0))

    while queue:
        location, rolls = queue.popleft()
        if location == 100:
            return rolls
        for random in range(1, 7):
            next_location = location + random
            if next_location <= 100 and not visited[next_location]:
                visited[next_location] = True
                next_location = graph[next_location]
                queue.append((next_location, rolls + 1))
    

N, M = map(int, input().split())

graph = [i for i in range(101)]

for _ in range(N + M):
    x, y = map(int, input().split())
    graph[x] = y

print(bfs())

