def solution(routes):
    answer = 1
    
    # 고속도로 진출 지점을 기준으로 정렬
    routes.sort(key = lambda x : x[1])
    
    n = len(routes)
    
    # 우선 첫번째 차량의 진출 시점에 카메라를 설치함
    camera = routes[0][1]
    
    for i in range(1, n):
        # 그 다음 차량부터 카메라에 속하지 않으면
        if not routes[i][0] <= camera <= routes[i][1]:
            # 카메라를 하나 더 설치하고 다음 카메라를 그 차량의 진출 지점에 설치함
            answer += 1
            camera = routes[i][1]
        
    return answer