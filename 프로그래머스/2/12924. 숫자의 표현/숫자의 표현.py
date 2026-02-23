def solution(n):
    answer = 0
    
    nums = [i for i in range(1, n + 1)]
    l, r = 0, 0
    
    curr_sum = sum(nums[l:r])
    
    while l < n and r <= n:            
        if curr_sum < n:
            curr_sum += nums[r]
            r += 1
        elif curr_sum > n:
            curr_sum -= nums[l]
            l += 1
        else:
            answer += 1
            curr_sum -= nums[l]
            l += 1
            
    return answer