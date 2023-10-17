import itertools

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

# 치킨집 최대 M개 조합 생성
combinations = itertools.combinations(chickens, M)

# 도시의 치킨 거리 계산
def chicken_distance(house, selected_chicken):
    m = float('inf')
    for chicken in selected_chicken:
        distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
        m = min(m, distance)
    return m

# 도시의 치킨 거리 합
def sum_chicken_distance(selected_chicken):
    total = 0
    for house in houses:
        distance = chicken_distance(house, selected_chicken)
        total += distance
    return total

min_distance = float('inf')

# 모든 조합을 돌면서 최소 도시 치킨 거리 찾기
for combination in combinations:
    total_distance = sum_chicken_distance(combination)
    min_distance = min(min_distance, total_distance)

print(min_distance)






# import itertools

# N, M = map(int, input().split())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, input().split())))


# houses = []
# chicken_shop = []
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 2:
#             chicken_shop.append((i, j))
#         if graph[i][j] == 1:
#             houses.append((i, j))

# # 최대 치킨집 조합
# combinations = list(itertools.combinations(chicken_shop, M))


# res = float('inf')
# for combination in combinations:
#     total = 0
#     for house in houses:
#         min_distance = float('inf')
#         for chicken in combination:
#             distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
#             min_distance = min(distance, min_distance)
#         total += min_distance
#     res = min(total, res)
        
# print(res)


        
