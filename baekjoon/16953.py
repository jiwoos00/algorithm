from collections import deque

def AB(A, B):
    queue = deque([(A, 1)])
    visited = set()

    while queue:
        num, cnt = queue.popleft()

        if num == B:
            return cnt
        
        n1 = num * 2
        if n1 <= B and n1 not in visited:
            visited.add(n1)
            queue.append((n1, cnt + 1))

        n2 = int(str(num) + '1')
        if n2 <= B and n2 not in visited:
            visited.add(n2)
            queue.append((n2, cnt + 1))
    


A, B = map(int, input().split())

res = AB(A, B)
if res:
    print(res)
else:
    print(-1)



"""
visited = [False] * (B + 1)
visited[n1] = True
이러한 식으로 작성하면 메모리 초과 문제가 발생함
"""