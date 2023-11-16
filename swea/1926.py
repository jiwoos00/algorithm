N = int(input())

for i in range(1, N + 1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        cnt = 0
        for j in str(i):
            if '3' in j or '6' in j or '9' in j:
                cnt += 1
        
        print('-' * cnt, end = ' ')
    else:
        print(i, end = ' ')