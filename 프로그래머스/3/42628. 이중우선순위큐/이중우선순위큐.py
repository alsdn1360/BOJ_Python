from collections import deque


def solution(operations):
    queue = deque()
    
    for operation in operations:
        command, num = operation.split(' ')
        num = int(num)
        
        if command == 'I':
            queue.append(num)
        elif command == 'D':
            if queue:
                if num == -1:
                    queue.popleft()
                elif num == 1:
                    queue.pop()

        queue = deque(sorted(queue))
        
    if not queue:
        return [0, 0]
    elif len(queue) == 1:
        return [queue[0], queue[0]]
    else:
        return [queue[-1], queue[0]]
    
    
    