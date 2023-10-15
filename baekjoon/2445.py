N = int(input())

for i in range(1, N):
    star = "*" * i
    space = " " * (N * 2 - (i * 2))
    print(star + space + star)

for i in range(N, 0, -1):
    star = "*" * i
    space = " " * (N * 2 - (i * 2))
    print(star + space + star)