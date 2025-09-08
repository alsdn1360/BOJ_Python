def solution(n, l, r):
    ans = 0
    
    for i in range(l - 1, r):
        k = i
        
        is_zero = False
        
        while k > 0:
            # 11011에서 5로 나눈 나머지가 2면 무조건 0임
            # 11011 11011 00000 11011 11011에서 5로 나눈 몫에서 5로 나눈 나머지가 2여도 무조건 0임
            if k % 5 == 2 or (k // 5) % 5 == 2:
                is_zero = True
                break
                
            k = k // 5
            
        if not is_zero:
            ans += 1
        
    return ans
