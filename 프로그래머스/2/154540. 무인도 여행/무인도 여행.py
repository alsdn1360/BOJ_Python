from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def oob(n, m, nx, ny):
    return 0 <= nx < n and 0 <= ny < m

def bfs(n, m, maps, visited, i, j, days):
    queue = deque([(i, j)])
    visited[i][j] = True
    
    total_days = days
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            
            if oob(n, m, nx, ny) and not visited[nx][ny] and maps[nx][ny] != 'X':
                total_days += int(maps[nx][ny])
                
                queue.append((nx, ny))
                visited[nx][ny] = True
                    
    return total_days

def solution(maps):
    answer = []
    new_maps = []
    
    # maps 리스트로 변환
    for elem in maps:
        new_maps.append(list(elem))
        
    # maps의 크기
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    # 연결된 무인도 식량 확인
    for i in range(n):
        for j in range(m):
            if new_maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(n, m, new_maps, visited, i, j, int(new_maps[i][j])))
    
    # 오름차순 정렬
    answer.sort()
    
    return answer if answer else [-1]