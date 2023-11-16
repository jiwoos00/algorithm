def solv(arr, i, j, M):
    s = 0
    for l in range(j, j+M):
        for k in range(i, i+M):
            s += arr[k][l]
    return s



T = int(input())

for idx in range(T):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    
    max_s = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            max_s = max(max_s, solv(arr, i, j, M))
    print(f'#{idx+1} {max_s}')
