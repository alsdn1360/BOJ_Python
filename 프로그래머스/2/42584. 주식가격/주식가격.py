def solution(prices):
    n = len(prices)
    
    answer = [0] * n
    stack = []
    
    for time, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            past_time = stack.pop()
            answer[past_time] = time - past_time
            
        stack.append(time)
        
    while stack:
        past_time = stack.pop()
        answer[past_time] = n - 1 - past_time
        
    return answer