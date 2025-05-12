MOVES = [(1, 0), (0, 1), (-1, -1)] # 하, 우, 좌상 대각선

def solution(n):
    if n == 1:
        return [1]
    
    answer = []
    
    snail = [[0 for _ in range(n)] for _ in range(n)]  # 달팽이를 채울 2차원 배열 초기화
    
    x, y = -1, 0 # 첫 좌표
    move_cnt, change_dirc_cnt, dirc = 0, n, 0 # 이동 횟수, 현재 이동 방향
    
    for i in range(1, n ** 2):
        if change_dirc_cnt == 1:
            break
            
        # 총 n번의 방향전환이 일어나는데, 이동횟수는 1씩 감소됨
        if move_cnt == change_dirc_cnt:
            change_dirc_cnt -= 1
            move_cnt = 0
            dirc = (dirc + 1) % 3
            
        # 이동방향 결정
        dx, dy = MOVES[dirc]
        nx, ny = x + dx, y + dy
        
        # 달팽이 채우기
        snail[nx][ny] = i
        
        # 현재 위치 및 이동 횟수 조정
        x, y = nx, ny
        move_cnt += 1
    
    for i in range(n):
        for j in range(n):
            if snail[i][j] != 0:
                answer.append(snail[i][j])
            
    return answer