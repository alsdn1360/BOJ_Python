def solution(n):
    answer = n + 1
    
    # n의 1의 갯수 세기
    bin_n_cnt = format(n, 'b').count('1')
    
    while True:
        bin_answer_cnt = format(answer, 'b').count('1')
        
        if bin_answer_cnt == bin_n_cnt:
            return answer
        
        answer += 1
    
    return answer