from collections import deque
import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    
    jobs = deque(sorted(jobs))
    
    waiting_queue = []
    time = 0
    end_process_cnt = 0
    
    while end_process_cnt < n:
        while jobs and jobs[0][0] <= time:
            s, l = jobs.popleft()
            heapq.heappush(waiting_queue, (l, s))
            
        if waiting_queue:
            l, s = heapq.heappop(waiting_queue)
            time += l
            answer += time - s
            end_process_cnt += 1
        else: 
            if time < jobs[0][0]:
                time = jobs[0][0]
            
    return answer // n
