# 입력된 괄호를 왼쪽으로 x 만큼 회전하는 함수
def rotate(s, x):
    return s[x:] + s[:x]

# 괄호의 짝이 맞는지 확인하는 함수
def check(s):
    stack = []
    
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c) # 여는 괄호이면 스택에 푸시
        else:
            if not stack: # 스택이 비어있으면 False 리턴
                return False
            
            if c == ')' and stack[-1] == '(': # ) 일 때, 스택의 최상위 항목이 ( 이면 팝
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
    
    if stack: # 스택이 비어있지 않으면 False 리턴
        return False
    else:
        return True

def solution(s):
    answer = 0
    rotate_s = []
    
    for i in range(len(s)):
        rotate_s = rotate(s, i)
        
        if check(rotate_s):
            answer += 1
            
    return answer
