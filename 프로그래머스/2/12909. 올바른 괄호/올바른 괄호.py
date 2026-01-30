def solution(s):
    stack = []
    
    for p in s:   
        if stack and stack[-1] == '(' and p == ')' :
            stack.pop()
            
            continue
            
        stack.append(p)
                    
    return True if not stack else False
        