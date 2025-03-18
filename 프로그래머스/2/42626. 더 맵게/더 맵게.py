import heapq

def solution(scoville, K):
    answer = 0
    n = len(scoville)
    
    # scoville을 우선순위 큐로 변경
    heapq.heapify(scoville)
    
    # 가장 작은 스코빌 지수가 K 보다 크거나 같을 때까지 반복
    while scoville[0] < K:
        # 계속 반복해도 모든 음식의 개수가 1이되면 K 이상으로 만들 수 없으므로 -1 리턴
        if len(scoville) == 1:
            return -1
        
        scoville1 = heapq.heappop(scoville)
        scoville2 = heapq.heappop(scoville)
        
        heapq.heappush(scoville, scoville1 + (scoville2 * 2))
        
        answer += 1
        
    return answer