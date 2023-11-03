def find_sequence(cur_sequence = []):
    if len(cur_sequence) == M:
        print(' '.join(map(str, cur_sequence)))
        return
    
    for i in arr:
        if not cur_sequence or i >= cur_sequence[-1]:
            cur_sequence.append(i)
            find_sequence(cur_sequence)
            cur_sequence.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()

find_sequence()