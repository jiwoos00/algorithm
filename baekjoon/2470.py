N = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, len(arr) - 1
m = float('inf')

while (start < end):
    s = arr[start] + arr[end]

    if abs(s) < m:
        m = abs(s)
        a, b = arr[start], arr[end]
    
    if s == 0:
        print(arr[start], arr[end])
        break
    
    elif s < 0:
        start += 1
    
    elif s > 0:
        end -= 1

if s != 0:
    print(a, b)
    

