N = int(input())
arr = [(0,0), (1, 0)]

for _ in range(N):
    pre_a, pre_b = arr[-1]
    arr.append((pre_b, pre_a + pre_b))
    
a, b = arr[-1]
print(a, b)