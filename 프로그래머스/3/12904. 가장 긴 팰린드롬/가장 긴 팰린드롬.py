def solve(s, l, r):
    while 0 <= l and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
        
    return r - l - 1
        
        
def solution(s):    
    ans = 1 # 문자 한 개도 팰린드롬이 될 수 있음
    
    for i in range(len(s) - 1):
        odd_ans = solve(s, i, i) # 홀수 팰린드롬 (ex. aba)
        even_ans = solve(s, i, i + 1) # 짝수 팰린드롬 (ex. abba)
        
        ans = max(ans, odd_ans, even_ans)
    
    return ans
