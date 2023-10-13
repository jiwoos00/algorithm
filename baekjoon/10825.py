import sys
import time
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    name, korean, english, math = input().split()
    korean, english, math = int(korean), int(english), int(math)
    arr.append([name, korean, english, math])

arr = sorted(arr, key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(arr[i][0])