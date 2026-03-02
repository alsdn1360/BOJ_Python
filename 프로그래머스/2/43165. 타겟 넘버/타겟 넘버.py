def bt(n, numbers, idx, current, target):    
    global answer
    
    if idx == n:
        if current == target:
            answer += 1
        
        return
        
    bt(n, numbers, idx + 1, current + numbers[idx], target)
    bt(n, numbers, idx + 1, current - numbers[idx], target)
    

def solution(numbers, target):
    global answer
    
    answer = 0
    
    bt(len(numbers), numbers, 0, 0, target)
    
    return answer