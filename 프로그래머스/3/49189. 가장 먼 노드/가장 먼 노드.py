from collections import defaultdict, deque


def solution(n, edge):  
    graph = defaultdict(list)
    
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS
    queue = deque([1])
    
    dists = [-1] * (n + 1)
    dists[1] = 0
    
    while queue:
        node = queue.popleft()
            
        for adj_node in graph[node]:
            if dists[adj_node] == -1:
                queue.append(adj_node)
                dists[adj_node] = dists[node] + 1
    
    return dists.count(max(dists))
