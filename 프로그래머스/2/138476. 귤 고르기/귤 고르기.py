from collections import defaultdict

def solution(k, tangerine):
    tangerines = defaultdict(int)
    
    for t in tangerine:
        tangerines[t] += 1
        
    sorted_tangerines = sorted(tangerines.items(), key=lambda x:x[1], reverse=True)
    
    total_cnt = 0
    answer = 0
        
    for _, cnt in sorted_tangerines:
        total_cnt += cnt
        answer += 1
        
        if total_cnt >= k:
            break
    
    return answer