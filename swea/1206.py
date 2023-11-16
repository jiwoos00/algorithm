for idx in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))

    s = 0
    for i in range(2, n - 2):
        tmp = arr[i] - max(arr[i-1], arr[i-2], arr[i+1], arr[i+2])
        if tmp > 0:
            s += tmp
    print(f'#{idx} {s}')