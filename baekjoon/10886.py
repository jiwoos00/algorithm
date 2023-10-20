T = int(input())
res = [0, 0]
for _ in range(T):
    res[int(input())] += 1

if res[0] > res[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
