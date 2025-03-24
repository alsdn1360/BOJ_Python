def solution(n, lost, reserve):
    answer = 0
    
    student = [1] * (n + 1)
    student[0] = 0
    
    # 체육복 도난 학생 처리
    for l in lost:
        student[l] -= 1
    
    # 여벌 체육복이 있는 학생 처리
    for r in reserve:
        student[r] += 1
        
    for i in range(1, n + 1):
        # 여벌 체육복이 있는 학생만
        if student[i] >= 2:
            # 앞 학생
            if i > 1 and student[i - 1] == 0:
                student[i] -= 1
                student[i - 1] += 1
            # 뒤 학생
            elif i < n and student[i + 1] == 0:
                student[i] -= 1
                student[i + 1] += 1
                
    for i in range(1, n + 1):
        if student[i] > 0:
            answer += 1
    
    return answer