def check_bingo(board, mark):
    # 열 확인
    for i in range(3):
        if board[i][0] == mark and board[i][1] == mark and board[i][2] == mark:
            return True
        
    # 행 확인
    for j in range(3):
        if board[0][j] == mark and board[1][j] == mark and board[2][j] == mark:
            return True
        
    # \ 대각선 확인
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    
    # / 대각선 확인
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    
    return False

def solution(board):
    n_board = [list(elem) for elem in board]
    
    cnt_o = 0
    cnt_x = 0
    
    # O와 X 카운트
    for i in range(3):
        for j in range(3):
            if n_board[i][j] == 'O':
                cnt_o += 1
            elif n_board[i][j] == 'X':
                cnt_x += 1
        
    # 아직 진행을 안했으니 항상 정상
    if cnt_o + cnt_x == 0:
        return 1
    
    # O랑 X의 개수는 항상 같거나, O가 한개 더 많아야 함
    if not (cnt_o == cnt_x or cnt_o == cnt_x + 1):
        return 0
    
    # O와 X 빙고 확인
    bingo_o = check_bingo(n_board, 'O')
    bingo_x = check_bingo(n_board, 'X')
    
    # 둘 다 이기면 비정상
    if bingo_o and bingo_x:
        return 0
    # O가 이겼는데, 개수가 같으면 비정상
    elif bingo_o and cnt_o != cnt_x + 1:
        return 0
    # X가 이겼는데, O의 개수가 1개 더 많으면 비정상(X가 후공이니까 X가 이기면 개수가 같아져야 함)
    elif bingo_x and cnt_o != cnt_x:
        return 0
    
    return 1
    