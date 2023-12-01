price = int(input())

arr = [2, 5]

d = [100001] * (price + 1)

d[0] = 0
for i in arr:
    for j in range(i, price + 1):
        if d[j - i] != 100001:
            d[j] = min(d[j], d[j - i] + 1)

if d[price] == 100001:
    print(-1)
else:
    print(d[price])
