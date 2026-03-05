def solution(routes):
    answer = 1
    
    routes.sort(key = lambda x : (x[1], x[0]))
    
    prev_out = routes[0][1]
    
    for enter, out in routes[1:]:
        if prev_out >= enter:
            continue
            
        answer += 1
        prev_out = out
            
    return answer
