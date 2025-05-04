import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    
    for e in enemy:
        # 병사 사용
        n -= e
        
        # 맥스힙 푸시
        heapq.heappush(heap, -e)
        
        if n < 0:
            if k > 0:
                # 무적권 사용
                n += -heapq.heappop(heap)
                k -= 1
            else:
                # 모든 라운드를 막지 못했을 때, 종료
                return answer
            
        answer += 1
        
    # 모든 라운드를 막고 종료
    return answer
        