# 포인터 이용

import sys
input = sys.stdin.readline
m = 100000 # 최솟값


N, S = map(int, input().split())
num = list(map(int, input().split()))

start = 0
end = 0
cur_sum = 0


while True:
    if cur_sum >= S:
        m = min(m, end - start)
        cur_sum -= num[start]
        start += 1
    elif end == N:
        break
    else:
        cur_sum += num[end]
        end += 1

if m == 100000:
    print(0)
else:
    print(m)   