digit = list(map(int, input()))

digit.sort(reverse = True)
if sum(digit) % 3 == 0 and digit[-1] == 0:
    print(''.join(map(str, digit)))
else:
    print(-1)




"""
N = int(input())

cnt = [0] * 10
sum_cnt = 0
ch = 0

for i in str(N):
    cnt[int(i)] += 1
    if int(i) == 0:
        ch = 1
    else:
        sum_cnt += int(i)

if ch == 1:
    sum_cnt *= 10


if sum_cnt % 30 != 0:
    print(-1)
else:
    ans = ''
    for digit in range(9, -1, -1):
        ans += (cnt[digit] * str(digit))
    
    if ans[0] == '0':
        print("0")
    else:
        print(ans)

"""