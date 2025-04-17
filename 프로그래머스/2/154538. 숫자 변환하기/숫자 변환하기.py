from collections import deque

def solution(x, y, n):
    # BFS 사용
    queue = deque([(x, 0)])
    visited = set([x])
    
    while queue:
        curr_num, step = queue.popleft()
        
        if curr_num == y:
            return step
        
        # 연산 적용
        for cal_num in (curr_num + n, curr_num * 2, curr_num * 3):
            # y보다 작아야 큐에 삽입
            if cal_num not in visited and cal_num <= y:
                queue.append((cal_num, step + 1))
                visited.add(cal_num)
            
    return -1