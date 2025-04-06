def solution(N, number):
    # 1개부터 8개까지의 N으로 만들 수 있는 모든 결과(집합) 저장 리스트
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        # 이어붙인 숫자
        dp[i].add(int(str(N) * i))
        
        for j in range(1, i):
            # 이전의 개수를 합쳐서 i개로 만들 수 있는 경우를 구함
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    # 사칙연산
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    
                    if num2 != 0:
                        dp[i].add(num1 // num2)
                        
        # 타겟이 dp의 i 인덱스에 있으면 N을 i번 사용한 것
        if number in dp[i]:
            return i
    
    # dp 안에 없으면 최솟값이 8보다 크므로 -1
    return -1       