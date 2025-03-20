import heapq

def solution(operations):
    heap = []
    
    for operation in operations:
        cmd, num = operation.split()
        
        if cmd == 'I':
            # 우선순위큐로 삽입
            heapq.heappush(heap, int(num))
        elif cmd == 'D' and len(heap) != 0:
            if num == '-1':
                # 우선순위큐이므로 가장 작은 값 팝
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
                    
    if not heap:
        return [0, 0]
    
    return [max(heap), heap[0]]