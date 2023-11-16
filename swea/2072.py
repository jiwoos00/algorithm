T = int(input())

for idx in range(T):
    s = 0
    arr = list(map(int, input().split()))

    for i in arr:
        if i % 2 != 0:
            s += i
    print(f'#{idx+1} {s}')