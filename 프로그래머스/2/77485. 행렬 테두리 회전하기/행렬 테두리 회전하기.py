def solution(rows, columns, queries):
    answer = []
    board = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    
    for q in queries:
        min_num = float('inf')
        
        x1, y1, x2, y2 = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1
        
        curr_x, curr_y = x1, y1 # 초기 위치
        
        move_r = x2 - x1 # 상, 하로 이동해야하는 횟수
        move_c = y2 - y1 # 좌, 우로 이동해야하는 횟수
        
        curr_num = 0
        temp_num = board[curr_x][curr_y]
        
        # 1. (y2 - y1) 만큼 우 이동
        for _ in range(move_c):
            curr_y += 1
            
            curr_num = board[curr_x][curr_y]
            board[curr_x][curr_y] = temp_num
            temp_num = curr_num
            
            min_num = min(min_num, curr_num)
            
        # 2. (x2 - x1) 만큼 하 이동
        for _ in range(move_r):
            curr_x += 1
            
            curr_num = board[curr_x][curr_y]
            board[curr_x][curr_y] = temp_num
            temp_num = curr_num
            
            min_num = min(min_num, curr_num)
            
        # 3. (y2 - y1) 만큼 좌 이동
        for _ in range(move_c):
            curr_y -= 1
            
            curr_num = board[curr_x][curr_y]
            board[curr_x][curr_y] = temp_num
            temp_num = curr_num
            
            min_num = min(min_num, curr_num)
            
        # 4. (x2 - x1) 만큼 상 이동
        for _ in range(move_r):
            curr_x -= 1
            
            curr_num = board[curr_x][curr_y]
            board[curr_x][curr_y] = temp_num
            temp_num = curr_num
            
            min_num = min(min_num, curr_num)
            
        answer.append(min_num)
        
    return answer
        