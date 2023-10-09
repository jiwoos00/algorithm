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
            if graph[a][k] and graph[k][b] :
                ans[a][b] = 1
          
for i in range(N):
    print(' '.join(map(str, ans[i])))

# INF = int(1e9)

# # 노드 개수 및 간선 개수
# n = int(input())
# m = int(input())

# # 2차원 리스트 초기화
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# # 자기 자신으로 가는 비용은 0으로 초기화
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0

# # 각 간선에 대한 정보 초기화
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c

# # 점화식에 따른 알고리즘 수행
# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# # 수행 결과 출력
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if graph[a][b] == INF:
#             print("INFINITY", end = ' ')
#         else:
#             print(graph[a][b], end = ' ')
#     print()