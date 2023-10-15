import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))


for i in range(1, N):
    num[i] += num[i - 1]

cnt = 0
if num[0] == M:
    cnt += 1 

for i in range(1, N):
    if num[i] == M:
        cnt += 1
    for j in range(i - 1, -1, -1):
        s = num[i] - num[j]
        if s == M:
            
            cnt += 1
print(cnt)


'''
시간 초과
for i in range(N + 1):
    for j in range(i, N + 1):
        if sum(num[i:j]) == M:   
            cnt += 1

print(cnt)
'''
