# bfs
import sys
from collections import deque
input = sys.stdin.readline


def DSLR(A, B):
    queue = deque()
    visited = [False] * 10001
    queue.append((A, ''))

    while queue:
        num, cmd = queue.popleft()

        if num == B:
            return cmd
        
        d = (num * 2) % 10000
        if not visited[d]:
            visited[d] = True
            queue.append((d, cmd + 'D'))

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            queue.append((s, cmd + 'S'))

        # 왼쪽 회전
        l = num // 1000 + ((num % 1000) * 10)
        if not visited[l]:
            visited[l] = True
            queue.append((l, cmd + 'L'))
        
        # 오른쪽 회전
        r = num // 10 + ((num % 10) * 1000)
        if not visited[r]:
            visited[r] = True
            queue.append((r, cmd + 'R'))
    



T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(DSLR(A, B))