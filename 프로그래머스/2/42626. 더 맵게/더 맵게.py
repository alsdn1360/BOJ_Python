import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville:
        first_s = heapq.heappop(scoville)
        
        if first_s >= K:
            return answer
        
        if not scoville:
            return -1
            
        second_s = heapq.heappop(scoville)
                           
        heapq.heappush(scoville, first_s + (second_s * 2))
        answer += 1
                           
    return -1