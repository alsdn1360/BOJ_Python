import heapq

def solution(jobs):
    n = len(jobs)
    
    jobs.sort(key = lambda x : x[0]) # 요청 시간 기준 정렬
    
    curr_time = 0 # 현재 시각
    waiting_time = 0 # 총 대기 시간
    
    complete_job_cnt = 0 # 완료한 작업 수
    idx = 0 # job의 인덱스
    
    queue = [] # 대기 큐
    
    while complete_job_cnt < n:
        
        # 현재 시간까지의 작업을 전부 대기 큐에 넣음
        while idx < n and jobs[idx][0] <= curr_time:
            s, l = jobs[idx]
            
            # 작업의 소요시간 순으로 대기 큐에서 처리해야 하므로 소요시간 기준으로 우선순위 정하게 함
            heapq.heappush(queue, (l, s))
            idx += 1
        
        if queue:
            l, s = heapq.heappop(queue)
            
            # 현재 시각에 소요된 시간 더하기
            curr_time += l

            # 반환 시간 더하기
            waiting_time += curr_time - s
            
            # 완료한 작업 수 처리
            complete_job_cnt += 1
        else:
            # 대기 큐에 작업이 없으면, 다음 작업 요청시간으로 옮김
            curr_time = jobs[idx][0]
    
    return waiting_time // n