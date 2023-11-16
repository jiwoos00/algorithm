T = int(input())

for idx in range(1, T + 1):
    arr = list(map(int, input().split()))
    avg = int(round(sum(arr) / 10, 0))

    print(f'#{idx} {avg}')