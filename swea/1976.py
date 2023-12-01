T = int(input())

for i in range(T):
    h1, m1, h2, m2 = map(int, input().split())

    ans_h = h1 + h2
    ans_m = m1 + m2

    if ans_m >= 60:
        ans_m -= 60
        ans_h += 1
    if ans_h >= 12:
        ans_h -= 12


    print(f'#{i+1} {ans_h} {ans_m}')