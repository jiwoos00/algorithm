import math

M = int(input())
N = int(input())

start = int(math.sqrt(M)) 
if start ** 2 < M:
    start += 1

arr = []
cnt = 0
while True:
    n = start ** 2
    if n > N:
        break
    start += 1
    arr.append(n)
    cnt += 1

if cnt == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
    