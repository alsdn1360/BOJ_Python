from collections import defaultdict, deque


def solution(tickets):
    answer = []
    n = len(tickets)
    
    airlines = defaultdict(list)
    past_airlines = defaultdict(list)
    
    for ori, dest in tickets:
        airlines[ori].append(dest)
        past_airlines[ori].append(False)
    
    for ori, dests in airlines.items():        
        airlines[ori] = sorted(dests)
    
    def dfs(curr_country):
        if len(answer) == n + 1:
            return True
            
        for i, nxt_country in enumerate(airlines[curr_country]):
            if not past_airlines[curr_country][i]:
                answer.append(nxt_country)
                past_airlines[curr_country][i] = True
                
                if dfs(nxt_country):
                    return answer
                
                past_airlines[curr_country][i] = False
                answer.pop()
            
    answer.append('ICN')
    
    return dfs('ICN')