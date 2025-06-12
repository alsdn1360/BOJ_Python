import heapq

def solution(n, works):
    answer = 0
    
    heap = []
    
    # 맥스힙 만들기
    for work in works:
        heapq.heappush(heap, (-work, work))
    
    while n > 0:
        curr_work = heapq.heappop(heap)[1]
        
        if curr_work == 0:
            break
        elif curr_work > 0:
            curr_work -= 1
            heapq.heappush(heap, (-curr_work, curr_work))
            
        n -= 1
    
    for elem in heap:
        answer += elem[1] ** 2
        
    return answer
    