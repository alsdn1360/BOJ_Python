def solution(a):
    n = len(a)
    
    # 길이가 2 이하면 무조건 그 풍선들은 살아남음
    if n <= 2:
        return n
    
    # 하나의 기준에서 왼쪽에 대한 최솟값 구하기
    l_min = [0] * n
    l_min[0] = a[0]
    
    for i in range(1, n):
        l_min[i] = min(l_min[i - 1], a[i])
        
    # 하나의 기준에서 오른쪽에 대한 최솟값 구하기
    r_min = [0] * n
    r_min[n - 1] = a[n - 1]
    
    for i in range(n - 2, -1, -1):
        r_min[i] = min(r_min[i + 1], a[i])
        
    # 양쪽 끝은 무조건 살아남으므로 2에서 시작
    ans = 2
        
    for i in range(1, n - 1):
        if l_min[i - 1] > a[i] or r_min[i + 1] > a[i]:
            ans += 1
    
    return ans
