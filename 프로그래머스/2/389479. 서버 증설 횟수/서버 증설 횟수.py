from collections import deque

def solution(players, m, k):
    server = 0
    server_time = deque() # 서버를 증설한 시간 담을 덱
    server_cnt = 0
    
    # 시각 -> 0 ~ 1시면 t = 0
    for t in range(24):
        # k 시간이 넘은 서버 반납 처리
        while server_time and (t - server_time[0]) == k:
            server_time.popleft()
            server -= 1
            
        player = players[t]
        
        # m명 미만이라면 서버 증설 하지 않음
        if player < m:
            continue
        
        # 현재 서버가 유저를 감당 가능한지 체크
        if server * m >= player:
            continue
        
        # 최소 증설된 서버 체크
        if server * m <= player < (server + 1) * m:
            continue
        
        # 서버 증설
        server_cnt += (player // m) - server
        
        for _ in range((player // m) - server):
            server_time.append(t)
            
        server = player // m
        
    return server_cnt