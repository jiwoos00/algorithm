from itertools import permutations, combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr = (list(set(list(permutations(arr, M)))))
arr.sort()

for i in arr:
    print(' '.join(map(str, i)))
    