import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N = int(input())
    applicants = []

    for _ in range(N):
        rank = list(map(int, input().split()))
        applicants.append(rank)

    applicants = sorted(applicants, key = lambda x:x[0])
    
    min_interview_rank = applicants[0][1]
    hired_applicants = 1

    for i in range(1, N):
        if applicants[i][1] < min_interview_rank:
            min_interview_rank = applicants[i][1]
            hired_applicants += 1
            
    print(hired_applicants)



