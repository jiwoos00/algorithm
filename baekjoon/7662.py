import heapq
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    max_heap = []
    min_heap = []
    deleted = set()
    
    k = int(input())
    for i in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            heapq.heappush(max_heap, (-num, i))
            heapq.heappush(min_heap, (num, i))
        else: # 'D'
            if num == 1:
                while max_heap and max_heap[0][1] in deleted:
                    heapq.heappop(max_heap)
                if max_heap:
                    deleted.add(max_heap[0][1])
                    heapq.heappop(max_heap)
            else:
                while min_heap and min_heap[0][1] in deleted:
                    heapq.heappop(min_heap)
                if min_heap:
                    deleted.add(min_heap[0][1])
                    heapq.heappop(min_heap)


    while max_heap and max_heap[0][1] in deleted:
        heapq.heappop(max_heap)
    while min_heap and min_heap[0][1] in deleted:
        heapq.heappop(min_heap)
    
    if not max_heap or not min_heap:
        print("EMPTY")
    else:
        min_val = min_heap[0][0]
        max_val = -max_heap[0][0]
        print(max_val, min_val)