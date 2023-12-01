from collections import deque

N, K = map(int, input().split())

visited = [-1 for _ in range(100001)]
visited[N] = 0

queue = deque()
queue.append(N)

while queue:
    n = queue.popleft()

    if n == K:
        print(visited[n])
        break
    if 0 <= n - 1 < 100001 and visited[n - 1] == -1:
        visited[n - 1] = visited[n] + 1
        queue.append(n - 1)
    if 0 < n * 2 < 100001 and visited[n * 2] == -1:
        visited[n * 2] = visited[n]
        queue.appendleft(n * 2)
    if 0 <= n + 1 < 100001 and visited[n + 1] == -1:
        visited[n + 1] = visited[n] + 1
        queue.append(n + 1)
    
