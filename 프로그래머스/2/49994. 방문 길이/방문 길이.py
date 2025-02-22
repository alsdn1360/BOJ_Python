# 좌표를 벗어나는지 확인하는 함수
def is_vaild_move(nx, ny):
    return 0 <= nx < 11 and 0 <= ny < 11

# 좌표 이동 함수
def move_location(x, y, dir):
    if dir == 'U':
        nx, ny = x, y + 1
    elif dir == 'D':
        nx, ny = x, y - 1
    elif dir == 'L':
        nx, ny = x - 1, y
    elif dir == 'R':
        nx, ny = x + 1, y
        
    return nx, ny

def solution(dirs):
    x, y = 5, 5
    answer = set() # 중복 방지를 위해 set으로 선언
    
    for dir in dirs:
        nx, ny = move_location(x, y, dir)
        
        if not is_vaild_move(nx, ny):
            continue
            
        # 아래 코드는 (x,y)에서 (nx,ny)로 이동했다는 것을 의미함
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        
        x, y = nx, ny
        
    return len(answer) / 2