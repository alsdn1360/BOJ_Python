def solution(elements):
    answer = set()
    
    n = len(elements)
    extended = elements * 2 # 원형 수열로 변경
    
    # 누적합 이용
    prefix = [0] * (2 * n + 1)
    
    for i in range(2 * n):
        prefix[i + 1] = prefix[i] + extended[i]
        
    for i in range(n):
        # 길이별로 누적합에서 값을 가져옴
        for length in range(1, n + 1):
            answer.add(prefix[i + length] - prefix[i])
            
    return len(answer)