from collections import deque


MAX_COOR = 102
MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def in_bound(nx, ny):
    return 0 <= nx < MAX_COOR and 0 <= ny < MAX_COOR


def solution(rectangle, characterX, characterY, itemX, itemY):
    topo = [[0 for _ in range(MAX_COOR)] for _ in range(MAX_COOR)]
    
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = 2 * x1, 2 * y1, 2 * x2, 2 * y2
        
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if topo[i][j] == 2:
                    continue
                    
                if i == x1 or i == x2 or j == y1 or j == y2:
                    topo[i][j] = 1
                else:
                    topo[i][j] = 2
                    
    character_x, character_y =  2 * characterX, 2 * characterY
    item_x, item_y = 2 * itemX, 2 * itemY
    
    # BFS
    queue = deque([(character_x, character_y, 0)])
    
    visited = [[False for _ in range(MAX_COOR)] for _ in range(MAX_COOR)]
    visited[character_x][character_y] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if (x, y) == (item_x, item_y):
            return cnt // 2
        
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            
            if in_bound(nx, ny) and not visited[nx][ny] and topo[nx][ny] == 1:
                queue.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
