import math

def count(x1, y1, r1, x2, y2, r2):
    # 두 원의 중심 사이 거리 계산 
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if distance == 0 and r1 == r2: # 두 원이 같을 때
        return -1
    elif distance > r1 + r2: # 두 원이 서로 떨어져 있을 때
        return 0
    elif distance + min(r1, r2) < max(r1, r2): # 한 원이 다른 원에 포함
        return 0
    elif distance == r1 + r2 or distance + min(r1, r2) == max(r1, r2): # 한 지점에서 만남
        return 1
    else:
        return 2



T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    res = count(x1, y1, r1, x2, y2, r2)
    print(res)

