from collections import defaultdict


def solution(participant, completion):
    participant_status = defaultdict(int)
    
    for p in participant:
        if participant_status[p]:
            participant_status[p] += 1
            continue
            
        participant_status[p] = 1
        
    for c in completion:
        participant_status[c] -= 1
        
    for p, c in participant_status.items():
        if c > 0:
            return p
    