def solution(n, k, cmd):
    deleted = []
    
    # 링크드 리스트 이용
    # 각 행 위아래의 행의 인덱스를 저장
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]
    
    # 현재 인덱스 위치
    k += 1
    
    for cmd_i in cmd:
        if cmd_i == 'C':
            deleted.append(k)
            # 만약 k = 2에서 up이 1, down이 3이었을 때, k = 1의 down에 3을 전달하고 k = 3의 up에 1을 전달함
            up[down[k]] = up[k] # 삭제한 행이 가지고 있던 up 정보를 아래의 행에 그대로 전달
            down[up[k]] = down[k] # 삭제한 행이 가지고 있던 down 정보를 위의 행에 그대로 전달
            
            if n < down[k]:
                k = up[k]
            else:
                k = down[k]
            
        elif cmd_i == 'Z':
            undo = deleted.pop()
            up[down[undo]] = undo
            down[up[undo]] = undo
            
        else:
            action, num = cmd_i.split()
            
            if action == 'U':
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]
                    
                    
    answer = ['O'] * n
    
    while deleted:
        answer[deleted.pop() - 1] = 'X'
        
    return ''.join(answer)
    