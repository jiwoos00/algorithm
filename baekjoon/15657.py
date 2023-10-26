def find_sequence(current_sequence = []):
    if len(current_sequence) == M:
        print(' '.join(map(str, current_sequence)))
        return 
    
    for i in arr:
        if not current_sequence or current_sequence[-1] <= i:
            current_sequence.append(i)
            find_sequence(current_sequence)
            current_sequence.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
find_sequence()