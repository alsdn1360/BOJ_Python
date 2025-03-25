def solution(number, k):  
    stack = []
    
    for num in number:
        # 왼쪽부터 돌면서 큰 숫자만 스택에 남게 함
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
            
        stack.append(num)
    
    # k가 남아있으면 뒤에서부터 빼줌
    if k > 0:
        for i in range(k):
            stack.pop()
            
    return ''.join(stack)