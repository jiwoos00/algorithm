cnt = 0

def n_queens(i, col):
    global cnt
    n = len(col) - 1
    if (promising(i, col)):
        if (i == n): # 마지막 노드
            cnt += 1
            return
        else:
            for j in range(1, n + 1):
                col[i+1] = j
                n_queens(i + 1, col)

def promising(i, col):

    for k in range(1, i):
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)): # 행과 대각선 검사
            return False
        k += 1
    return True

N = int(input())
col = [0] * (N + 1)

n_queens(0, col)
print(cnt)