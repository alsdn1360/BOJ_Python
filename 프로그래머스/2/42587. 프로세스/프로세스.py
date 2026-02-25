from collections import deque

def solution(priorities, location):
    answer = 0
    
    processes = deque([(p, i == location) for i, p in enumerate(priorities)])
    
    run_process = max(priorities)
    
    while processes:
        process, is_target = processes.popleft()
        
        if process == run_process:
            answer += 1
            
            if is_target:
                return answer
            
            run_process = max(p[0] for p in processes)
        else:
            processes.append((process, is_target))
            