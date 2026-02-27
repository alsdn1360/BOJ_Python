from collections import defaultdict, deque


def bfs(tree, n, v1, v2):
    queue = deque([v1])
    
    visited = [False] * (n + 1)
    visited[v1], visited[v2] = True, True
    
    cnt = 1
    
    while queue:
        v = queue.popleft()
        
        for adj_v in tree[v]:
            if not visited[adj_v]:
                queue.append(adj_v)
                visited[adj_v] = True
                cnt += 1
                
    return cnt
            

def solution(n, wires):
    answer = float('inf')
    
    tree = defaultdict(list)
    
    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)
        
    cnt = 0
        
    for v1 in tree.keys():
        for v2 in tree[v1]:
            cnt = bfs(tree, n, v1, v2)
            
            answer = min(answer, abs(n - 2 * cnt))
            
    return answer
