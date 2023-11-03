from collections import deque
import sys
input = sys.stdin.readline


def tree(N, graph):
    queue = deque([1])
    ans = [0] * (N + 1)

    while queue:
        p = queue.popleft()

        for c in graph[p]:
            if ans[c] == 0 and c != 1:
                ans[c] = p
                queue.append(c)
    
    for i in range(2, N + 1):
        print(ans[i])


N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

tree(N, graph)