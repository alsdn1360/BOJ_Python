from collections import deque

def solution(order):
    answer = 0
    n = len(order)

    first_belt = deque(range(1, n + 1)) # 컨테이너 벨트
    second_belt = [] # 보조 컨테이너 벨트(스택)
    
    for box in order:
        #  두 번째 컨테이너 벨트에 상자가 있으면 바로 팝
        if second_belt and second_belt[-1] == box:
            second_belt.pop()
            answer += 1
            continue
        
        # 두 번째 컨테이너 벨트에 상자를 넣음
        while first_belt and first_belt[0] != box:
            second_belt.append(first_belt.popleft())
        
        # 넣어야 할 박스 차례면 팝
        if first_belt and first_belt[0] == box:
            first_belt.popleft()
            answer += 1
        # 첫 번째 컨테이너에도 없고 보조 컨테이너에도 없으면 중단
        else:
            break
            
    return answer