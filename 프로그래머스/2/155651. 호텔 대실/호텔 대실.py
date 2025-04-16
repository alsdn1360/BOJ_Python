import heapq

def solution(book_time):
    answer = 0
    new_book_time = []
    
    # 현재 사용 중인 방
    using_room = []
    
    # 예약시간 분 단위로 변경
    for bt in book_time:       
        start_h, start_m = bt[0].split(':')
        end_h, end_m = bt[1].split(':')
        
        start = 60 * int(start_h) + int(start_m)
        end = 60 * int(end_h) + int(end_m) + 10 # 청소시간 10분 추가
        
        new_book_time.append([start, end])
        
    # 입실 시간을 기준으로 정렬
    new_book_time.sort(key = lambda x : x[0])
    
    # 첫 번째 예약의 퇴실 시간 삽입
    heapq.heappush(using_room, new_book_time[0][1])
    
    for i in range(1, len(new_book_time)):
        # 현재 예약의 입실 시간이 사용 중인 방의 가장 빠른 퇴실 시간보다 크면 방을 재활용할 수 있음
        if new_book_time[i][0] >= using_room[0]:
            heapq.heappop(using_room)
            
        # 이후에 현재 예약의 퇴실 시간 삽입
        heapq.heappush(using_room, new_book_time[i][1])
        
    # 사용 중인 방의 개수가 필요한 방의 개수
    return len(using_room)