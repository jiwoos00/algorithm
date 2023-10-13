import math

def find_calendar(M, N, x, y):
    lcm = (M * N) // math.gcd(M, N) # 중국인의 나머지 정리

    k = x
    while k <= lcm:
        if (k - y) % N == 0:
            return k
        k += M
    return -1


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(find_calendar(M, N, x, y))