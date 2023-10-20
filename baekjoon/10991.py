N = int(input())

j = N - 1
for i in range(1, N + 1):
    space = ' ' * j
    j -= 1
    
    print(space + ' '.join(i * '*'))

    