N = int(input())

for i in range(1, N):
    space = " " * (N - i)
    star = "*" * i
    print(space + star)

for i in range(N, 0, -1):
    space = " " * (N - i)
    star = "*" * i
    print(space + star)