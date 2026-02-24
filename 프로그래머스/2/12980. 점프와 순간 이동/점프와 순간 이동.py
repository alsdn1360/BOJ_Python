def solution(n):
    answer = 0
    curr_loc = n
    
    while curr_loc > 0:
        if curr_loc % 2 == 0:
            curr_loc = curr_loc // 2
        else:
            curr_loc -= 1
            answer += 1
            
    return answer