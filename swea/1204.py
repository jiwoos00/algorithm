T = int(input())

for _ in range(T):
    cnt = {}

    idx = int(input())
    arr = list(map(int, input().split()))

    for i in arr:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    ans = (sorted(cnt.items(), key=lambda x:(-x[1], -x[0]))[0][0])
    print(f"#{idx} {ans}")
    
    