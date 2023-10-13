
N = int(input())
M = int(input())
S = input()

cursor = 0
cnt = 0
res = 0
while cursor < M:
    
    if S[cursor:cursor + 3] == "IOI":
        cursor += 2
        cnt += 1

        if cnt == N:
            res += 1
            cnt -= 1
    else:
        cursor += 1
        cnt = 0
print(res)
