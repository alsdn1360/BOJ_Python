from collections import defaultdict, deque


def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    dists = [float('inf')] * (n + 1)
        
    # BFS
    queue = deque([(1, 1)])
    
    visited = set()
    visited.add(1)
    
    while queue:
        node, cnt = queue.popleft()
        
        dists[node] = min(dists[node], cnt)
            
        for adj_node in graph[node]:
            if adj_node not in visited:
                queue.append((adj_node, cnt + 1))
                visited.add(adj_node)
                
    max_dist = max(dists[1:])
    
    answer = dists.count(max_dist)
    
    return answer