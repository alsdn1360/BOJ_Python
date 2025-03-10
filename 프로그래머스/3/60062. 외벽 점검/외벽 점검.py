from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    
    # 원형 구조를 선형 구조로 펼치기 위해 각 요소에 n을 더함
    for i in range(length):
        weak.append(weak[i] + n)
        
    # 투입할 친구의 최솟값 찾기위해 +1
    answer = len(dist) + 1
        
    for start in range(length):
        # 친구를 나열하는 모든 순열에 대해 확인
        for friends in permutations(dist, len(dist)):
            # 투입할 친구 수
            cnt = 1
            
            # 현재 친구가 출발 지점에서 시작하여 이동할 수 있는 최대 거리
            position = weak[start] + friends[cnt - 1]
            
            # 모든 취약점을 시작점으로 해서 확인
            for i in range(start, start + length):
                # 현재 친구가 다음 취약점까지 못가는 경우
                if position < weak[i]:
                    # 친구 한 명 더 투입
                    cnt += 1
                    
                    if cnt > len(dist):
                        break
                    
                    # 새로운 친구가 갈 수 있는 최대 거리 갱신
                    position = weak[i] + friends[cnt - 1]
                
            # 최솟값 선택
            answer = min(answer, cnt)
            
    return answer if answer <= len(dist) else -1
                