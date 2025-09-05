import heapq

def dijkstra(n, graph, start):
    costs = { node : float('inf') for node in range(1, n + 1)}
    costs[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        curr_cost, curr_node = heapq.heappop(queue)
        
        if costs[curr_node] < curr_cost:
            continue
            
        for nxt_node in graph[curr_node]:
            cost = curr_cost + 1
            
            if costs[nxt_node] > cost:
                costs[nxt_node] = cost
                heapq.heappush(queue, (cost, nxt_node))
    
    return costs


def solution(n, roads, sources, destination):
    graph = { node : [] for node in range(1, n + 1)}
    
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
        
    # 목적지에서 출발하면 모든 지역까지의 최단 거리가 나옴
    costs = dijkstra(n, graph, destination)
    
    ans = []
    
    for source in sources:
        if costs[source] == float('inf'):
            ans.append(-1)
        else:
            ans.append(costs[source])
        
    return ans
        