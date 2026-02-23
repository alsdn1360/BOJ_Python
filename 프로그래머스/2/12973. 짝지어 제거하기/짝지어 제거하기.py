def solution(s):
    stack = []
    
    for alp in s:
        if stack and stack[-1] == alp:
            stack.pop()
        else:
            stack.append(alp)
            
    return 1 if not stack else 0
