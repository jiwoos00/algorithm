# 포인터 이용

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
start, end = 0, n - 1
ans = 0

while(start < end):
    
    num = arr[start] + arr[end]
    
    if num == x:
        start += 1
        end -= 1
        ans += 1
    elif num > x:
        end -= 1
    elif num < x:
        start += 1

print(ans)

# 시간초과
# arr.sort()
# ans = 0

# for i in range(len(arr) - 1):
#     for j in range(len(arr) - 1, i + 1, -1):
#         if arr[i] + arr[j] == x:
#             ans += 1
#             break

# print(ans)