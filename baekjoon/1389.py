N, M = map(int, input().split())

INF = float('inf')
friend = [[INF] * N for _ in range(N)]

for i in range(N):
    friend[i][i] = 0

for _ in range(M):
    i, j = map(int, input().split())
    friend[i - 1][j - 1] = 1
    friend[j - 1][i - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            friend[i][j] = min(friend[i][j], friend[i][k] + friend[k][j])


ans = []
for i in range(N):
    ans.append(sum(friend[i]))
m = min(ans)

print(ans.index(m) + 1)

