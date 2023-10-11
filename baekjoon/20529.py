from itertools import combinations
import sys
input = sys.stdin.readline

def mbti(type1, type2):
    dis = 0
    for i in range(4):
        if type1[i] != type2[i]:
            dis += 1
    return dis

T = int(input())

for _ in range(T):
    N = int(input())

    types = input().split()
    types.sort()

    min_dis = float('inf')

    if N > 32:
        print(0)
    else:
        for comb in combinations(types, 3):
            dis = 0

            dis += mbti(comb[0], comb[1])
            dis += mbti(comb[1], comb[2])
            dis += mbti(comb[0], comb[2])
            

            #for c in combinations(comb, 2):
            #   dis += mbti(c[0], c[1])

            # for i in range(2):
            #     for j in range(i + 1, 3):
            #         dis += mbti(comb[i], comb[j])
            min_dis = min(min_dis, dis)

        print(min_dis)