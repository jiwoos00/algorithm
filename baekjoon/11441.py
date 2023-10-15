import sys
input = sys.stdin.readline

N = int(input())
num = [0] + list(map(int, input().split()))

for i in range(1, N + 1):
    num[i] += num[i - 1]

M = int(input())

for _ in range(M):
    i, j = map(int, input().split())
    print(num[j] - num[i-1])


#  시간초과
# for _ in range(M):
#     i, j = map(int, input().split())
#     print(sum(num[i-1:j]))