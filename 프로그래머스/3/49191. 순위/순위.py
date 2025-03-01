from collections import defaultdict, deque

def bfs(n, graph, player):
    queue = deque([player])
    visited = [False] * (n + 1)
    visited[player] = True
    
    cnt = 0
    
    while queue:
        curr_player = queue.popleft()
        
        for other_player in graph[curr_player]:
            if not visited[other_player]:
                queue.append(other_player)
                visited[other_player] = True
                cnt += 1
            
    return cnt

def solution(n, results):
    answer = 0
    
    winner_graph = defaultdict(list)
    loser_graph = defaultdict(list)
    
    for A, B in results:
        winner_graph[A].append(B)
        loser_graph[B].append(A)
        
    for player in range(1, n + 1):
        win_cnt = bfs(n, winner_graph, player)
        lose_cnt = bfs(n, loser_graph, player)
        
        # N명의 선수가 있을 때, 자기 자신을 제외한 다른 선수와의 경기 결과를 전부 알면 순위가 결정됨(무승부가 없다고 가정)
        if win_cnt + lose_cnt == (n - 1):
            answer += 1
            
    return answer