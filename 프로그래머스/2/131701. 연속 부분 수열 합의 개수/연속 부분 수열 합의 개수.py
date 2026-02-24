def solution(elements):
    answer = set()
    
    n = len(elements)
    elements *= 2
    
    prefix = [0] * (2 * n + 1)
    
    for i in range(2 * n):
        prefix[i + 1] = prefix[i] + elements[i]
    
    for i in range(n):
        for l in range(1, n + 1):
            answer.add(prefix[i + l] - prefix[i])
            
    return len(answer)
