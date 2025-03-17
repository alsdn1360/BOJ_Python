def solution(n):
    answer = 1
    
    while True:
        if n == 1:
            return answer
        
        # n이 짝수면 점프할 필요없이 순간이동함
        if n % 2 == 0:
            n = n / 2
        # n이 홀수면 한 칸 점프하고 순간이동함
        else:
            answer += 1
            # 점프하기 때문에 n-1
            n = (n - 1) / 2