from collections import deque

def solution(progresses, speeds):
    queue = deque()
    answer = []
    pre_feature = 0
    
    for i in range(len(progresses)):
        remain_progress = 100 - progresses[i]
        
        # 배포 가능 날짜를 구함
        deploy_day = remain_progress // speeds[i]
    
        # 날짜 올림 해줌
        if remain_progress % speeds[i] > 0:
            deploy_day += 1
            
        queue.append(deploy_day)
    
    while queue:
        feature = queue.popleft()
        
        # 이전에 배포한 날짜가 현재 배포한 날짜보다 크면 이후의 기능도 배포 가능하기 때문에 추가
        if feature <= pre_feature:
            deploy_feature += 1
        else:
            # 현재 배포한 날짜가 더 크기 때문에 아직 배포할 수 없어서 지금까지 배포한 기능의 수 추가
            if pre_feature != 0:
                answer.append(deploy_feature)
            
            pre_feature = feature
            deploy_feature = 1
    
    # 마지막으로 기능 수 추가
    answer.append(deploy_feature)
        
    return answer