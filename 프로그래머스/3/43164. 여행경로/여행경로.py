def solution(tickets):
    # 티켓 사전순 정렬
    tickets.sort()
    n = len(tickets)
    used = [False] * n

    def dfs(route):
        if len(route) == n + 1:
            return route
        
        for i in range(n):
            # 현재 공항과 티켓 출발지가 일치하고, 티켓이 미사용인 경우
            if route[-1] == tickets[i][0] and not used[i]:
                used[i] = True  # 티켓 사용 표시
                
                result = dfs(route + [tickets[i][1]])
                
                if result:
                    return result
                
                used[i] = False  # 백트래킹
                
        return None

    return dfs(["ICN"])