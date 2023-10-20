m = 0
for idx in range(5):
    tmp = list(map(int, input().split()))

    if sum(tmp) > m:
        m = sum(tmp)
        m_idx = idx + 1

print(m_idx, m)