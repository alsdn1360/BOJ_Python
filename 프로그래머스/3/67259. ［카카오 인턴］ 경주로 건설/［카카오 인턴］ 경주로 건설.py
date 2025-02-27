from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def oob(nx, ny, N):
    return 0 <= nx < N and 0 <= ny < N

def bfs(board, N):
    # x, y, direction, curr_cost
    queue = deque([(0, 0, -1, 0)])
    
    # 방향 => (0 : 상), (1 : 하), (2 : 좌), (3 : 우)
    cost = [[[float("inf") for _ in range(4)] for _ in range(N)] for _ in range(N)]
    
    # 모든 방향에 대해서 초기 비용 0으로 초기화
    for i in range(4):
        cost[0][0][i]
        
    while queue:
        x, y, direction, curr_cost = queue.popleft()
        
        if curr_cost > cost[x][y][direction]:
            continue
            
        # 네 방향으로 이동하는데, 방향에 대한 인덱스를 가지고 옴
        for i, (dx, dy) in enumerate(MOVES):
            nx, ny = x + dx, y + dy
            
            if not oob(nx, ny, N) or board[nx][ny] == 1:
                continue
            
            # 직선 코스는 100원 추가
            new_cost = curr_cost + 100
            
            # 시작점을 제외하고 곡선코스는 500원 추가
            if direction != i and (x != 0 or y != 0):
                new_cost += 500
                
            # 새로운 비용이 이전의 값보다 작으면 갱신
            if new_cost < cost[nx][ny][i]:
                cost[nx][ny][i] = new_cost
                queue.append((nx, ny, i, new_cost))
                
    # 도착점에서 네 가지 방향 중 가장 작은 값 선택
    return min(cost[N - 1][N - 1])
                    
def solution(board):
    N = len(board)
    
    return bfs(board, N)