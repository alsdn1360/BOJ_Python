def solution(n):
    answer = 0
    
    # 투 포인터 사용
    i, j = 1, 1
    total = 0
    
    while i != n + 1:
        # 현재 합이 n보다 작으면 j 이동
        if total < n:
            total += j
            j += 1
        # 현재 합이 n이면 방법수 +1 하고, i 이동
        elif total == n:
            answer += 1
            
            total -= i
            i += 1
        # 현재 합이 n보다 작아질 때까지 i 이동
        else:
            total -= i
            i += 1
            
    return answer