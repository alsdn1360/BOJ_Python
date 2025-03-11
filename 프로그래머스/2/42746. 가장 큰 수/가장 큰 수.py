def solution(numbers):
    numbers = list(map(str, numbers))
    
    # 문자열로 변환해서 사전식으로 비교해서 정렬함
    # 예를 들어, 3 과 30이 있으면 333과 303030 중에서 사전식으로 비교하면 333이 303030보다 먼저 오므로, 333 더 큼
    numbers.sort(key = lambda x : x * 3, reverse = True)
    
    answer = "".join(numbers)
    
    # 0이 주어지면 0으로 반환해야 함
    return '0' if answer[0] == '0' else answer