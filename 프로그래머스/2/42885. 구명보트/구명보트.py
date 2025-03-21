from collections import deque

def solution(people, limit):
    answer = 0
    
    # 무게 최소값과 최대값을 더하기 위해 정렬
    people.sort()
    queue = deque()
    
    for p in people:
        queue.append(p)
    
    while len(queue) > 1:
        # 무게 최대값과 최소값을 더해서 limit을 넘으면 무게 최대값을 가진 사람만 태워서 구출
        if queue[0] + queue[-1] > limit:
            queue.pop()
            answer += 1
        # 둘 다 합쳐서 limit을 안넘으면 둘 다 구출
        else:
            queue.pop()
            queue.popleft()
            answer += 1
            
    # 만약 한 명만 남아있으면 그 한 명만 구출
    if len(queue) == 1:
        answer += 1
        
    return answer