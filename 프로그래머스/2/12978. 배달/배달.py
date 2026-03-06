import heapq


def dijkstra(N, graph):
    costs = {node:float('inf') for node in range(1, N + 1)}
    costs[1] = 0
    
    queue = []
    heapq.heappush(queue, (0, 1))  # cost, 출발 지점
    
    while queue:
        curr_cost, curr_node = heapq.heappop(queue)
        
        if curr_cost < costs[curr_node]:
            continue
            
        for nxt_node, nxt_cost in graph[curr_node]:
            cost = curr_cost + nxt_cost
            
            if cost < costs[nxt_node]:
                costs[nxt_node] = cost
                heapq.heappush(queue, (cost, nxt_node))
                
    return costs


def solution(N, road, K):
    answer = 0

    graph = {node:[] for node in range(1, N + 1)}
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    costs = dijkstra(N, graph)
        
    for cost in costs.values():
        if cost <= K:
            answer += 1
            
    return answer