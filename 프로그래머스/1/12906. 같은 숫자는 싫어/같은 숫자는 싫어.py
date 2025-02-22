def solution(arr):
    stack = []
    
    for i in arr:
        if not stack:
            stack.append(i)
        else:
            if not stack[-1] == i:
                stack.append(i)
            
    return stack
            