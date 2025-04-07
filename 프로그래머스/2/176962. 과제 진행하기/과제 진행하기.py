def solution(plans):
    answer = []
    
    # 잠시 멈춘 과제
    pause = []
    
    # hh:mm을 전부 분으로 만듦
    for plan in plans:
        h, m = plan[1].split(':')
        
        plan[1] = (int(h) * 60) + int(m)
        plan[2] = int(plan[2])
    
    # 시작 시간 기준으로 정렬
    plans.sort(key = lambda x : x[1])
    
    for i in range(len(plans)):
        name, start, playtime = plans[i]
        
        # 마지막 과제면 바로 끝낼 수 있음
        if i == (len(plans) - 1):
            answer.append(name)
        else:
            next_start = plans[i + 1][1]
            
            # 바로 과제를 끝낼 수 있는 경우
            if start + playtime <= next_start:
                answer.append(name)
                
                # 과제하고 나서 남은 시간
                remaining_time = next_start - (start + playtime)
                
                # 남은 시간에 멈춰놓은 과제를 처리해야 함
                while remaining_time > 0 and pause:
                    pause_name, pause_playtime = pause.pop()
                    
                    if remaining_time >= pause_playtime:
                        answer.append(pause_name)
                        remaining_time -= pause_playtime
                    else:
                        pause.append((pause_name, pause_playtime - remaining_time))
                        remaining_time = 0
            # 바로 과제 못 끝내는 경우
            else:
                pause.append((name, playtime - (next_start - start)))
                
    # 남아있는 과제 처리
    while pause:
        pause_name, _ = pause.pop()
        answer.append(pause_name)
            
    return answer