# picks: 다이아, 철, 돌 곡괭이의 개수
def solution(picks, minerals):
    answer = 0
    
    # 전체 곡괭이 수에 5를 곱한 만큼만 채굴(나머지 광물은 무시)
    total_picks = sum(picks)
    max_minerals = total_picks * 5
    minerals = minerals[:max_minerals]
    
    # 5개씩 그룹화
    groups = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    
    # 그룹별 곡괭이에 대한 피로도
    fati_groups = []
    
    for group in groups:
        # 각각의 곡괭이로 광물을 캤을 때, 발생하는 피로도 변수
        fati_dia = 0
        fati_iron = 0
        fati_stone = 0
        
        for mineral in group:
            if mineral == 'diamond':
                fati_dia += 1
                fati_iron += 5
                fati_stone += 25
            elif mineral == 'iron':
                fati_dia += 1
                fati_iron += 1
                fati_stone += 5
            else:
                fati_dia += 1
                fati_iron += 1
                fati_stone += 1
                
        fati_groups.append((fati_dia, fati_iron, fati_stone))
        
    # 돌 곡괭이 피로도 기준 내리차순 정렬
    fati_groups.sort(key = lambda x : x[2], reverse = True)
    
    # 다이아 곡괭이부터 그룹별 피로도 추가
    for fati in fati_groups:
        if picks[0] > 0:
            answer += fati[0]
            picks[0] -= 1
        elif picks[1] > 0:
            answer += fati[1]
            picks[1] -= 1
        elif picks[2] > 0:
            answer += fati[2]
            picks[2] -= 1
    
    return answer