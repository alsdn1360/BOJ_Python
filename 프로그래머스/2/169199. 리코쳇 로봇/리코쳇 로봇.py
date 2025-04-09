from collections import deque

# 상, 하, 좌, 우
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def oob(n, m, nx, ny):
    return 0 <= nx < n and 0 <= ny < m

def bfs(n, m, board, start, target):
    queue = deque([(start[0], start[1], 0)])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, step = queue.popleft()
        
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            
            # 벽이나 장애물 만날 때까지 계속 미끄러짐
            while oob(n, m, nx, ny) and board[nx][ny] != 'D':
                nx += dx
                ny += dy
                
            # 바로 직전의 좌표가 벽이나 장애물을 만나기 전 좌표
            final_x, final_y = nx - dx, ny - dy
            
            # 그 좌표가 target이면 리턴(아직 이동 횟수를 더하지 않았기 때문에 +1 해서 리턴)
            if (final_x, final_y) == target:
                return step + 1
            
            if not visited[final_x][final_y]:
                queue.append((final_x, final_y, step + 1))
                visited[final_x][final_y] = True
                
    return -1
                
def solution(board):
    new_board = []
    n, m = len(board), len(board[0])
    
    # 리스트로 변환해서 보드 생성
    for state in board:
        new_board.append(list(state))
    
    # R 좌표 및 G 좌표 초기화
    start = ()
    target = ()
    
    for i in range(n):
        for j in range(m):
            if new_board[i][j] == 'R':
                start = (i, j)
            
            if new_board[i][j] == 'G':
                target = (i, j)
    
    return bfs(n, m, new_board, start, target)