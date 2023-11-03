# V, E = map(int, input().split())
# K = int(input())

# distance = [float('inf')] * (V + 1)
# graph = [[] for _ in range(V + 1)]
# visited = [False] * (V + 1)

# for _ in range(V):
#     u, v, w = map(int, input().split())
#     graph[u].append(v, w)

# def get_smallest_node():
#     min_value = float('inf')
#     index = 0

#     for i in range(1, V + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index


# def dijkstra(K):
#     distance[K] = 0
#     visited[K] = True

#     for i in graph[K]:
#         distance[i[0]] = i[1]
    
#     for _ in range(V):
#         now = get_smallest_node()
#         visited[now] = True

#         for i in graph[now]:
#             cost = distance[now] 

import heapq

# 무한대를 나타내는 상수
INF = float('inf')

def dijkstra(graph, start):
    V = len(graph)
    distance = [INF] * V
    distance[start - 1] = 0

    pq = [(0, start)]

    while pq:
        dist, u = heapq.heappop(pq)

        if distance[u - 1] < dist:
            continue

        for v, w in graph[u - 1]:
            if distance[u - 1] + w < distance[v - 1]:
                distance[v - 1] = distance[u - 1] + w
                heapq.heappush(pq, (distance[v - 1], v))

    return distance

# 입력 받기
V, E = map(int, input().split())
start = int(input())

# 그래프 초기화
graph = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v, w))

# 다익스트라 알고리즘을 사용하여 최단 경로 계산
result = dijkstra(graph, start)

# 결과 출력
for dist in result:
    if dist == INF:
        print("INF")
    else:
        print(dist)
