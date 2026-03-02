from collections import deque
    

def solution(n, computers):
    answer = 0
    
    networks = {c:set() for c in range(n)}
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            if computers[i][j] == 1:
                networks[i].add(j)
                networks[j].add(i)
            
    visited = [False] * n
            
    for c in networks.keys():
        if not visited[c]:
            # bfs
            answer += 1
            
            queue = deque([c])
            visited[c] = True
            
            while queue:
                nxt_c = queue.popleft()
                
                for adj_c in networks[nxt_c]:
                    if not visited[adj_c]:
                        queue.append(adj_c)
                        visited[adj_c] = True
    
    return answer