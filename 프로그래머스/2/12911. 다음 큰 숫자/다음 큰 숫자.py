def solution(n):
    answer = 0
    
    b_n = str(format(n, 'b'))
    b_n_zero = b_n.count('1')
    
    nxt_n = n + 1
    
    while True:
        nxt_b_n = str(format(nxt_n, 'b'))
        nxt_b_n_cnt = nxt_b_n.count('1')
        
        if b_n_zero == nxt_b_n_cnt:
            return nxt_n
        else:
            nxt_n += 1
