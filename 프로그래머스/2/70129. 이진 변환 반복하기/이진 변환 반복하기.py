def solution(s):
    answer = []

    trans_cnt = 0
    zero_cnt = 0
    
    while len(s) > 1:
        # 이진 변환 횟수
        trans_cnt += 1
        
        # 제거할 0의 개수
        zero_cnt += s.count('0')
        
        # 0 제거 후 길이
        s = s.replace('0', '')
        c = len(s)
        
        # 2진수 변환
        s = format(c, 'b')
        
    answer.append(trans_cnt)
    answer.append(zero_cnt)
    
    return answer