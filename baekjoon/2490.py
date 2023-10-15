for _ in range(3):
    arr = list(map(int, input().split()))
    
    n = arr.count(1)
    if n == 4:
        print("E")
    elif n == 3:
        print("A")
    elif n == 2:
        print("B")
    elif n == 1:
        print("C")
    elif n == 0:
        print("D")