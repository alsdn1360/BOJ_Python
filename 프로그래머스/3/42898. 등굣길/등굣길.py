MOD = 1000000007

def solution(m, n, puddles):
    # puddles의 좌표는 (x, y) 형태이므로 집합
    puddle_set = {(x, y) for x, y in puddles}
    
    # dp[i][j]: (j, i) 좌표까지 도달하는 경로의 수 (행: i, 열: j)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
                
            # 물 웅덩이인 경우 경로 수는 0
            if (j, i) in puddle_set:
                dp[i][j] = 0
            else:
                # 오른쪽이랑 아래로만 이동하니까, 왼쪽과 위에 있는 부분을 확인함
                up = dp[i - 1][j] if i > 1 else 0
                left = dp[i][j - 1] if j > 1 else 0
                
                dp[i][j] = (up + left) % MOD
                
    return dp[n][m]