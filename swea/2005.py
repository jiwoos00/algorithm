T = int(input())

for idx in range(T):
    n = int(input())
    print(f'#{idx+1}')

    arr = [[1]]
    print(1)
    for i in range(n - 1):
        tmp = []
        for j in range(i + 2):
            if j == 0:
                tmp.append(arr[i][0])
            elif j == i + 1:
                tmp.append(arr[i][i])
            else:
                tmp.append(arr[i][j-1] + arr[i][j])
        arr.append(tmp)
        print(' '.join(map(str, tmp)))
        