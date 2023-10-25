def find_sequences(N, M, current_sequences = []):
    if len(current_sequences) == M:
        print(' '.join(map(str, current_sequences)))
        return
    
    start_number = 1 if not current_sequences else current_sequences[-1] + 1
    for i in range(start_number, N + 1):
        current_sequences.append(i)
        find_sequences(N, M, current_sequences)
        current_sequences.pop()


N, M = map(int, input().split())
find_sequences(N, M)
