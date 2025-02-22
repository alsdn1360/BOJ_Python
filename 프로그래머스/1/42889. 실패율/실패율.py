def solution(N, stages):
    # 스테이지별 도전자 수
    challenger = [0] * (N + 2)
    for stage in stages:
        challenger[stage] += 1
        
    # 스테이지별 실패한 도전자 수
    fails = {}
    total = len(stages)
    
    # 스테이지별 실패율 계산
    for i in range(1, N + 1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            
            # 다음 스테이지의 실패율을 위한 도전자 수
            total -= challenger[i]
            
    # 딕셔너리를 정렬하는 방법임
    answer = sorted(fails, key = lambda x : fails[x], reverse = True)
    
    return answer