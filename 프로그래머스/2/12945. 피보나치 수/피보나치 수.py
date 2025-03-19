def solution(n):
    # 메모이제이션
    fibo = [0, 1]
    
    for i in range(2, n + 1):
        fibo.append((fibo[i - 1]) + fibo[i - 2])
        
    return fibo[n] % 1234567