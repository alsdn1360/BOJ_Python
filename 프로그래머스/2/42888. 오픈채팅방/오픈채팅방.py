def solution(record):
    answer = []
    uid = {}
    
    # 기록을 cmd로 전부 나눔
    for line in record:
        cmd = line.split()
        
        # Leave가 아니면 uid를 키로 name을 저장
        if cmd[0] != 'Leave':
            uid[cmd[1]] = cmd[2]
            
    for line in record:
        cmd = line.split()
        
        # Change가 아니면 기록을 answer에 저장
        if cmd[0] == 'Enter':
            answer.append(f"{uid[cmd[1]]}님이 들어왔습니다.")
        elif cmd[0] == 'Leave':
            answer.append(f"{uid[cmd[1]]}님이 나갔습니다.")
        
    return answer