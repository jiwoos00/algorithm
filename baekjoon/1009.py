import sys
input = sys.stdin.readline

T = int(input())
dic = {2:[2, 4, 8, 6], 3:[3, 9, 7, 1], 4:[4, 6], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6], 9:[9, 1]}
for _ in range(T):
    a, b = map(int, input().split())
    
    a = a % 10
    if a == 0:
        print(10)
    elif b == 1 or a == 1 or a == 5 or a == 6:
        print(a)
    else:
        b = b % len(dic[a]) - 1
        print(dic[a][b])

'''
0 : 10
1 : 1
2 : 2 4 6 8
3 : 3 9 7 1
4 : 4 6
5 : 5
6 : 6
7 : 7 9 3 1
8 : 8 4 2 6
9 : 9 1
'''


''' 시간초과

for _ in range(T):
    a, b = map(int, input().split())
    if a == 1:
        print(1)
    else:
        print(str(a ** b)[-1])
'''    
