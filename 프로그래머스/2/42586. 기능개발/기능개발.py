from math import ceil

def solution(progresses, speeds):
    answer = []
    
    n = len(progresses)
    
    deploy_days = []
    
    for i in range(n):
        p, s = progresses[i], speeds[i]
        deploy_days.append(ceil((100 - p) / s))
        
    l, r = 0, 1
    
    while l <= r and r < n:
        if deploy_days[l] < deploy_days[r]:
            answer.append(r - l)
            l = r
        else:
            r += 1
            
    answer.append(r - l)
        
    return answer