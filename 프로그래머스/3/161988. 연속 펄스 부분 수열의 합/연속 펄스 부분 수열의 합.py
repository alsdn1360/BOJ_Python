def solution(sequence):
    n = len(sequence)
    
    positive_seq = [] # 처음에 1을 곱한 수열 : 1, -1, 1...
    negative_seq = [] # 처음에 -1을 곱한 수열 : -1, 1, -1...
    
    for i in range(n):
        num = sequence[i]
        
        if i % 2 == 0:
            positive_seq.append(num)
            negative_seq.append(num * (-1))
        else:
            positive_seq.append(num * (-1))
            negative_seq.append(num)
            
    dp = [0] * n      
    positive_dp = [0] * n
    negative_dp = [0] * n
    
    dp[0] = max(positive_seq[0], negative_seq[0])
    positive_dp[0] = positive_seq[0]
    negative_dp[0] = negative_seq[0]
    
    for i in range(1, n):
        positive_dp[i] = max(positive_seq[i], positive_seq[i] + positive_dp[i - 1])
        negative_dp[i] = max(negative_seq[i], negative_seq[i] + negative_dp[i - 1])
        
        dp[i] = max(positive_dp[i], negative_dp[i])
        
    return max(dp)