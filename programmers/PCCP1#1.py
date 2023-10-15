def solution(input_string):
    
    cnt = dict()
    
    for idx, s in enumerate(input_string):
        if s in cnt:
            cnt[s].append(idx)
        else:
            cnt[s] = [idx]
    
    ans = []
    for s, num in cnt.items():
        for i in range(1, len(num)):
            if cnt[s][i] - cnt[s][i - 1] > 1:
                ans.append(s)
                break
    ans.sort()
    
    if ans:
        return (''.join(ans))
    else:
        return ("N")
    
  
