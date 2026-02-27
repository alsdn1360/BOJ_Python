from collections import defaultdict

def solution(nums):
    answer = 0
    
    choice_cnt = len(nums) // 2
    
    ponkemon = defaultdict(int)
    
    for num in nums:
        ponkemon[num] = 1

    for cnt in ponkemon.values():
        answer += 1
    
    return answer if answer <= choice_cnt else choice_cnt