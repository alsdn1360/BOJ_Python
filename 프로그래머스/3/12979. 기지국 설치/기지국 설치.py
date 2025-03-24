import math

def solution(n, stations, w):
    answer = 0
    
    # 기지국 하나 당 전달할 수 있는 전파 범위
    wave_coverage = 2 * w + 1
    
    # 아파트 번호(첫 번째 아파트부터 시작)
    idx = 1
    
    for station in stations:
        # 초기에 설치되어 있는 기지국 커버 범위의 왼쪽
        wave_left = station - w
        
        if idx < wave_left:
            # idx부터 wave_left까지의 아파트를 커버할 수 있는 기지국 개수 세기
            # 범위보다 항상 더 많이 커버해야하기 때문에 ceil로 올림 처리
            answer += math.ceil((wave_left - idx) / wave_coverage)
        
        # 다음 아파트를 초기에 설치되어 있는 기지국 커버 범위의 오른쪽 다음으로 옮김
        idx = station + w + 1
        
    # 초기 기지국 오른쪽 처리
    if idx <= n:
        answer += math.ceil((n + 1 - idx) / wave_coverage)
        
    return answer