N = 8
chase = []

for _ in range(N):
    c = input()
    tmp = []
    for i in c:
        tmp.append(i)
    chase.append(tmp)

res = 0
for i in range(N):
    if i % 2 == 0:
        for j in range(0, 8, 2):
            if chase[i][j] == 'F':
                res += 1
    else:
        for j in range(1, 8, 2):
            if chase[i][j] == 'F':
                res += 1

print(res)