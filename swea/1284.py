T = int(input())

for idx in range(T):
    P, Q, R, S, W = map(int, input().split())
    a = W * P
    b = Q
    if R < W:
        b += (W - R) * S
    

    print(f'#{idx+1} {min(a, b)}')