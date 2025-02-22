def solution(s):
    arr = list(s.split())
    stack = []
    answer = 0

    for i in arr:
        if i == 'Z':
            answer -= stack.pop()
        else:
            answer += int(i)
            stack.append(int(i))
            
    return answer