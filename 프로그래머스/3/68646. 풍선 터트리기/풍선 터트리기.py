def solution(a):
    n = len(a)
    
    # 길이가 2 이하면 무조건 그 풍선들은 살아남음
    if n <= 2:
        return n
    
    survive_idx = set()
    
    min_num = a[0]
    
    for i in range(n):
        # 가장 작은 값이 자기자신일 수도 있음
        if min_num >= a[i]:
            min_num = a[i]
            survive_idx.add(i)
            
    min_num = a[-1]
    
    for i in range(n - 1, -1, -1):
        # 가장 작은 값이 자기자신일 수도 있음
        if min_num >= a[i]:
            min_num = a[i]
            survive_idx.add(i)
            
    return len(survive_idx)