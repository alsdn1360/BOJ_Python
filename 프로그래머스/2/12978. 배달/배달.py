import heapq

def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N + 1)]
    
    # 방향이 없으므로 서로 연결
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    dists = [float("inf")] * (N + 1)
    dists[1] = 0
    
    heap = []
    # heap에 (코스트, 출발점) 추가
    heapq.heappush(heap, (0, 1))
    
    while heap:
        dist, curr_node = heapq.heappop(heap)
        
        for adj_node, adj_dist in graph[curr_node]:
            cost = dist + adj_dist
            
            if cost < dists[adj_node]:
                dists[adj_node] = cost
                heapq.heappush(heap, (cost, adj_node))
                
    # K 시간 이내만 골라내기
    for i in range(N):
        if dists[i + 1] <= K:
            answer += 1
    
    return answer