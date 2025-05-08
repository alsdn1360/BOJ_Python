from collections import deque

def solution(queue1, queue2):
    answer = 0
    n = len(queue1)
    
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    
    total = sum_q1 + sum_q2
    
    if total % 2 != 0:
        return -1
    
    while sum_q1 != (total // 2):
        if answer > (2 * n + 1):
            return -1
        
        if sum_q1 > sum_q2:
            curr_num = deque1.popleft()
            
            sum_q1 -= curr_num
            sum_q2 += curr_num
            
            deque2.append(curr_num)
        else:
            curr_num = deque2.popleft()
            
            sum_q1 += curr_num
            sum_q2 -= curr_num
            
            deque1.append(curr_num)
            
        answer += 1
            
    return answer