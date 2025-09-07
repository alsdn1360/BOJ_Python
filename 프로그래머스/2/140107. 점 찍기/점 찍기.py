from math import sqrt, floor

def solution(k, d):
    ans = 0
    
    max_y = []
    
    # 고정된 x 값에 대해서 y의 최대값들
    for x in range(0, d + 1, k):
        max_y.append(floor(sqrt(d ** 2 - x ** 2)))
        
    # 그 y의 최대값에 대해서 가능한 y의 개수
    for y in max_y:
        ans += y // k + 1
    
    return ans
