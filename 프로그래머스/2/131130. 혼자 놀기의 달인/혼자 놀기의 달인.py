def solution(cards):   
    opened = [False] * (len(cards))
    groups = []
    
    for i, card in enumerate(cards):
        # 이미 열려있는 상자라면 패스
        if opened[i]:
            continue
            
        group_cnt = 0
        curr_idx = i
        
        while not opened[curr_idx]:
            opened[curr_idx] = True
            
            group_cnt += 1
            curr_idx = cards[curr_idx] - 1
            
        groups.append(group_cnt)
        
    # 가장 큰 값 두개만 찾으면 됨
    groups.sort(reverse = True)
    
    # 그룹이 하나밖에 없을 때 점수는 0
    return groups[0] * groups[1] if len(groups) > 1 else 0
