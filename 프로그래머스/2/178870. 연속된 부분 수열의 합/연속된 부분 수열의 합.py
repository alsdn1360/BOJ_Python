def solution(sequence, k):
    n = len(sequence)
    answer = [0, n]
    
    # 투 포인터 사용
    l, r = 0, 0
    curr_sum = sequence[l]
    
    while r < n:
        if curr_sum == k:
            if (r - l) < answer[1] - answer[0]:
                answer = [l, r]
                
            curr_sum -= sequence[l]
            l += 1
        elif curr_sum < k:
            r += 1    
            
            if r < n:
                curr_sum += sequence[r]
        else:
            # curr_sum이 k보다 작아질 때까지 왼쪽 포인터 인덱스 값을 빼줌
            curr_sum -= sequence[l]
            l += 1
            
    return answer
        