def check(arr):
    # 가로
    for i in arr:
        if sorted(i) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return 0
    
    
    # 세로
    for i in range(9):
        tmp = []
        for j in range(9):
            tmp.append(arr[j][i])
        if sorted(tmp) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return 0
    
    # 3x3

    for i in range(0, 9, 3):
        t1 = arr[i][0:3] + arr[i+1][0:3] + arr[i+2][0:3]
        t2 = arr[i][3:6] + arr[i+1][3:6] + arr[i+2][3:6]
        t3 = arr[i][6:9] + arr[i+1][6:9] + arr[i+2][6:9]

        if sorted(t1) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return 0
        if sorted(t2) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return 0
        if sorted(t3) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return 0
            
    return 1





T = int(input())

for idx in range(T):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    
    print(f'#{idx+1} {check(arr)}')



