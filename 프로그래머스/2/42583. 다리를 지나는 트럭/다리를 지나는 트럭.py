from collections import deque

def solution(bridge_length, weight, truck_weights):
    num_of_truck = len(truck_weights) # 트럭들이 전부 다리를 건넜는지 체크하기 위함
    
    waiting_truck = deque(truck_weights)
    crossing_truck = deque()
    crossing_truck_second = deque()
    crossed_truck = deque()
    
    seconds = 0
    current_bridge_weight = 0
    
    # 다리를 지난 트럭의 수와 대기했던 트럭의 수가 같으면 종료
    while len(crossed_truck) != num_of_truck:
        seconds += 1
        
        if crossing_truck:
            # 다리를 건너는 첫 번째 트럭이 다리 길이와 같으면 다 건넌 것이므로 다리를 지난 것으로 판단
            if crossing_truck_second[0] == bridge_length:
                crossing_truck_second.popleft()
                
                current_crossed_truck = crossing_truck.popleft()
                current_bridge_weight -= current_crossed_truck
                crossed_truck.append(current_crossed_truck)
            
            # 다리를 건너는 트럭이 1초마다 이동하기 때문에 1씩 증가
            for i in range(len(crossing_truck_second)):
                crossing_truck_second[i] += 1
            
        # 다리를 건너는 트럭의 무게와 대기 중인 첫 번째 트럭의 무게를 더했을 때, 한도 무게보다 작으면 추가
        if waiting_truck and current_bridge_weight + waiting_truck[0] <= weight:
            crossing_truck_second.append(1) 
            
            current_truck = waiting_truck.popleft()
            current_bridge_weight += int(current_truck)
            crossing_truck.append(int(current_truck))
        
    return seconds