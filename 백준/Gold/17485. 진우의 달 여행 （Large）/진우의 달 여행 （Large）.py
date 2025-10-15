import sys

input = sys.stdin.readline

# main
n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]

dp = [[[float("inf")] * 3 for _ in range(m)] for _ in range(n)]  # d는 위치정보

for j in range(m):
    for d in range(3):
        dp[0][j][d] = s[0][j]

for i in range(1, n):
    for j in range(m):
        # 북서에서 온 것은 북 or 북동에서 온 것 중에 선택
        if j > 0:
            dp[i][j][0] = s[i][j] + min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2])

        # 북에서 온 것은 북서 or 북동에서 온 것 중에 선택
        dp[i][j][1] = s[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])

        # 북동에서 온 것은 북서 or 북에서 온 것 중에 선택
        if j < m - 1:
            dp[i][j][2] = s[i][j] + min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1])

answer = float("inf")

for j in range(m):
    answer = min(answer, min(dp[n - 1][j]))

print(answer)
