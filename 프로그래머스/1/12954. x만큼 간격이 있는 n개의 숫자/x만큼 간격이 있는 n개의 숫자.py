def solution(x, n):
    answer = []
    curr_x = x
    
    while (len(answer) < n):
        answer.append(curr_x)
        curr_x += x
    
    return answer