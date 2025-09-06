def solution(n, money):    
    dp = [0] * (n + 1) # i원을 만들 수 있는 방법의 수
    dp[0] = 1 # 아무것도 안거슬러주면 0원이므로 방법은 1개
    
    for m in money:
        for i in range(m, n + 1):
            dp[i] += dp[i - m]
            
    return dp[n]
