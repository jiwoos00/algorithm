dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for idx in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    x, y, d = 0, 0, 0
    num = 1

    while num <= n * n:

        arr[x][y] = num
        x += dx[d]
        y += dy[d]
        num += 1

        # 방향 전환
        if x < 0 or x >= n or y < 0 or y >= n or arr[x][y] > 0:
            x -= dx[d]
            y -= dy[d]
            d = (d + 1) % 4
            x += dx[d]
            y += dy[d]

    print(f"#{idx}")
    for row in arr:
        print(" ".join(map(str, row)))
