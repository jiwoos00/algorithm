def find_sequence(N, M, current_sequence = []):
    if len(current_sequence) == M:
        print(' '.join(map(str, current_sequence)))
        return


    for i in arr:
        if not i in current_sequence:
            current_sequence.append(i)
            find_sequence(N, M, current_sequence)
            current_sequence.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
find_sequence(N, M)