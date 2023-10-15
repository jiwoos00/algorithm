N = input()

hex_arr = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

for i in range(0, 10):
    hex_arr[str(i)] = i

N = N[::-1]
res = 0
for idx, i in enumerate(N):
    res += ((16 ** idx) * hex_arr[i])
    
print(res)