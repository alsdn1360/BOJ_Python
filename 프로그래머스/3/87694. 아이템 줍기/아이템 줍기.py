from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def oob(nx, ny):
    return 0 <= nx < 102 and 0 <= ny < 102

def bfs(board, start, end):
    queue = deque([(start[0], start[1], 0)])
    
    visited = [[False] * 102 for _ in range(102)]
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, step = queue.popleft()
        
        if (x, y) == end:
            # 영역을 2배 확장했으니 2로 나눔
            return step // 2
        
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            
            if oob(nx, ny) and not visited[nx][ny] and board[nx][ny]:
                queue.append((nx, ny, step + 1))
                visited[nx][ny] = True

def solution(rectangle, characterX, characterY, itemX, itemY): 
    # 좌표 2배 확장: 최대 좌표 50*2 = 100, 여유분 포함하여 102×102 보드 생성
    board = [[False] * 102 for _ in range(102)]
    
    # 모든 사각형 내부 채우기
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] = True

    # 테두리만 남기기
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                board[i][j] = False
                            
    start = (characterX * 2, characterY * 2)
    end = (itemX * 2, itemY * 2)
    
    return bfs(board, start, end)