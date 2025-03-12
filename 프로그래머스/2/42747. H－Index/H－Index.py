def solution(citations):
    h_index = 0
    
    for h in range(len(citations) + 1):
        cnt = 0
        
        for citation in citations:
            if citation >= h:
                cnt += 1
                
        if cnt >= h:
            h_index = max(h_index, h)
            
    return h_index