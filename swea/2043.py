P, K = map(int, input().split())

if P == K:
    print(0)
else:
    print(P - K + 1)