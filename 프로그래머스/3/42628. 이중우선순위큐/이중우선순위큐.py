import heapq


def pop_max(heap):
    temp_heap = []
                    
    while heap:
        heapq.heappush(temp_heap, -heapq.heappop(heap))

    max_num = -heapq.heappop(temp_heap)

    while temp_heap:
        heapq.heappush(heap, -heapq.heappop(temp_heap))
        
    return max_num, heap


def solution(operations):
    heap = []
    
    for operation in operations:
        command, num = operation.split(' ')
        
        if command == 'I':
            heapq.heappush(heap, int(num))
        elif command == 'D':
            if heap:
                if num == '-1':
                    heapq.heappop(heap)
                elif num == '1':
                    _, heap = pop_max(heap)
    
    if not heap:
        return [0, 0]
    elif len(heap) == 1:
        num = heapq.heappop(heap)
        
        return [num, num]
    else:
        max_num, heap = pop_max(heap)
        min_num = heapq.heappop(heap)
        
        return [max_num, min_num]
    