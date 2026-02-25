from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    passing = deque()
    waiting = deque(truck_weights)
    passed = 0
    
    curr_weight = 0
    nxt_weight = waiting[0]
    
    while passed < len(truck_weights):
        time += 1
        
        if passing and time - passing[0][0] == bridge_length:
            _, passed_weight = passing.popleft()
            passed += 1
            
            curr_weight -= passed_weight
        
        if waiting and curr_weight + nxt_weight <= weight:
            curr_weight += nxt_weight
            passing.append((time, nxt_weight))
            
            waiting.popleft()
            
            if waiting:
                nxt_weight = waiting[0]
            
    return time