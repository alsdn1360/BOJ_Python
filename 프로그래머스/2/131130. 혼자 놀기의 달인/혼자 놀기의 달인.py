'''
1. 가능한 최고의 점수를 얻어야 함
2. 일단 그룹을 나눠야할 것 같음
3. 1번 그룹와 2번 그룹의 상자 개수로만 점수가 나옴
'''

def solution(cards):
    answer = 0
    
    opened = [False] * (len(cards) + 1)
    
    groups = []
    group_idx = 0
    
    for i, card in enumerate(cards):
        # 이미 열려있는 상자라면 패스
        if opened[card - 1]:
            continue
            
        group_cnt = 0
        
        curr_card_idx = i
        curr_card = card
        
        while not opened[curr_card_idx]:
            group_cnt += 1
            
            opened[curr_card_idx] = True
            
            curr_card_idx = curr_card - 1
            curr_card = cards[curr_card_idx]
            
        groups.append(group_cnt)
            
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            answer = max(answer, groups[i] * groups[j])
    
    return answer
