def solution(triangle):
    n = len(triangle)
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j, num in enumerate(triangle[i]):
            board[i][j] = num
    
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                board[i][j] += board[i - 1][j]
            else:
                board[i][j] += max(board[i - 1][j - 1], board[i - 1][j])   
    
    return max(board[n - 1])