import collections

# 딕셔너리 이용
def solution(participant, completion):
    ans = {}
    for p in participant:
        if p in ans:
            ans[p] += 1
        else:
            ans[p] = 1
    for c in completion:
        ans[c] -= 1
    
    for i in ans.items():
        if i[1] > 0:
            return i[0]


# collections.Counter 이용
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer.keys())[0]
