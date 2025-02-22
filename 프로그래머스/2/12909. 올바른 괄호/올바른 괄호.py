def solution(s):
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
                
    if not stack: # 스택이 비어있다면
        return True
    else:
        return False