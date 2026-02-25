from collections import deque

def solution(priorities, location):
    answer = 0
    
    n = len(priorities)
    
    target_process = deque([False] * n)
    target_process[location] = True
    
    priorities = deque(priorities)
    
    run_process = max(priorities)
    
    while priorities:
        process, is_target = priorities.popleft(), target_process.popleft()
        
        if process >= run_process:
            answer += 1
            
            if is_target:
                return answer
            
            run_process = max(priorities)
        else:      
            priorities.append(process)
            target_process.append(is_target)
    