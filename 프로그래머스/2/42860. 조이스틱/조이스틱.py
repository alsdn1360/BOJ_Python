def solution(name):
    answer = 0
    n = len(name)
    
    for alpha in name:
        # 위로 움직이는 경우나, 아래로 움직이는 경우 중에 최소값 찾음
        answer += min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1)
    
    move = n - 1
    
    for idx in range(n):
        next_idx = idx + 1
        
        # 연속된 A 찾기
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
            
        # 연속된 A가 있을 때, 왼쪽으로 가는게 더 빠른지, 오른쪽으로 계속 가는게 더 빠른지 비교
        distance = min(idx, n - next_idx) # 시작점까지의 거리 비교: 오른쪽 vs 왼쪽
        move = min(move, idx + distance + (n - next_idx)) # 최소 거리 비교: 지금까지 최소 vs 왼쪽(처음부터 idx까지 + 처음으로 돌아가는 거리 - 끝에서부터 다음 idx까지)
        
    answer += move
    
    return answer