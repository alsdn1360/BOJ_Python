from collections import deque


MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def in_bound(n, m, nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def bfs(maps, n, m):
    answer = float('inf')
    
    queue = deque([(0, 0, 1)]) # x, y, cnt
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if (x, y) == (n - 1, m - 1):
            answer = min(answer, cnt)
            
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            
            if in_bound(n, m, nx, ny) and maps[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
    
    return answer if answer != float('inf') else -1


def solution(maps):
    n, m = len(maps), len(maps[0])
    
    return bfs(maps, n, m)