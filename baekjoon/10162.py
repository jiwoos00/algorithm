T = int(input())

t = [300, 60, 10]
t_cnt = [0, 0, 0]

for idx, i in enumerate(t):
    if T >= i:
        cnt = T // i
        T -= (i * cnt)
        t_cnt[idx] += cnt

if T == 0:
    print(t_cnt[0], t_cnt[1], t_cnt[2])
else:
    print(-1)

