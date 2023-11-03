arr1 = []
arr2 = []

N, M = map(int, input().split())
for _ in range(N):
    arr1.append(list(map(int,input().split())))

M, K = map(int, input().split())
for _ in range(M):
    arr2.append(list(map(int, input().split())))


ans = [[0] * K for _ in range(N)]
for i in range(N):
    for k in range(K):
            for j in range(M):
                ans[i][k] += (arr1[i][j] * arr2[j][k])

for i in ans:
     print(' '.join(map(str, i)))
        


