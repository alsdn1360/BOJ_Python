def solution(storey):    
    answer = 0
    
    while storey > 0:
        # 1의 자리만 가져옴
        n = storey % 10
        
        # 5보다 크면 올림
        if n > 5:
            answer += 10 - n
            storey += 10 - n
        elif n == 5:
            nxt_n = (storey % 100) // 10
            
            # 5일 때는 바로 앞자리의 수에 따라 달라짐
            if nxt_n >= 5:
                answer += 10 - n
                storey += 10 - n
            else:
                answer += n
        # 5보다 작으면 내림
        else:
            answer += n
            
        storey //= 10
            
    return answer
        