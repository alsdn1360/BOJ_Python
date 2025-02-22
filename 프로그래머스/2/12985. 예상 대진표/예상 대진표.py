def solution(n,a,b):
    answer = 0
    
    # 다음 라운드에서 받을 번호가 같으면 같은 라운드에 진출한 것임
    while a != b:
        # 승리했을 때 다음 라운드에서 받게될 번호 계산
        a = (a + 1) // 2
        b = (b + 1) // 2
        
        answer += 1
        
    return answer