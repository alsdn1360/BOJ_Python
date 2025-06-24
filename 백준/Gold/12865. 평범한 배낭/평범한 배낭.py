# main
n, k = map(int, input().split())

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    # 현재 물건의 무게, 가치
    w, v = map(int, input().split())

    for j in range(1, k + 1):
        # 현재 물건의 무게가 현재 배낭 최대 무게보다 크면
        if j < w:
            # 현재 물건 직전까지만 넣었을 때의 최대 가치
            dp[i][j] = dp[i - 1][j]
        else:
            # 현재 물건 직전까지만 넣었을 때의 최대 가치
            # vs
            # 현재 물건의 가치 + 현재 물건 직전까지만 넣었을 때의 가치
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[n][k])
