def solve(sticker):
    n = len(sticker)
    
    dp = [0] * n
    
    dp[0] = sticker[0]
    dp[1] = max(dp[0], sticker[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i]) # 현재 스티커 선택 X vs 선택 O
        
    return max(dp)
    

def solution(sticker):
    if len(sticker) <= 2:
        return max(sticker)
        
    
    case1 = solve(sticker[:-1]) # 첫 번째 스티커를 뜯었을 때, 마지막 스티커는 선택 못하므로 아예 없앰
    case2 = solve(sticker[1:]) # 마지막 스티커를 뜯었을 때, 첫 번재 스티커는 선택 못하므로 아예 없앰
    
    return max(case1, case2)
