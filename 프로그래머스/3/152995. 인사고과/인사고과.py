def solution(scores):
    ans = 0
    
    # 합 구하기, 누가 완호인지 체크하기
    for i, score in enumerate(scores):
        score.append(sum(score))
        
        if i == 0:
            score.append(True)
        else:
            score.append(False)
        
    # 인센티브 누락 사원 체크하기
    scores.sort(key = lambda x : (-x[0], x[1]))
    
    curr_peer_score = scores[0][1]
    
    for score in scores: 
        if score[1] < curr_peer_score:
            if score[3]:
                return -1 # 완호가 인센티브 제외면 바로 -1 리턴
            
            score.append(False)
        else:
            curr_peer_score = score[1]
            score.append(True)
    
    # 석차 내기
    scores.sort(key = lambda x : -(x[0] + x[1]))
    
    rank = 1
    same_rank = 0
    curr_sum = scores[0][2]
    
    for i, score in enumerate(scores):
        # 인센티브 누락자
        if not score[4]:
            continue
            
        if score[2] < curr_sum:
            curr_sum = score[2]
            rank += same_rank
            same_rank = 0
        
        score.append(rank)
        same_rank += 1
    
    # 완호 석차 찾기
    for i, score in enumerate(scores):
        if score[3]:
            ans = score[5]
            break
    
    return ans