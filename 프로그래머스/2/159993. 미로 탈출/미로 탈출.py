from collections import deque

def bfs(maps, start, target):
    n = len(maps)
    m = len(maps[0])
    
    # 방문 여부를 저장하는 2차원 배열
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    # 큐 생성 및 시작 좌표, 초기 이동 횟수 추가
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    
    # 순서대로 우, 좌, 하, 상
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        row, col, steps = queue.popleft()
        
        # 현재 칸이 찾고자하는 칸(통로, 레버)이면 반환
        if maps[row][col] == target:
            return steps
        
        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc
            
            # 새로운 칸이 미로를 벗어나는지 확인
            if 0 <= new_row < n and 0 <= new_col < m:
                # 방문하지 않았고, 벽이 아닌지 확인
                if not visited[new_row][new_col] and maps[new_row][new_col] != 'X':
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, steps + 1))
                    
    return -1
    
def solution(maps):
    start = None
    lever = None
    
    # 시작 지점, 레버, 출구의 좌표를 찾음
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
                
    # 레버로 가는 최단 거리 찾기
    steps_lever = bfs(maps, start, 'L')
    if steps_lever == -1:
        return -1
    
    # 출구로 가는 최단 거리 찾기
    steps_exit = bfs(maps, lever, 'E')
    if steps_exit == -1:
        return -1
    
    return steps_lever + steps_exit