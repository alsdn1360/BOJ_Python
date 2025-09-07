def solution(targets):
    ans = 0
    
    targets.sort(key = lambda x : x[1])
    
    curr_e = 0
    
    for s, e in targets:
        if s >= curr_e:
            ans += 1
            curr_e = e
    
    return ans