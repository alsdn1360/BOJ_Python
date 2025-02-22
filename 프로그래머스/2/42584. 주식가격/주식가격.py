def solution(prices):
    n = len(prices)
    stack = [] # prices의 인덱스가 들어감
    seconds = [0] * n
    
    # i는 현재 시간
    for i in range(n):
        # 스택이 비어있지 않고
        # 현재 시간의 가격이 스택의 최상위 인덱스의 가격보다 작으면 가격이 떨어진 것
        while stack and prices[stack[-1]] > prices[i]:
            index = stack.pop()
            seconds[index] = i - index # 현재 시간 - 이전의 인덱스(최상위 인덱스)
            
        stack.append(i)
    
    # 스택에 남아있는 인덱스 처리
    while stack:
        index = stack.pop()
        seconds[index] = n - index - 1 # 현재 위치를 제외하고 남은 시간을 위해 -1을 함
                
    return seconds