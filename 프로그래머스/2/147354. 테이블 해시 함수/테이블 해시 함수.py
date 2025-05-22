def solution(data, col, row_begin, row_end):
    answer = 0
    
    # 조건에 맞게 정렬
    data.sort(key = lambda x : (x[col - 1], -x[0]))
    idx = row_begin
    
    for tupl in data[row_begin - 1 : row_end]:
        s_i = 0
        
        for data in tupl:
            s_i += data % idx
            
        # XOR 처리
        answer = answer ^ s_i
        
        idx += 1
    
    return answer