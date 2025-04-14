def solution(m, n, startX, startY, balls):
    answer = []
    
    for a, b in balls:
        min_dist = float('inf')
        
        # 위로 튕길 때
        if not a == startX or not b > startY:
            dist = (a - startX) ** 2 + ((b + (n - b) * 2) - startY) ** 2
            min_dist = min(min_dist, dist)
        
        # 아래로 튕길 때
        if not a == startX or not b < startY:
            dist = (a - startX) ** 2 + ((-b) - startY) ** 2
            min_dist = min(min_dist, dist)
        
        # 왼쪽으로 튕길 때
        if not a < startX or not b == startY:
            dist = ((-a) - startX) ** 2 + (b - startY) ** 2
            min_dist = min(min_dist, dist)
        
        # 오른쪽으로 튕길 때
        if not a > startX or not b == startY:
            dist = ((a + (m - a) * 2) - startX) ** 2 + (b - startY) ** 2
            min_dist = min(min_dist, dist)
        
        answer.append(min_dist)
        
    return answer