from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def oob(nx, ny, n, m):
    return 0 <= nx < n and 0 <= ny < m

def bfs(maps, answer):
    n = len(maps)
    m = len(maps[0])
    
    # (출발 x, 출발 y, 현재 지난 칸) 초기화
    queue = deque([(0, 0, 1)])
    
    # 방문 여부 초기화
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    # 출발칸으로부터 거리 초기화
    grid = [[0] * m for _ in range(n)]
    grid[0][0] = 1
    
    is_escape = False
    
    while queue:
        x, y, distance = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            is_escape = True
            answer = grid[x][y]
            break
        
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            
            if oob(nx, ny, n, m) and not visited[nx][ny] and maps[nx][ny] == 1:
                queue.append((nx, ny, distance + 1))
                visited[nx][ny] = True
                grid[nx][ny] = distance + 1
                
    if is_escape:
        return answer
    else:
        return -1

def solution(maps):
    answer = 0
    
    return bfs(maps, answer)
    