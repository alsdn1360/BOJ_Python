from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    
    # 큐에 우선순위와 그때의 위치를 삽입
    for idx, priority in enumerate(priorities):
        queue.append((idx, priority))
        
    while queue:
        # 위치와 우선순위 팝
        l, p = queue.popleft()
        
        # 현재 우선순위가 가장 높은 것을 확인함
        high_p = max(priorities)
        
        # 현재 우선순위가 더 높은게 있다면 다시 삽입
        if high_p > p:
            queue.append((l, p))
        else:
            # 현재 우선순위랑 같거나 더 크면
            priorities.remove(high_p)
            answer += 1
            
            # 그때 원하는 위치면 리턴
            if location == l:
                return answer