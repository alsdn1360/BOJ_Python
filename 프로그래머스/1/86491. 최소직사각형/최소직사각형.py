def solution(sizes):
    answer = 0
    
    # 가로, 세로 값을 각각 하나의 리스트에 저장하기 위함
    r_sizes = [[] for _ in range(2)]
    
    n = len(sizes)
    
    # 작은 값은 가로에 넣고 큰 값은 세로에 넣음
    for i in range(n):
        if sizes[i][0] > sizes[i][1]:
            r_sizes[0].append(sizes[i][1])
            r_sizes[1].append(sizes[i][0])
        else:
            r_sizes[0].append(sizes[i][0])
            r_sizes[1].append(sizes[i][1])
    
    return max(r_sizes[0]) * max(r_sizes[1])