from collections import defaultdict, deque

def bfs(n, graph):
    # 시작 노드, 거리
    queue = deque([(1, 0)])
    visited = set()
    visited.add(1)
    
    # 노드별 거리 저장을 위한 배열
    dists = [0] * (n + 1)
    
    while queue:
        curr_node, dist = queue.popleft()
        
        for adj_node in graph[curr_node]:
            if adj_node not in visited:
                queue.append((adj_node, dist + 1))
                visited.add(adj_node)
                dists[adj_node] = dist + 1
                
    # 거리가 가장 먼 값을 찾아서 그 값과 같은 수를 가지는 배열 요소 개수 리턴
    return dists.count(max(dists))

def solution(n, edge):
    graph = defaultdict(list)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    return bfs(n, graph)