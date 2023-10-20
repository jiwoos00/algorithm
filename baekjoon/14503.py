# 방향에 따른 이동 방향 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(r, c, d):
    global count

    # 현재 위치 청소
    if graph[r][c] == 0:
        graph[r][c] = 2
        count += 1

    # 네 방향 모두 청소되었거나 벽인 경우
    if all(graph[r + dx[i]][c + dy[i]] != 0 for i in range(4)):
        back_dir = (d + 2) % 4
        back_x, back_y = r + dx[back_dir], c + dy[back_dir]

        # 후진할 수 있다면 후진
        if graph[back_x][back_y] != 1:
            clean(back_x, back_y, d)
            return
        else:  # 후진할 수 없으면 작동 중지
            return

    # 왼쪽 방향으로 회전
    left_dir = (d + 3) % 4
    left_x, left_y = r + dx[left_dir], c + dy[left_dir]

    # 왼쪽 방향에 청소하지 않은 공간이 있다면 회전하고 전진
    if graph[left_x][left_y] == 0:
        clean(left_x, left_y, left_dir)
    else:  # 왼쪽 방향에 청소할 공간이 없으면 회전만
        clean(r, c, left_dir)

N, M = map(int, input().split())
start_r, start_c, start_d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

count = 0
clean(start_r, start_c, start_d)
print(count)
