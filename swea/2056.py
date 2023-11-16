T = int(input())

for idx in range(T):
    date = input()
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]

    if not (1<= int(month) <= 12):
        print(f'#{idx+1} {-1}')
        continue
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if not (1 <= int(day) <= 31):
            print(f'#{idx+1} {-1}')
            continue
    if int(month) in [9, 11, 4, 6]:
        if not (1 <= int(day) <= 30):
            print(f'#{idx+1} {-1}')
            continue
    if int(month) in [2]:
        if not (1 <= int(day) <= 28):
            print(f'#{idx+1} {-1}')
            continue
    print(f'#{idx+1} {year}/{month}/{day}')
    
