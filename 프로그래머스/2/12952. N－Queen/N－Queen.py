def solution(n):    
    board = [-1] * n
    
    def check_queen(row, col):
        # board[i]는 그 행에 놓여진 퀸의 열 정보를 가지고 있음
        for i in range(row):
            # 현재 검사하려는 col과 같다면, 같은 열에 퀸이 있다는 뜻
            # 왼쪽 위 대각선상에 있는 모든 칸은 '열 번호 - 행 번호'가 동일함 => ex) (0,0), (1,1), (2,2)는 모두 '열 - 행 = 0'
            # 오른쪽 위 대각선상에 있는 모든 칸은 '열 번호 + 행 번호'가 동일함 => ex) (0,3), (1,2), (2,1), (3,0)은 모두 '열 + 행 = 3'
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
            
        return True
    
    def place_queen(row):
        if row == n:
            return 1
        
        answer = 0
        
        for col in range(n):
            if check_queen(row, col):
                # 현재 행에 퀸을 배치한 열 값을 저장
                board[row] = col
                
                # 다음 행으로 이동해서 퀸을 배치
                answer += place_queen(row + 1)

        return answer
    
    # 0번째 행부터 배치 시작
    return place_queen(0)
                
            