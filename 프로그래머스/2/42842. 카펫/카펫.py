def solution(brown, yellow):
    # 전체 면적
    area = brown + yellow
    
    # 수학적 특성을 활용한 최적화: 제곱근까지만 탐색
    # 가로 >= 세로이므로 세로는 최대 √area까지만 확인하면 됨
    for h in range(3, int(area**0.5) + 1):
        if area % h != 0:
            continue
            
        w = area // h
        
        # 갈색 테두리와 노란색 내부 격자 수 검증
        if 2 * (w + h) - 4 == brown and (w - 2) * (h - 2) == yellow:
            return [w, h]