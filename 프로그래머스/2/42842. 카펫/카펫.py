import math

def solution(brown, yellow):
    # 카펫 전체 면적은 갈색과 노란색 격자의 합
    area = brown + yellow
    
    # 가로와 세로의 최솟값은 3
    for h in range(3, area):
        # 나눴을 때, 가로 길이가 정수가 아니면 패스
        if area % h != 0:
            continue
            
        # 가로 구하기
        w = area // h
        
        # 가로가 세로보다 작으면 패스
        if w < h:
            continue
            
        # 갈색 = 가로와 세로 둘 다 두 줄씩 가지고 있어서 2 * (w + h), 각 꼭지점을 빼야하므로 -4
        # 노란색 = 양 옆에 테두리를 제외한 가로, 세로를 곱한 값
        if 2 * (w + h) - 4 == brown and (w - 2) * (h - 2) == yellow:
            return [w, h]