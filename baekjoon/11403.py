N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


ans = graph[:]

for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][b] == 1:
                continue
            if graph[a][k] and graph[k][b]:
                ans[a][b] = 1
          
for i in range(N):
    print(' '.join(map(str, ans[i])))