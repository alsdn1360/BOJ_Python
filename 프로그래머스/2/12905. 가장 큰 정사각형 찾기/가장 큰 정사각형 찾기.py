def solution(board):
    answer = 0
    
    m = len(board)
    n = len(board[0])
    
    # 만약 board가 1칸이면 그 칸의 값을 출력
    if m * n == 1:
        return board[0][0]
    
    # dp 생성 및 첫 행과 첫 열 입력
    dp = [[0] * n for _ in range(m)]
    dp[0] = board[0]
    for i in range(1, m):
        dp[i][0] = board[i][0]
        
    # i, j를 정사각형의 오른쪽 아래 꼭지점이라고 생각
    for i in range(1, m):
        for j in range(1, n):
            # 그 꼭지점이 1일 때
            if board[i][j] == 1:
                # 그 꼭지점 근처의 점에서 만들 수 있는 정사각형 한 변의 길이의 최솟값에 1을 더함
                # 그러면 그 꼭지점에서 만들 수 있는 정사각형 한 변의 최소 길이가 나옴
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                
                # 그 중에서 가장 큰 한 변의 길이를 구함
                answer = max(answer, dp[i][j])
    
    # 정사각형의 넓이이므로 제곱해서 리턴
    return answer**2