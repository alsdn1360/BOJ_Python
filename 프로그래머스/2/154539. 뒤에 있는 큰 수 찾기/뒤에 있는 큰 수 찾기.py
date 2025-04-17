def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    # 모노토닉 감소 스택 사용
    stack = []
    
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            # 현재 값이 스택 최상단의 값보다 크면 팝
            idx = stack.pop()
            
            # 팝하면 이전의 인덱스가 나오고 그 인덱스에 현재 값을 입력
            answer[idx] = num
            
        stack.append(i)
        
    return answer