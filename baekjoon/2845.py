L, P = map(int, input().split())
predict_cnt = list(map(int, input().split()))
cal_cnt = L * P

for c in predict_cnt:
    print(c - cal_cnt, end = ' ')