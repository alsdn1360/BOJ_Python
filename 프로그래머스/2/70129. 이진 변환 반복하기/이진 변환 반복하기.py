def solution(s):
    answer = []
    
    bin_cnt = 0
    total_zero_cnt = 0
    
    while len(s) > 1:        
        bin_cnt += 1
        total_zero_cnt += s.count('0')
        
        c = s.count('1')
        x = format(c, 'b')
        s = str(x)

    return [bin_cnt, total_zero_cnt]