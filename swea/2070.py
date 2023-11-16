T = int(input())

for idx in range(T):
    a, b = map(int, input().split())
    if a < b:
        ans = '<'
    elif a > b:
        ans = '>'
    else:
        ans = '='
    print(f'#{idx+1} {ans}')