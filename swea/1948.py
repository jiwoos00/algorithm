month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())

for i in range(T):
    m1, d1, m2, d2 = map(int, input().split())
    ans = 0

    if m1 == m2:
        ans = d2 - d1
    else:
        ans += month[m1] - d1
        ans += d2
        for k in range(m1+1, m2):
            ans += month[k]

    print(f'#{i+1} {ans+1}')