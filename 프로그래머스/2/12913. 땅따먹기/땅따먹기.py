def solution(land):
    answer = 0

    N = len(land)
    
    # dp를 생성하고 첫번째 행을 land에서 가져옴
    dp = [[0] * 4 for _ in range(N)]
    dp[0] = land[0]
    
    # 두번째 행부터 시작
    for i in range(1, N):
        for j in range(4):
            for k in range(4):
                # 현재 열과 이전의 열이 같으면 패스
                if j == k:
                    continue
                    
                # 이전의 행에서 같은 열을 제외하고 값을 더해가며 최대값을 현재 위치에 삽입
                dp[i][j] = max(dp[i][j], land[i][j] + dp[i - 1][k]) 
            
    # 마지막 행에서 가장 큰 값 리턴
    return max(dp[N - 1])