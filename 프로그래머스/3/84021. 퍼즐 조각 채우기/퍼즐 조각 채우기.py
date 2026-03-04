from collections import deque


MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def in_bound(n, nx, ny):
    return 0 <= nx < n and 0 <= ny < n


def bfs(n, sx, sy, matrix, visited, target):
    queue = deque([(sx, sy)])
    visited[sx][sy] = True
    
    piece = [(sx, sy)]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            
            if in_bound(n, nx, ny) and not visited[nx][ny] and matrix[nx][ny] == target:
                queue.append((nx, ny))
                visited[nx][ny] = True
                piece.append((nx, ny))
        
    return piece


def align(piece):
    min_x = min(p[0] for p in piece)
    min_y = min(p[1] for p in piece)
    
    aligned = [(x - min_x, y - min_y) for x, y in piece]
    
    return sorted(aligned)


def rotate(piece):
    # 90도 시계방향 회전 공식: (x, y) -> (y, -x)
    rotated = [(y, -x) for x, y in piece]
    
    return align(rotated)
    

def solution(game_board, table):
    n = len(game_board)
    
    # 빈 공간 찾기
    empty_pieces = []
    board_visited = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not board_visited[i][j]:
                piece = bfs(n, i, j, game_board, board_visited, 0)
                empty_pieces.append(align(piece))
          
    # 퍼즐 조각 찾기
    puzzle_pieces = []
    table_visited = [[False for _ in range(n)] for _ in range(n)]
                
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not table_visited[i][j]:
                piece = bfs(n, i, j, table, table_visited, 1)
                puzzle_pieces.append(align(piece))
                
    answer = 0
    used_puzzles = [False] * len(puzzle_pieces)
    
    for empty in empty_pieces:
        for i, puzzle in enumerate(puzzle_pieces):
            if used_puzzles[i]:
                continue
                
            if len(empty) != len(puzzle):
                continue
                
            can_use = False
            curr_puzzle = puzzle
            
            for _ in range(4):
                if empty == curr_puzzle:
                    can_use = True
                    break
                    
                curr_puzzle = rotate(curr_puzzle)
                
            if can_use:
                answer += len(empty)
                used_puzzles[i] = True
                break
                
    return answer
