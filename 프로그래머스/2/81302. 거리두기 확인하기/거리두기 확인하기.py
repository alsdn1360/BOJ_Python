from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bound(nx, ny):
    return 0 <= nx < 5 and 0 <= ny < 5

def check_manhattan_dist(x1, y1, x2, y2):
    return True if abs(x1 - x2) + abs(y1 - y2) <= 2 else False

def bfs(i, j, place):
    queue = deque([(i, j)])
    
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[i][j] = True
                
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            
            if in_bound(nx, ny) and not visited[nx][ny] and check_manhattan_dist(i, j, nx, ny):
                # P가 있으면 바로 종료
                if place[nx][ny] == 'P':
                    return False
                # 파티션이 있으면 그 방향으로는 탐색 종료
                elif place[nx][ny] == 'X':
                    continue
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                
    return True

def solution(places):
    answer = []
    
    for place in places:    
        is_ok = True
                
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(i, j, place):
                        is_ok = False
                        break
                
            if not is_ok:
                break
        
        answer.append(1 if is_ok else 0)
                
    return answer