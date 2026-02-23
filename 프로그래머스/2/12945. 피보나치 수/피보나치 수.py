def solution(n):
    fibo = [0] * (n + 1)
    fibo[0], fibo[1] = 0, 1
    
    for i in range(2, n + 1):
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 1_234_567
        
    return fibo[n]
    