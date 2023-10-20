# 시간 단축
import sys
input = sys.stdin.readline

def find_max_tetromino_sum(N, M, paper):
    tetrominoes = [
        # T자 모양과 회전
        [[(0, 0), (0, 1), (0, 2), (1, 1)]],
        [[(0, 1), (1, 0), (1, 1), (1, 2)]],
        [[(0, 1), (1, 0), (1, 1), (2, 1)]],
        [[(0, 0), (1, 0), (1, 1), (2, 0)]],
        # 일자 모양과 회전
        [[(0, 0), (0, 1), (0, 2), (0, 3)]],
        [[(0, 0), (1, 0), (2, 0), (3, 0)]],
        # 네모 모양
        [[(0, 0), (0, 1), (1, 0), (1, 1)]],
        # L자 모양과 회전
        [[(0, 0), (1, 0), (2, 0), (2, 1)]],
        [[(0, 0), (1, 0), (2, 0), (0, 1)]],
        [[(0, 0), (0, 1), (0, 2), (1, 2)]],
        [[(0, 0), (0, 1), (0, 2), (1, 0)]],
        [[(0, 0), (1, 0), (1, 1), (1, 2)]],
        [[(0, 1), (1, 1), (2, 0), (2, 1)]],
        [[(0, 0), (0, 1), (1, 1), (2, 1)]],
        [[(1, 0), (1, 1), (1, 2), (0, 2)]],
        
        
        # 지그재그 모양과 회전
        [[(0, 0), (0, 1), (1, 1), (1, 2)]],
        [[(0, 1), (0, 2), (1, 0), (1, 1)]],
        [[(0, 0), (1, 0), (1, 1), (2, 1)]],
        [[(0, 1), (1, 0), (1, 1), (2, 0)]]
    ]

    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < M

    def calculate_sum(x, y, tetromino):
        total_sum = 0
        for dx, dy in tetromino:
            if is_valid(x + dx, y + dy):
                total_sum += paper[x + dx][y + dy]
            else:
                return -1
        return total_sum

    max_sum = 0
    for x in range(N):
        for y in range(M):
            for tetromino_set in tetrominoes:
                for tetromino in tetromino_set:
                    tetromino_sum = calculate_sum(x, y, tetromino)
                    if tetromino_sum != -1 and tetromino_sum > max_sum:
                        max_sum = tetromino_sum

    return max_sum

# 입력 처리
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
result = find_max_tetromino_sum(N, M, paper)
print(result)






# import sys
# input = sys.stdin.readline

# def find_max_tetromino_sum(N, M, paper):
#     tetrominoes = [
#         # T자 모양과 회전
#         [[(0, 0), (0, 1), (0, 2), (1, 1)]],
#         [[(0, 1), (1, 0), (1, 1), (1, 2)]],
#         [[(0, 1), (1, 0), (1, 1), (2, 1)]],
#         [[(0, 0), (1, 0), (1, 1), (2, 0)]],
#         # 일자 모양과 회전
#         [[(0, 0), (0, 1), (0, 2), (0, 3)]],
#         [[(0, 0), (1, 0), (2, 0), (3, 0)]],
#         # 네모 모양
#         [[(0, 0), (0, 1), (1, 0), (1, 1)]],
#         # L자 모양과 회전
#         [[(0, 0), (1, 0), (2, 0), (2, 1)]],
#         [[(0, 0), (1, 0), (2, 0), (0, 1)]],
#         [[(0, 0), (0, 1), (0, 2), (1, 2)]],
#         [[(0, 0), (0, 1), (0, 2), (1, 0)]],
#         [[(0, 0), (1, 0), (1, 1), (1, 2)]],
#         [[(0, 1), (1, 1), (2, 0), (2, 1)]],
#         [[(0, 0), (0, 1), (1, 1), (2, 1)]],
#         [[(1, 0), (1, 1), (1, 2), (0, 2)]],
        
#         # 지그재그 모양과 회전
#         [[(0, 0), (0, 1), (1, 1), (1, 2)]],
#         [[(0, 1), (0, 2), (1, 0), (1, 1)]],
#         [[(0, 0), (1, 0), (1, 1), (2, 1)]],
#         [[(0, 1), (1, 0), (1, 1), (2, 0)]]
#     ]

#     def calculate_sum(x, y, tetromino):
#         total_sum = 0
#         for dx, dy in tetromino:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < M:
#                 total_sum += paper[nx][ny]
#             else:
#                 return -1
#         return total_sum


#     max_sum = 0
#     for x in range(N):
#         for y in range(M):
#             for tetromino_set in tetrominoes:
#                 for tetromino in tetromino_set:
#                     tetromino_sum = calculate_sum(x, y, tetromino)
#                 max_sum = max(tetromino_sum, max_sum)

#     max_sum = 0
#     for x in range(N):
#         for y in range(M):
#             for tetromino_set in tetrominoes:
#                 for tetromino in tetromino_set:
#                     tetromino_sum = calculate_sum(x, y, tetromino)
#                     if tetromino_sum != -1 and tetromino_sum > max_sum:
#                         max_sum = tetromino_sum

#     return max_sum

# N, M = map(int, input().split())
# paper = [list(map(int, input().split())) for _ in range(N)]

# res = find_max_tetromino_sum(N, M, paper)
# print(res)