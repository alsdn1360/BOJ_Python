def solution(A, B):
    # 아예 이길 수 없으면 0 리턴
    if min(A) > max(B):
        return 0
    
    answer = 0
    
    A.sort()
    B.sort()
    
    n = len(A)

    b_idx = 0
    
    # A의 낮은 수부터 B의 가장 작은 수로 이길 수 있는 수를 내면 됨
    for a_idx in range(n):
        if b_idx == n:
            break
            
        while b_idx < n and B[b_idx] <= A[a_idx]:
            b_idx += 1
        
        if b_idx < n and B[b_idx] > A[a_idx]:
            answer += 1
            b_idx += 1
    
    return answer 
    