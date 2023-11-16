T = int(input())

for idx in range(T):
    arr = list(map(int, input().split()))
    print(f'#{idx+1} {max(arr)}')