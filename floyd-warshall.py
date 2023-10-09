INF = float('inf')

N = int(input()) # 노드
M = int(input()) # 간선

graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기자신으로 가는 경로는 0으로 초기화
for i in range(1, N + 1):
    graph[i][i] = 0

# 각 간선에 대한 정보 초기화
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 알고리즘 수행
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[a][b] == INF:
            print("INF", end = " ")
        else:
            print(graph[i][j], end = " ")
    print()
    