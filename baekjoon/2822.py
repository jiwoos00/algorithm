T = 8

score = []
for i in range(1, T + 1):
    score.append((i, int(input())))

score = sorted(score, key = lambda x:x[1], reverse = True)

ans_score, ans_idx = 0, []
for _ in range(5):
    a, b = score.pop(0)
    ans_score += b
    ans_idx.append(a)

ans_idx.sort()
print(ans_score)
print(' '.join(map(str, ans_idx)))
