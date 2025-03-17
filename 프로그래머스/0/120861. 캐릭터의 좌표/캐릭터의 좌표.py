# 상, 하, 좌, 우
MOVES = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def solution(keyinput, board):
    # 보드의 중앙값
    mid_w, mid_h = (board[0] - 1) // 2, (board[1] - 1) // 2
    
    # 캐릭터의 첫 좌표
    x, y = mid_w, mid_h
    
    for command in keyinput:
        if command == 'up':
            dx, dy = MOVES[0]
        elif command == 'down':
            dx, dy = MOVES[1]
        elif command == 'left':
            dx, dy = MOVES[2]
        elif command == 'right':
            dx, dy = MOVES[3]
            
        # 새로운 좌표로 이동예측
        nx, ny = x + dx, y + dy
            
        # 새로운 좌표가 보드의 크기보다 작아야 새로운 좌표로 이동
        if 0 <= nx < board[0] and 0 <= ny < board[1]:
            x, y = nx, ny
            
    # (0, 0)이 보드의 중앙이므로 보드의 중앙값을 빼줌
    return [x - mid_w, y - mid_h]