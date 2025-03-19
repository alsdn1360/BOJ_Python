# 전부 가로, 전부 세로, 가로 세로, 세로 가로

def solution(n):
    # n이 1이면 세로로 하나 두는 경우밖에 없음
    if n == 1:
        return 1
    
    # n이 2면 세로로 2개랑 가로로 두는 경우밖에 없음
    if n == 2:
        return 2
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    # n이 3이상일 때부턴 n - 1이랑 n - 2에서 사용했던 방식을 합쳐서 사용함
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
        
    return dp[n]