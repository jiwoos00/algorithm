N, K = map(int, input().split())
a = []
arr = {}

for i in range(N):
    idx, g, s, b = map(int, input().split())
    arr[idx] = (g, s, b)

new_arr = sorted(arr.values(), key = lambda x:(-x[0], -x[1], -x[2]))
print(new_arr.index(arr[K]) + 1)


