# main
n, k = map(int, input().split())

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

# i: 현재 고려하는 물건의 인덱스
for i in range(1, n + 1):
    # 현재 물건의 무게, 가치
    w, v = map(int, input().split())

    # j: 배낭의 용량
    for j in range(1, k + 1):
        # 현재 물건을 담을 수 없는 경우
        if j < w:
            # 이전 물건까지만 고려했을 때의 가치를 그대로 가져옴
            dp[i][j] = dp[i - 1][j]
        # 현재 물건을 담을 수 있는 경우
        else:
            # (이전 물건까지만 고려한 가치) vs (현재 물건을 담는 가치)
            # 현재 물건을 담는 가치 = 현재 물건 가치 + (현재 물건 무게를 뺀 용량으로 이전 물건까지 고려한 가치)
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[n][k])
