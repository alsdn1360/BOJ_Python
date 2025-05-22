def solution(k, ranges):
    answer = []
    
    seq = [k]
    
    # 우박수열 좌표 만들기
    while k > 1:        
        if k % 2 == 0:
            k //= 2
        else:
            k = (3 * k) + 1
            
        seq.append(k)
        
    # 그래프의 누적합 구하기
    n = len(seq)
    prefix_sum = [0] * n
        
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + ((seq[i - 1] + seq[i]) / 2) # 사다리꼴 넓이 (높이는 1)
        
    for a, b in ranges:
        s = a
        e = n + b - 1
        
        if s > e:
            answer.append(-1.0)
        else:
            answer.append(prefix_sum[e] - prefix_sum[s])
            
    return answer