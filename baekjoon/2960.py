def find_kth_removed_number(N, K):
    sieve = [True] * (N + 1)
    count = 0

    for num in range(2, N + 1):

        for multiple in range(num, N + 1, num):
            if sieve[multiple]:
                sieve[multiple] = False
                count += 1
            if count == K:
                return multiple

   
N, K = map(int, input().split())
result = find_kth_removed_number(N, K)
print(result)
