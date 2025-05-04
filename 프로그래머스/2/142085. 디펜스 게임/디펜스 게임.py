import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    
    # 두 가지 경우가 있음 => 1. 병사 사용 2. 무적권 사용
    for e in enemy:
        if n < e and k == 0:
            return answer
        
        # 맥스 힙 사용
        heapq.heappush(heap, (-e, e))
            
        if n >= e:
            # 병사 사용
            n -= e
            answer += 1
        else:
            if heap and k != 0:
                # 무적권 사용 -> 이전 라운드에서 가장 많이 사용한 병사 되돌리기
                k -= 1
                n += heapq.heappop(heap)[1]
                
                # 되돌린 병사로 현재 라운드 막기
                n -= e
                answer += 1
                
    return answer
