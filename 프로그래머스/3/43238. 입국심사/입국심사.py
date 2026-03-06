def solution(n, times):
    answer = 0
    
    left, right = 0, max(times) * n
    
    while left <= right:
        mid  = (left + right) // 2
        
        judge = sum(mid // time for time in times)
        
        if judge >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
    