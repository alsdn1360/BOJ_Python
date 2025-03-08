def solution(n, info):
    max_diff = 0
    max_r_info = []
    
    # 화살 점수, 남은 화살 수, 라이언이 맞힌 화살 개수 배열
    def dfs(idx, arrows, r_info):
        nonlocal max_diff, max_r_info
        
        # 종료 조건
        if idx == 11 or arrows == 0:
            # 화살이 남아있으면 0점에 몰아줌
            # 가장 낮은 점수를 더 많이 맞힌 경우를 리턴해야하기 때문
            if arrows > 0:
                temp_r_info = r_info[:]
                temp_r_info[10] = arrows
            else:
                temp_r_info = r_info[:]
                
            r_score = 0
            a_score = 0

            for i in range(11):
                if temp_r_info[i] > info[i]:
                    # 점수가 10점부터 0점까지 있는 배열이므로 10에서 i를 빼줌
                    r_score += 10 - i
                elif info[i] > 0:
                    a_score += 10 - i

            # 라이언이 어피치를 이겼을 때
            if r_score > a_score:
                diff = r_score - a_score

                # 현재 점수차가 이전의 최대 점수차보다 크면
                if diff > max_diff:
                    # 그 점수차를 최대 점수차로 만듦
                    max_diff = diff
                    max_r_info = temp_r_info[:]
                elif diff == max_diff:
                    # 점수차가 같으면 더 낮은 점수를 많이 맞힌 경우를 선택해야 함
                    for i in range(10, -1, -1):
                        if temp_r_info[i] > max_r_info[i]:
                            max_r_info = temp_r_info[:]
                            break
                        elif max_r_info[i] > temp_r_info[i]:
                            break

            return
        
        # 현재 점수 선택
        if arrows >= info[idx] + 1:
            # 어치피보다 한 개 더 많이 맞혀야하므로 +1
            r_info[idx] = info[idx] + 1
            
            # 방금 화살을 썼으므로 남은 화살 개수에서 빼줌
            dfs(idx + 1, arrows - (info[idx] + 1), r_info)
            
            # 백트래킹
            r_info[idx] = 0
            
        # 현재 점수 포기
        dfs(idx + 1, arrows, r_info)
        
    dfs(0, n, [0] * 11)
    
    return max_r_info if max_r_info else [-1]