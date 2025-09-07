def solution(targets):
    ans = 0
    n = len(targets)
    
    targets.sort(key = lambda x : x[1])
    
    curr_e = 0
    
    for i in range(n):
        if targets[i][0] < curr_e:
            continue
            
        ans += 1
        curr_e = targets[i][1]
    
    return ans